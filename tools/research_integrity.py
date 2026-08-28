#!/usr/bin/env python3
from __future__ import annotations
import argparse, datetime as dt, difflib, json, os, re, subprocess, urllib.error, urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PREFLIGHT=["MISSING FACT:","WHY NOT COLD:","PASS:","FAIL:","BASELINE MUST HOLD:"]
MUTATION_EXT={".bat",".cmd",".ps1",".py",".c",".cc",".cpp",".h",".hpp",".zig",".ini",".cfg",".json",".yaml",".yml",".toml"}
CLAIM_STATUSES={"ACTIVE","PENDING","QUEUED","PARKED","PROVEN","FALSIFIED","SUPERSEDED"}; CLOSED={"PROVEN","FALSIFIED","SUPERSEDED"}; CLASSES={"COLD","PASSIVE_LIVE","CAUSAL_LIVE","BUILD_LIVE"}; LIVE=CLASSES-{"COLD"}
STOP={"the","a","an","and","or","of","to","for","in","on","at","by","with","from","current","exact","runtime","project","gate","path","vr","result","proof","owner","ownership"}
def fail(m,e):e.append(m);print("ERROR:",m)
def warn(m):print("WARN:",m)
def read(p):return p.read_text(encoding="utf-8",errors="replace")
def load(p,l,e):
 try:return json.loads(read(p))
 except Exception as x:fail(f"{l} must be JSON-compatible: {x}",e);return None
def dateof(s):
 m=re.search(r"(?<!\d)(20\d{2})[-_/](\d{2})[-_/](\d{2})(?!\d)",s) or re.search(r"(?<!\d)(20\d{2})(\d{2})(\d{2})(?!\d)",s)
 if not m:return None
 try:return dt.date(*map(int,m.groups()))
 except ValueError:return None
def changed(b):
 if not b or not re.fullmatch(r"[0-9a-fA-F]{7,40}",b) or set(b)=={"0"}:return []
 try:o=subprocess.check_output(["git","diff","--name-status",f"{b}...HEAD"],cwd=ROOT,text=True,stderr=subprocess.STDOUT)
 except subprocess.CalledProcessError as x:warn("git diff failed: "+x.output.strip());return []
 return [(x.split("\t")[0],x.split("\t")[-1]) for x in o.splitlines() if "\t" in x]
