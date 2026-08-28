#!/usr/bin/env python3
from __future__ import annotations
import argparse, datetime as dt, difflib, json, os, re, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PREFLIGHT=["MISSING FACT:","WHY NOT COLD:","PASS:","FAIL:","BASELINE MUST HOLD:"]
CODE_EXT={".bat",".cmd",".ps1",".py",".c",".cc",".cpp",".h",".hpp",".zig"}
STATUSES={"ACTIVE","PENDING","QUEUED","PARKED","PROVEN","FALSIFIED","SUPERSEDED"}
BLOCKED={"PROVEN","FALSIFIED","SUPERSEDED"}
STOP={"the","a","an","and","or","of","to","for","in","on","at","by","with","from","current","exact","runtime","project","gate","path","vr","result","proof","owner","ownership"}
def fail(msg,errors): errors.append(msg); print("ERROR:",msg)
def warn(msg): print("WARN:",msg)
def read(p): return p.read_text(encoding="utf-8",errors="replace")
def load(p,label,errors):
    try:return json.loads(read(p))
    except Exception as e: fail(f"{label} must be JSON-compatible: {e}",errors); return None
def dateof(s):
    m=re.search(r"(?<!\d)(20\d{2})[-_/](\d{2})[-_/](\d{2})(?!\d)",s) or re.search(r"(?<!\d)(20\d{2})(\d{2})(\d{2})(?!\d)",s)
    if not m:return None
    try:return dt.date(*map(int,m.groups()))
    except ValueError:return None
