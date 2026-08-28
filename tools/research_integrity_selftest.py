#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, tempfile
from pathlib import Path
import research_integrity as ri
ROOT=Path(__file__).resolve().parents[1]; CLOSED={"PROVEN","FALSIFIED","SUPERSEDED"}; APPROVED={"7a35741e525755ccefc3d4b79c32aba420bb9bd0","680cea4e2d868cfcc96764eb72e94038625b55ed"}
def die(s): raise SystemExit("SELFTEST_FAIL: "+s)
def blob(p):
 d=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(d)).encode()+b"\0"+d).hexdigest()
def neederr(n,e):
 if not e: die(n+" incorrectly accepted")
def clean(n,e):
 if e: die(n+" unexpectedly failed: "+" | ".join(e))
def pick(*ns):
 for n in ns:
  f=getattr(ri,n,None)
  if callable(f): return f
 die("checker API missing: "+"/".join(ns))
def main():
 h=blob(ROOT/"tools/research_integrity.py")
 if h not in APPROVED: die("unreviewed checker blob "+h)
 c=json.loads((ROOT/"RESEARCH_CONTRACT.yaml").read_text(encoding="utf-8")); g=json.loads((ROOT/"CLAIM_GRAPH.json").read_text(encoding="utf-8"))
 if c.get("schema_version")!=2: die("contract schema is not v2")
 debt=[x.get("id") for x in g.get("claims",[]) if x.get("status") in CLOSED and not x.get("evidence_ids")]
 if debt: die("closed claims without evidence: "+", ".join(map(str,debt)))
 pre=pick("preflight","validate_preflight"); reo=pick("reopen","validate_reopen_rationale"); de=pick("delta","validate_delta_headers"); ex=pick("expmeta","experiment_metadata"); gc=pick("graph_check"); old=ri.ROOT
 try:
  with tempfile.TemporaryDirectory() as td:
   r=Path(td); ri.ROOT=r; d=r/"experiments/probe"; d.mkdir(parents=True)
   (d/"PREFLIGHT_5_LINES.txt").write_text("MISSING FACT: x\nWHY NOT COLD: y\nPASS: z\nFAIL: q\n",encoding="utf-8"); e=[]; pre(d,e); neederr("four-line preflight",e)
   (d/"PREFLIGHT_5_LINES.txt").write_text("MISSING FACT: one fact\nWHY NOT COLD: runtime required\nPASS: positive discriminator\nFAIL: negative discriminator\nBASELINE MUST HOLD: baseline unchanged\n",encoding="utf-8"); e=[]; pre(d,e); clean("five-line preflight",e)
   (d/"REOPEN_RATIONALE.md").write_text("\n",encoding="utf-8"); e=[]; reo(d,"CLOSED",e); neederr("empty reopen",e)
   (d/"REOPEN_RATIONALE.md").write_text("WHY_REOPEN: new exact-retail result contradicts the prior owner\nNEW_EVIDENCE: RESULT-NEW proves a different causal owner\n",encoding="utf-8"); e=[]; reo(d,"CLOSED",e); clean("reopen rationale",e)
   p=r/"research/RESULT_DELTA_TEST.md"; p.parent.mkdir(); p.write_text("# no ids\n",encoding="utf-8"); ev={"EV":{"id":"EV"}}; cl={"CL":{"evidence_ids":["EV"]}}; e=[]; de(p,ev,cl,e); neederr("delta without ids",e)
   p.write_text("EVIDENCE_ID: EV\nCLAIM_ID: CL\n",encoding="utf-8"); e=[]; de(p,ev,cl,e); clean("registered delta",e)
   (r/"CLAIM_GRAPH.json").write_text(json.dumps({"schema_version":1,"project":"T","claims":[{"id":"A","status":"ACTIVE","summary":"one","fingerprints":["same owner question"],"evidence_ids":[]},{"id":"B","status":"QUEUED","summary":"two","fingerprints":["same owner question"],"evidence_ids":[]}],"evidence":[]}),encoding="utf-8"); e=[]; gc({"project":"T","claim_graph":"CLAIM_GRAPH.json","active_claim_ids":["A"],"pending_evidence_refs":[]},e); neederr("duplicate fingerprint",e)
   (d/"CLAIM_ID.txt").write_text("A\n",encoding="utf-8"); (d/"EXPERIMENT_CLASS.txt").write_text("COLD\n",encoding="utf-8"); e=[]; ex(d,{"A":{"status":"ACTIVE"}},e); neederr("missing primary fact",e)
   (d/"PRIMARY_FACT.txt").write_text("PRIMARY_FACT: one bounded owner identity\n",encoding="utf-8"); (d/"EXPERIMENT_CLASS.txt").write_text("COLDISH\n",encoding="utf-8"); e=[]; ex(d,{"A":{"status":"ACTIVE"}},e); neederr("invalid experiment class",e)
   (d/"EXPERIMENT_CLASS.txt").write_text("COLD\n",encoding="utf-8"); e=[]; _,k=ex(d,{"A":{"status":"ACTIVE"}},e); clean("valid experiment metadata",e)
   if k!="COLD": die("explicit experiment class not authoritative")
 finally: ri.ROOT=old
 print("RESEARCH_INTEGRITY_SELFTEST=PASS"); print("CHECKER_GIT_BLOB="+h); return 0
if __name__=="__main__": raise SystemExit(main())
