# TimeShiftVR Promotion — R3 FX Ownership Scope Correction

CLAIM_ID: TS-FX-PASS-OWNER
ROLE: R3
TARGET: canonical TimeShiftVR missing-FX state/navigation
EVIDENCE_CLASS: SCOPE_RECONCILIATION_WITH_LATER_MASTER
PRIOR_SCOPE: EYE_DONE / final-color transaction ownership promoted as the primary R3 gate
NEW_SCOPE: View* -> DAT_00FCACD8 +0x9C(View) -> FX queue/list/membership -> consumer, with EYE_DONE/680EF0 retained as BORROWED sibling evidence

## Why this correction exists
The 2026-09-08 EYE_DONE convergence correctly retired stale OMNI v6.1 guidance and preserved strong native late-tail evidence, but subsequent synchronization against the later 2026-09-04 portable/master state exposed a role-scope collision.

That later authority explicitly separates:
- R3 renderer-graph / shared-vs-per-eye ownership: `View* -> DAT_00FCACD8 +0x9C -> FX queue/list/membership -> consumer`;
- R2 historical/runtime fanout candidates involving repeated `0x00680EF0`, rain-queue behavior and late eye teardown.

Under `docs/BRANCH_PROMOTION_POLICY.md`, cross-role imports remain `BORROWED_EVIDENCE` until independently closed in the receiving role. Therefore EYE_DONE evidence may constrain R3, but cannot silently replace the R3 PRIMARY fact.

## Accepted delta
Keep the existing active claim `TS-FX-PASS-OWNER`; do not create a duplicate claim.

Restore the R3 serial gate to:
```text
View*
  -> DAT_00FCACD8 +0x9C(View)
  -> FX queue/list/membership
  -> consumer
```

Retain as required context:
- current synthetic RIGHT reuses LEFT/main high-level `View*` at `0x0067F4F0 arg1`;
- `DAT_00FCACD8 +0x8C/+0x90` register/unregister object families;
- `+0x28/+0x2C` form a per-View preparation/membership surface;
- native MAIN has the bracket `+0x78 -> +0x9C(View) -> +0x7C`;
- exact semantics and downstream consumers remain UNKNOWN and COLD.

## Borrowed evidence retained, not deleted
The previous promotion's exact late-tail facts remain useful:
- `0x0067F4F0` is not proven EYE_DONE;
- native late rain/overlay/final work continues after current RIGHT return;
- final `425/6FDF` remains eye0-only in preserved v6.13 lineage;
- older captures show strong final composition on the real backbuffer;
- the existing backbuffer routing hook depends on eye ownership still being active;
- `DELAY_RIGHT_TEARDOWN_ONLY` remains unexecuted.

These are now explicitly marked `BORROWED_EVIDENCE` for R3. This correction does not falsify them and does not claim a new execution occurred.

## Orthogonal shadow-cache evidence retained
One-shot TS-LIVE-005 mechanically restored a native RIGHT bind -> 102 draws -> cleanup transaction after one cache miss. Preserve it as structural proof of a local activation-lifetime defect; do not promote it as a universal missing-FX fix.

## Machine contract reconciliation
`RESEARCH_CONTRACT.yaml.active_gate_anchor` is updated from the prior EYE_DONE wording to `Current R3 FIRST_MISSING_EDGE`, matching the canonical `docs/STATE.md` and the existing claim graph state anchor. This is part of the same scope correction, not a checker bypass.

## Protected baseline
No change to:
- exact retail identity;
- v4.7.2 OLD-GOOD true stereo;
- OLD-GOOD + DIP exact TEX0+TEX1 current-best effect state;
- closed generic replay negatives;
- R4 sidecar ownership;
- executed PASS/FAIL history.

## New canonical execution status
```text
COLD = CONTINUE
LIVE = DENIED
VALID_FRESH_LIVE_TICKET = NONE
```

## Canonical files changed
- `RESEARCH_CONTRACT.yaml`
- `README.md`
- `LATEST_SYNC.md`
- `CLAIM_GRAPH.json`
- `docs/STATE.md`
- `docs/NEXT.md`
- `docs/SYNC.md`
- `docs/ACTIVE_CLAIMS.md`
- this promotion record

## STOP RULE
This is a scope correction, not a runtime authorization. R3 must cold-close `View* -> +0x9C -> queue/list/membership -> consumer` before handing any executable one-mutation ticket to the incumbent implementation owner.