def norm(s):return " ".join(t for t in re.findall(r"[a-z0-9]+",str(s).casefold()) if len(t)>1 and t not in STOP)
def graph_check(c,e):
 rel=c.get("claim_graph","CLAIM_GRAPH.json");p=ROOT/rel
 if not p.exists():fail(f"claim graph missing: {rel}",e);return {},{}
 g=load(p,rel,e)
 if not isinstance(g,dict):return {},{}
 if g.get("schema_version")!=1:fail(f"{rel}: schema_version must be 1",e)
 if g.get("project")!=c.get("project"):fail(f"{rel}: project mismatch",e)
 cs={};es={}
 for r in g.get("claims",[]):
  cid=str(r.get("id","")).strip()
  if not cid or cid in cs:fail(f"{rel}: missing/duplicate claim id {cid!r}",e);continue
  if r.get("status") not in CLAIM_STATUSES:fail(f"{cid}: invalid status {r.get('status')!r}",e)
  if not str(r.get("summary","")).strip():fail(f"{cid}: missing summary",e)
  cs[cid]=r
 for r in g.get("evidence",[]):
  eid=str(r.get("id","")).strip()
  if not eid or eid in es:fail(f"{rel}: missing/duplicate evidence id {eid!r}",e);continue
  if not str(r.get("ref","")).strip():fail(f"{eid}: missing ref",e)
  if r.get("repo_path") and not (ROOT/r["repo_path"]).exists():fail(f"{eid}: missing repo_path {r['repo_path']}",e)
  es[eid]=r
 for cid,r in cs.items():
  for eid in r.get("evidence_ids",[]):
   if eid not in es:fail(f"{cid}: unknown evidence {eid}",e)
  for k in ("blocks","supersedes","allow_similarity_with"):
   for x in r.get(k,[]):
    if x not in cs:fail(f"{cid}: {k} unknown claim {x}",e)
  if r.get("status") in CLOSED and not r.get("evidence_ids"):warn(f"CLOSED_CLAIM_WITHOUT_EVIDENCE: {cid} status={r.get('status')}")
 fp={}
 for cid,r in cs.items():
  for s in [r.get("summary","")]+r.get("aliases",[])+r.get("fingerprints",[]):
   n=norm(s)
   if not n:continue
   if n in fp and fp[n]!=cid and fp[n] not in r.get("allow_similarity_with",[]) and cid not in cs[fp[n]].get("allow_similarity_with",[]):fail(f"DUPLICATE_CLAIM_FINGERPRINT: {cid} ~ {fp[n]} => {n}",e)
   fp.setdefault(n,cid)
 items=list(cs.items())
 for i,(a,ra) in enumerate(items):
  for b,rb in items[i+1:]:
   if b in ra.get("allow_similarity_with",[]) or a in rb.get("allow_similarity_with",[]):continue
   na,nb=norm(ra.get("summary","")),norm(rb.get("summary",""));ta,tb=set(na.split()),set(nb.split());u=ta|tb
   if not na or not nb:continue
   j=len(ta&tb)/len(u) if u else 0;q=difflib.SequenceMatcher(None,na,nb).ratio()
   if j>=.82 and q>=.92:fail(f"POSSIBLE_DUPLICATE_CLAIM: {a} ~ {b} token={j:.2f} text={q:.2f}",e)
   elif j>=.72 and q>=.86:warn(f"CLAIM_SIMILARITY_REVIEW: {a} ~ {b} token={j:.2f} text={q:.2f}")
 active=c.get("active_claim_ids",[])
 if not active:fail("active_claim_ids is empty",e)
 for cid in active:
  if cid not in cs:fail(f"active_claim_ids unknown claim {cid}",e)
  elif cs[cid].get("status") not in {"ACTIVE","PENDING"}:fail(f"active claim {cid} status is {cs[cid].get('status')}",e)
 refs=set(c.get("pending_evidence_refs",[]));pcs={cid:r for cid,r in cs.items() if r.get("status")=="PENDING"}
 if bool(refs)!=bool(pcs):fail("PENDING_MISMATCH: pending_evidence_refs and PENDING claim set must both be empty or both be non-empty",e)
 for relp in sorted(refs):
  ids={eid for eid,r in es.items() if r.get("repo_path")==relp}
  if not ids:fail(f"PENDING_EVIDENCE_UNREGISTERED: {relp}",e);continue
  if not any(ids&set(r.get("evidence_ids",[])) for r in pcs.values()):fail(f"PENDING_EVIDENCE_UNLINKED: {relp}",e)
 return cs,es
def marker(p,label,e,allowed=None,prefix=None):
 if not p.exists():fail(f"{p.relative_to(ROOT)} missing",e);return None
 rows=[x.strip() for x in read(p).splitlines() if x.strip() and not x.lstrip().startswith("#")]
 if len(rows)!=1:fail(f"{p.relative_to(ROOT)} must contain exactly one non-empty value",e);return None
 v=rows[0]
 if prefix:
  if not v.startswith(prefix) or not v[len(prefix):].strip():fail(f"{p.relative_to(ROOT)} must be one non-empty line starting with '{prefix}'",e);return None
  v=v[len(prefix):].strip()
 if allowed and v not in allowed:fail(f"{p.relative_to(ROOT)} invalid {label} {v!r}; allowed={sorted(allowed)}",e);return None
 return v
def reopen(d,cid,e):
 p=d/"REOPEN_RATIONALE.md"
 if not p.exists():fail(f"CLAIM_CLOSED: {cid} requires REOPEN_RATIONALE.md or a new claim",e);return
 rows=[x.strip() for x in read(p).splitlines() if x.strip()]
 for pref in ("WHY_REOPEN:","NEW_EVIDENCE:"):
  v=next((x[len(pref):].strip() for x in rows if x.startswith(pref)),"")
  if not v:fail(f"{p.relative_to(ROOT)} requires non-empty '{pref}'",e)
  elif len(v)<12:fail(f"{p.relative_to(ROOT)} '{pref}' is too weak; provide a concrete reason",e)
