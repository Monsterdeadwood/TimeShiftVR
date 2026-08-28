#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, re, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DOC_CLASSES={"EVIDENCE","CONVERGENCE","NOTE","ARCHIVE","INDEX","DESIGN","SYNC"}
AUTHORITATIVE={"EVIDENCE","CONVERGENCE"}

def err(msg,errors): errors.append(msg); print("ERROR:",msg)
def read(path): return path.read_text(encoding="utf-8",errors="replace")
def load(path): return json.loads(read(path))
def changed(base):
    if not base or not re.fullmatch(r"[0-9a-fA-F]{7,40}",str(base)) or set(str(base))=={"0"}: return []
    try: out=subprocess.check_output(["git","diff","--name-status",f"{base}...HEAD"],cwd=ROOT,text=True,stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as exc:
        print("WARN: git diff failed:",exc.output.strip()); return []
    rows=[]
    for line in out.splitlines():
        p=line.split("\t")
        if len(p)>=2: rows.append((p[0],p[-1]))
    return rows

def headers(path):
    head="\n".join(read(path).splitlines()[:80])
    def one(name):
        m=re.search(rf"(?im)^\s*{re.escape(name)}:\s*(\S.*?)\s*$",head)
        return m.group(1).strip() if m else None
    return {"class":one("RESEARCH_DOC_CLASS"),"evidence":one("EVIDENCE_ID"),"claim":one("CLAIM_ID"),"superseded_by":one("SUPERSEDED_BY")}

def maps(graph):
    claims={str(x.get("id")):x for x in graph.get("claims",[]) if x.get("id")}
    evidence={str(x.get("id")):x for x in graph.get("evidence",[]) if x.get("id")}
    return claims,evidence

def state_mentions(state_text,rel):
    low=state_text.casefold(); p=Path(rel)
    return rel.casefold() in low or p.name.casefold() in low

def validate_doc(rel,path,contract,claims,evidence,state_changed,state_text,errors):
    h=headers(path); klass=h["class"]
    if not klass: err(f"RESEARCH_DOC_IDENTITY_MISSING: {rel} requires RESEARCH_DOC_CLASS",errors); return
    klass=klass.upper()
    if klass not in DOC_CLASSES: err(f"RESEARCH_DOC_CLASS_INVALID: {rel} => {klass}",errors); return
    if klass=="ARCHIVE" and h.get("superseded_by"):
        target=ROOT/h["superseded_by"]
        if not target.exists(): err(f"ARCHIVE_SUPERSEDED_TARGET_MISSING: {rel} -> {h['superseded_by']}",errors)
    if klass not in AUTHORITATIVE: return
    eid,cid=h["evidence"],h["claim"]
    if not eid or not cid: err(f"RESEARCH_DOC_IDS_MISSING: {rel} {klass} requires EVIDENCE_ID + CLAIM_ID",errors); return
    if eid not in evidence: err(f"RESEARCH_DOC_EVIDENCE_UNREGISTERED: {rel} => {eid}",errors)
    else:
        ep=evidence[eid].get("repo_path")
        if ep!=rel: err(f"RESEARCH_DOC_PATH_MISMATCH: {eid} repo_path={ep!r}, file={rel!r}",errors)
    if cid not in claims: err(f"RESEARCH_DOC_CLAIM_UNREGISTERED: {rel} => {cid}",errors)
    elif eid not in claims[cid].get("evidence_ids",[]): err(f"RESEARCH_DOC_UNLINKED: {eid} not linked from {cid}",errors)
    pending=set(contract.get("pending_evidence_refs",[])); converged=state_changed or state_mentions(state_text,rel)
    if not converged and rel not in pending: err(f"UNCONVERGED_RESEARCH_DOC: {rel} changed without canonical state convergence or pending registration",errors)
    if rel in pending and cid in claims and claims[cid].get("status")!="PENDING": err(f"PENDING_DOC_CLAIM_NOT_PENDING: {rel} -> {cid} status={claims[cid].get('status')}",errors)

def audit_pending(contract,claims,evidence,errors):
    pending=set(contract.get("pending_evidence_refs",[]))
    for rel in sorted(pending):
        p=ROOT/rel
        if not p.exists(): err(f"PENDING_DOC_MISSING: {rel}",errors); continue
        ids=[eid for eid,row in evidence.items() if row.get("repo_path")==rel]
        if not ids: err(f"PENDING_DOC_UNREGISTERED: {rel}",errors); continue
        linked=[cid for cid,row in claims.items() if set(ids)&set(row.get("evidence_ids",[]))]
        if not linked: err(f"PENDING_DOC_UNLINKED: {rel}",errors)
        elif not any(claims[cid].get("status")=="PENDING" for cid in linked): err(f"PENDING_DOC_HAS_NO_PENDING_CLAIM: {rel}",errors)
        h=headers(p)
        if (h.get("class") or "").upper() not in AUTHORITATIVE: err(f"PENDING_DOC_NOT_AUTHORITATIVE: {rel}",errors)

def audit_active_state_anchors(contract,claims,state_text,errors):
    if not contract.get("require_active_claim_state_anchor",False): return
    low=state_text.casefold()
    for cid in contract.get("active_claim_ids",[]):
        row=claims.get(cid)
        if not row: continue
        anchor=str(row.get("state_anchor","")).strip()
        if not anchor: err(f"ACTIVE_CLAIM_STATE_ANCHOR_MISSING: {cid}",errors)
        elif anchor.casefold() not in low: err(f"ACTIVE_CLAIM_STATE_DRIFT: {cid} anchor not found in canonical state: {anchor}",errors)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--base",default=os.getenv("BASE_SHA")); args=ap.parse_args(); errors=[]
    contract=load(ROOT/"RESEARCH_CONTRACT.yaml"); graph=load(ROOT/contract.get("claim_graph","CLAIM_GRAPH.json")); claims,evidence=maps(graph)
    state_rel=str(contract.get("canonical_state","")); state_path=ROOT/state_rel; state_text=read(state_path) if state_path.exists() else ""
    changes=changed(args.base); state_changed=any((not st.startswith("D")) and rel==state_rel for st,rel in changes)
    checked=0
    if contract.get("require_research_doc_identity_for_changes",False):
        for st,rel in changes:
            p=Path(rel)
            if st.startswith("D") or len(p.parts)<2 or p.parts[0].casefold()!="research" or p.suffix.casefold()!=".md": continue
            full=ROOT/p
            if not full.exists(): continue
            checked+=1; validate_doc(p.as_posix(),full,contract,claims,evidence,state_changed,state_text,errors)
    audit_pending(contract,claims,evidence,errors); audit_active_state_anchors(contract,claims,state_text,errors)
    print("RESEARCH_DOCS_CHECKED="+str(checked)); print("STATE_CHANGED="+("YES" if state_changed else "NO")); print("PENDING_DOCS="+str(len(contract.get("pending_evidence_refs",[])))); print("DOC_ERRORS="+str(len(errors))); print("DOC_VERDICT="+("PASS" if not errors else "FAIL"))
    return 0 if not errors else 1

if __name__=="__main__": raise SystemExit(main())