def changed(base):
    if not base or not re.fullmatch(r"[0-9a-fA-F]{7,40}",base) or set(base)=={"0"}: return []
    try:o=subprocess.check_output(["git","diff","--name-status",f"{base}...HEAD"],cwd=ROOT,text=True,stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e: warn("git diff failed: "+e.output.strip()); return []
    return [(x.split("\t")[0],x.split("\t")[-1]) for x in o.splitlines() if "\t" in x]
def norm(s): return " ".join(t for t in re.findall(r"[a-z0-9]+",s.casefold()) if len(t)>1 and t not in STOP)
def graph_check(c,errors):
    rel=c.get("claim_graph","CLAIM_GRAPH.json"); p=ROOT/rel
    if not p.exists(): fail(f"claim graph missing: {rel}",errors); return {},{}
    g=load(p,rel,errors)
    if not isinstance(g,dict): return {},{}
    if g.get("schema_version")!=1: fail(f"{rel}: schema_version must be 1",errors)
    if g.get("project")!=c.get("project"): fail(f"{rel}: project mismatch",errors)
    claims={}; evidence={}
    for r in g.get("claims",[]):
        cid=r.get("id","").strip()
        if not cid or cid in claims: fail(f"{rel}: missing/duplicate claim id {cid!r}",errors); continue
        if r.get("status") not in STATUSES: fail(f"{cid}: invalid status {r.get('status')!r}",errors)
        if not str(r.get("summary","")).strip(): fail(f"{cid}: missing summary",errors)
        claims[cid]=r
    for r in g.get("evidence",[]):
        eid=r.get("id","").strip()
        if not eid or eid in evidence: fail(f"{rel}: missing/duplicate evidence id {eid!r}",errors); continue
        if not str(r.get("ref","")).strip(): fail(f"{eid}: missing ref",errors)
        if r.get("repo_path") and not (ROOT/r["repo_path"]).exists(): fail(f"{eid}: missing repo_path {r['repo_path']}",errors)
        evidence[eid]=r
    for cid,r in claims.items():
        for eid in r.get("evidence_ids",[]):
            if eid not in evidence: fail(f"{cid}: unknown evidence {eid}",errors)
        for k in ("blocks","supersedes","allow_similarity_with"):
            for x in r.get(k,[]):
                if x not in claims: fail(f"{cid}: {k} unknown claim {x}",errors)
    fp={}
    for cid,r in claims.items():
        for s in [r.get("summary","")]+r.get("aliases",[])+r.get("fingerprints",[]):
            n=norm(str(s))
            if not n: continue
            if n in fp and fp[n]!=cid and fp[n] not in r.get("allow_similarity_with",[]) and cid not in claims[fp[n]].get("allow_similarity_with",[]): fail(f"DUPLICATE_CLAIM_FINGERPRINT: {cid} ~ {fp[n]} => {n}",errors)
            fp.setdefault(n,cid)
    items=list(claims.items())
    for i,(a,ra) in enumerate(items):
        for b,rb in items[i+1:]:
            if b in ra.get("allow_similarity_with",[]) or a in rb.get("allow_similarity_with",[]): continue
            na,nb=norm(ra.get("summary","")),norm(rb.get("summary",""))
            if not na or not nb: continue
            ta,tb=set(na.split()),set(nb.split()); u=ta|tb; j=len(ta&tb)/len(u) if u else 0; q=difflib.SequenceMatcher(None,na,nb).ratio()
            if j>=.82 and q>=.92: fail(f"POSSIBLE_DUPLICATE_CLAIM: {a} ~ {b} token={j:.2f} text={q:.2f}",errors)
            elif j>=.72 and q>=.86: warn(f"CLAIM_SIMILARITY_REVIEW: {a} ~ {b} token={j:.2f} text={q:.2f}")
    active=c.get("active_claim_ids",[])
    if not active: fail("active_claim_ids is empty",errors)
    for cid in active:
        if cid not in claims: fail(f"active_claim_ids unknown claim {cid}",errors)
        elif claims[cid].get("status") not in {"ACTIVE","PENDING"}: fail(f"active claim {cid} status is {claims[cid].get('status')}",errors)
    return claims,evidence
def preflight(d,errors):
    p=d/"PREFLIGHT_5_LINES.txt"
    if not p.exists(): fail(f"{p.relative_to(ROOT)} missing",errors); return
    rows=[x.strip() for x in read(p).splitlines() if x.strip()]
    if len(rows)!=5: fail(f"{p.relative_to(ROOT)} must contain exactly 5 non-empty lines",errors); return
    for got,need in zip(rows,PREFLIGHT):
        if not got.startswith(need) or not got[len(need):].strip(): fail(f"{p.relative_to(ROOT)} bad line: expected {need}",errors)
def claim_marker(d,claims,errors):
    p=d/"CLAIM_ID.txt"
    if not p.exists(): fail(f"{p.relative_to(ROOT)} missing",errors); return
    rows=[x.strip() for x in read(p).splitlines() if x.strip() and not x.lstrip().startswith("#")]
    if len(rows)!=1: fail(f"{p.relative_to(ROOT)} must contain exactly one claim id",errors); return
    cid=rows[0]
    if cid not in claims: fail(f"{p.relative_to(ROOT)} unknown claim {cid}",errors); return
    if claims[cid].get("status") in BLOCKED and not (d/"REOPEN_RATIONALE.md").exists(): fail(f"CLAIM_CLOSED: {cid} is {claims[cid].get('status')}; use a new claim or REOPEN_RATIONALE.md",errors)
def new_delta(status,rel):
    p=Path(rel); n=p.name.casefold()
    return status.startswith("A") and p.suffix.casefold()==".md" and p.parts and p.parts[0].casefold() in {"research","docs","experiments"} and ("result_delta" in n or "evidence_delta" in n)
def delta_headers(p,evidence,claims,errors):
    s="\n".join(read(p).splitlines()[:100]); me=re.search(r"(?im)^\s*EVIDENCE_ID:\s*(\S+)\s*$",s); mc=re.search(r"(?im)^\s*CLAIM_ID:\s*(\S+)\s*$",s)
    if not me or not mc: fail(f"{p.relative_to(ROOT)} must declare EVIDENCE_ID and CLAIM_ID in first 100 lines",errors); return
    eid,cid=me.group(1),mc.group(1)
    if eid not in evidence: fail(f"{p.relative_to(ROOT)} unregistered EVIDENCE_ID {eid}",errors)
    if cid not in claims: fail(f"{p.relative_to(ROOT)} unregistered CLAIM_ID {cid}",errors)
    elif eid in evidence and eid not in claims[cid].get("evidence_ids",[]): fail(f"{eid} is not linked from claim {cid}",errors)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--base",default=os.getenv("BASE_SHA")); a=ap.parse_args(); errors=[]
    cp=ROOT/"RESEARCH_CONTRACT.yaml"
    if not cp.exists(): fail("RESEARCH_CONTRACT.yaml missing",errors); return 1
    c=load(cp,"RESEARCH_CONTRACT.yaml",errors)
    if not isinstance(c,dict): return 1
    sr=c.get("canonical_state")
    if not sr or not (ROOT/sr).exists(): fail(f"canonical state missing: {sr}",errors); return 1
    state=read(ROOT/sr); sd=dateof("\n".join(state.splitlines()[:120]))
    if c.get("workflow") and not (ROOT/c["workflow"]).exists(): fail(f"workflow missing: {c['workflow']}",errors)
    if c.get("active_gate_anchor") and c["active_gate_anchor"].casefold() not in state.casefold(): fail("active gate anchor missing from canonical state",errors)
    if c.get("protected_baseline_anchor") and c["protected_baseline_anchor"].casefold() not in state.casefold(): fail("protected baseline anchor missing from canonical state",errors)
    claims,evidence=graph_check(c,errors); pending=set(c.get("pending_evidence_refs",[]))
    for rel in pending:
        if not (ROOT/rel).exists(): fail(f"pending evidence missing: {rel}",errors)
    latest=None
    for pat in c.get("evidence_globs",[]):
        for p in ROOT.glob(pat):
            if p.is_file():
                d=dateof(p.name) or dateof("\n".join(read(p).splitlines()[:40]))
                if d and (latest is None or d>latest[0]): latest=(d,p)
    if latest and sd and latest[0]>sd:
        rel=latest[1].relative_to(ROOT).as_posix(); nm=latest[1].name
        if rel.casefold() not in state.casefold() and nm.casefold() not in state.casefold():
            if rel in pending: warn(f"STATE_PENDING: {rel} newer than STATE and queued for convergence")
            else: fail(f"STATE_STALE: {rel}@{latest[0]} newer than STATE@{sd}",errors)
    ch=changed(a.base); exp=set(); live=set()
    for st,rel in ch:
        p=Path(rel)
        if c.get("require_headers_for_new_evidence_delta",True) and new_delta(st,rel) and (ROOT/p).exists(): delta_headers(ROOT/p,evidence,claims,errors)
        if p.parts and p.parts[0].casefold()=="experiments" and p.suffix.casefold() in CODE_EXT and len(p.parts)>=2:
            d=ROOT/p.parts[0]/p.parts[1]; exp.add(d)
            if "cold" not in p.as_posix().casefold(): live.add(d)
    if c.get("require_claim_id_for_changed_experiments",True):
        for d in sorted(exp): claim_marker(d,claims,errors)
    for d in sorted(live): preflight(d,errors)
    if live and pending and c.get("block_live_when_pending",True): fail("LIVE_BLOCKED_BY_PENDING_EVIDENCE",errors)
    print(); print("PROJECT="+str(c.get("project","UNKNOWN"))); print("CANONICAL_STATE="+sr); print("STATE_DATE="+str(sd or "UNKNOWN")); print("CLAIMS="+str(len(claims))); print("EVIDENCE_IDS="+str(len(evidence))); print("ACTIVE_CLAIMS="+",".join(c.get("active_claim_ids",[]))); print("PENDING_EVIDENCE="+str(len(pending))); print("CHANGED_FILES="+str(len(ch))); print("EXPERIMENT_DIRS_CHECKED="+str(len(exp))); print("LIVE_EXPERIMENT_DIRS_CHECKED="+str(len(live))); print("ERRORS="+str(len(errors))); print("VERDICT="+("PASS" if not errors else "FAIL")); return 0 if not errors else 1
if __name__=="__main__": raise SystemExit(main())