def expmeta(d,cs,e):
 cid=marker(d/"CLAIM_ID.txt","CLAIM_ID",e);cl=marker(d/"EXPERIMENT_CLASS.txt","experiment class",e,CLASSES);marker(d/"PRIMARY_FACT.txt","primary fact",e,prefix="PRIMARY_FACT:")
 if cid:
  if cid not in cs:fail(f"{(d/'CLAIM_ID.txt').relative_to(ROOT)} unknown claim {cid}",e)
  elif cs[cid].get("status") in CLOSED:reopen(d,cid,e)
 return cid,cl
def preflight(d,e):
 p=d/"PREFLIGHT_5_LINES.txt"
 if not p.exists():fail(f"{p.relative_to(ROOT)} missing",e);return
 rows=[x.strip() for x in read(p).splitlines() if x.strip()]
 if len(rows)!=5:fail(f"{p.relative_to(ROOT)} must contain exactly 5 non-empty lines",e);return
 for got,need in zip(rows,PREFLIGHT):
  if not got.startswith(need) or not got[len(need):].strip():fail(f"{p.relative_to(ROOT)} bad line: expected {need}",e)
def isdelta(rel):
 p=Path(rel);n=p.name.casefold();return p.suffix.casefold()==".md" and p.parts and p.parts[0].casefold() in {"research","docs","experiments"} and ("result_delta" in n or "evidence_delta" in n)
def delta(p,es,cs,e):
 s="\n".join(read(p).splitlines()[:100]);me=re.search(r"(?im)^\s*EVIDENCE_ID:\s*(\S+)\s*$",s);mc=re.search(r"(?im)^\s*CLAIM_ID:\s*(\S+)\s*$",s)
 if not me or not mc:fail(f"{p.relative_to(ROOT)} must declare EVIDENCE_ID and CLAIM_ID in first 100 lines",e);return
 eid,cid=me.group(1),mc.group(1)
 if eid not in es:fail(f"{p.relative_to(ROOT)} unregistered EVIDENCE_ID {eid}",e)
 if cid not in cs:fail(f"{p.relative_to(ROOT)} unregistered CLAIM_ID {cid}",e)
 elif eid in es and eid not in cs[cid].get("evidence_ids",[]):fail(f"{eid} is not linked from claim {cid}",e)
def gh(url,t):
 req=urllib.request.Request(url,headers={"Accept":"application/vnd.github+json","Authorization":f"Bearer {t}","X-GitHub-Api-Version":"2022-11-28","User-Agent":"research-integrity-v2"})
 with urllib.request.urlopen(req,timeout=20) as r:return json.loads(r.read().decode())
def issue_sync(c,cs,e):
 n=c.get("current_issue_number")
 if not n:fail("current_issue_number is not declared",e);return
 t=os.getenv("GITHUB_TOKEN","").strip();repo=os.getenv("GITHUB_REPOSITORY","").strip()
 if not t or not repo:warn("ISSUE_SYNC_SKIPPED: GITHUB_TOKEN/GITHUB_REPOSITORY unavailable outside CI");return
 try:i=gh(f"https://api.github.com/repos/{repo}/issues/{n}",t);items=gh(f"https://api.github.com/repos/{repo}/issues?state=open&per_page=100",t)
 except (urllib.error.URLError,urllib.error.HTTPError,TimeoutError,json.JSONDecodeError) as x:fail(f"ISSUE_SYNC_API_ERROR: {x}",e);return
 if i.get("pull_request"):fail(f"current_issue_number {n} resolves to a pull request",e);return
 if i.get("state")!="open":fail(f"CURRENT_ISSUE_CLOSED: #{n}",e)
 title=str(i.get("title",""));body=str(i.get("body") or "")
 if not title.casefold().startswith("current:"):fail(f"CURRENT_ISSUE_TITLE: #{n} must start with 'CURRENT:'",e)
 sr=str(c.get("canonical_state",""))
 if sr and sr not in body:fail(f"CURRENT_ISSUE_STATE_LINK: #{n} does not mention {sr}",e)
 for cid in c.get("active_claim_ids",[]):
  if cid not in body:fail(f"CURRENT_ISSUE_CLAIM_MISSING: #{n} does not mention active claim {cid}",e)
 nums=sorted(int(x.get("number",0)) for x in items if "pull_request" not in x and str(x.get("title","")).casefold().startswith("current:"))
 if nums!=[int(n)]:fail(f"CURRENT_ISSUE_CARDINALITY: expected only #{n}, found {nums}",e)
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--base",default=os.getenv("BASE_SHA"));a=ap.parse_args();e=[]
 cp=ROOT/"RESEARCH_CONTRACT.yaml"
 if not cp.exists():fail("RESEARCH_CONTRACT.yaml missing",e);return 1
 c=load(cp,"RESEARCH_CONTRACT.yaml",e)
 if not isinstance(c,dict):return 1
 if c.get("schema_version")!=2:fail("unsupported RESEARCH_CONTRACT schema_version; expected 2",e)
 sr=c.get("canonical_state")
 if not sr or not (ROOT/sr).exists():fail(f"canonical state missing: {sr}",e);return 1
 state=read(ROOT/sr);sd=dateof("\n".join(state.splitlines()[:120]))
 if c.get("workflow") and not (ROOT/c["workflow"]).exists():fail(f"workflow missing: {c['workflow']}",e)
 if c.get("active_gate_anchor") and c["active_gate_anchor"].casefold() not in state.casefold():fail("active gate anchor missing from canonical state",e)
 if c.get("protected_baseline_anchor") and c["protected_baseline_anchor"].casefold() not in state.casefold():fail("protected baseline anchor missing from canonical state",e)
 cs,es=graph_check(c,e);pending=set(c.get("pending_evidence_refs",[]))
 for rel in pending:
  if not (ROOT/rel).exists():fail(f"pending evidence missing: {rel}",e)
 latest=None
 for pat in c.get("evidence_globs",[]):
  for p in ROOT.glob(pat):
   if p.is_file():
    d=dateof(p.name) or dateof("\n".join(read(p).splitlines()[:40]))
    if d and (latest is None or d>latest[0]):latest=(d,p)
 if latest and sd and latest[0]>sd:
  rel=latest[1].relative_to(ROOT).as_posix();nm=latest[1].name
  if rel.casefold() not in state.casefold() and nm.casefold() not in state.casefold():
   if rel in pending:warn(f"STATE_PENDING: {rel} newer than STATE and queued for convergence")
   else:fail(f"STATE_STALE: {rel}@{latest[0]} newer than STATE@{sd}",e)
 ch=changed(a.base);dirs=set()
 for st,rel in ch:
  p=Path(rel)
  if p.parts and p.parts[0].casefold()=="experiments" and p.suffix.casefold() in MUTATION_EXT and len(p.parts)>=2:dirs.add(ROOT/p.parts[0]/p.parts[1])
  if c.get("require_headers_for_changed_evidence_delta",True) and not st.startswith("D") and isdelta(rel) and (ROOT/p).exists():delta(ROOT/p,es,cs,e)
 live=set()
 for d in sorted(dirs):
  _,cl=expmeta(d,cs,e)
  if cl in LIVE:live.add(d);preflight(d,e)
 if live and pending and c.get("block_live_when_pending",True):fail("LIVE_BLOCKED_BY_PENDING_EVIDENCE",e)
 issue_sync(c,cs,e)
 print();print("PROJECT="+str(c.get("project","UNKNOWN")));print("CANONICAL_STATE="+str(sr));print("STATE_DATE="+str(sd or "UNKNOWN"));print("CLAIMS="+str(len(cs)));print("EVIDENCE_IDS="+str(len(es)));print("ACTIVE_CLAIMS="+",".join(c.get("active_claim_ids",[])));print("PENDING_EVIDENCE="+str(len(pending)));print("CHANGED_FILES="+str(len(ch)));print("EXPERIMENT_DIRS_CHECKED="+str(len(dirs)));print("LIVE_EXPERIMENT_DIRS_CHECKED="+str(len(live)));print("ERRORS="+str(len(e)));print("VERDICT="+("PASS" if not e else "FAIL"));return 0 if not e else 1
if __name__=="__main__":raise SystemExit(main())
