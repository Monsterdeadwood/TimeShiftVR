# TimeShiftVR — LATEST SYNC

SYNC_EPOCH = 2026-09-08
ACTIVE_CLAIM = `TS-FX-PASS-OWNER`
CURRENT_R3_GATE = `VIEW_TO_FX_MEMBERSHIP_OWNERSHIP`
LIVE = DENIED

## Mandatory read order
1. `docs/STATE.md` — canonical truth and protected OLD-GOOD baseline.
2. `docs/NEXT.md` — exact current COLD edge and STOP rules.
3. `docs/ACTIVE_CLAIMS.md` — role ownership and collision law.
4. `docs/EVIDENCE_BOUNDARY.md` and `docs/BRANCH_PROMOTION_POLICY.md`.
5. Exact preserved RESULT/source corpus for any claim being advanced.

## Generic continuation gate
On `думайте дальше` / generic continuation, resolve current status/owner first: `ACTIVE` -> own FIRST_MISSING_EDGE only; `PENDING` -> ingest/validate; `HOLD/BLOCKED` -> blocker only; `CLOSED/PROVEN/FALSIFIED/SUPERSEDED/DO_NOT_REPEAT` -> STOP that PRIMARY_FACT; `UNBOUND` -> COLD only; conflict -> adjudicate before mutation. Generic continuation never authorizes sibling-claim takeover or LIVE/build by itself.

## Current canonical direction
The serial gate is no longer `TIMESHIFTVR_OMNI_EXACT_CLOSURE_v6.1.0` and is not generic texture/state replay.

R3 PRIMARY:
```text
View*
  -> DAT_00FCACD8 +0x9C(View)
  -> FX queue/list/membership
  -> consumer
```

Required RIGHT semantic input remains `rightView = 0x0067F4F0 arg1`.

Known surrounding ownership surface:
- `DAT_00FCACD8 +0x8C/+0x90` register/unregister scene objects;
- `+0x28/+0x2C` participate in per-View preparation/membership;
- MAIN-only native bracket is `+0x78 -> +0x9C(View) -> +0x7C`;
- exact semantics and downstream consumers remain the active COLD unknown.

## Borrowed sibling constraints
Preserved EYE_DONE/final-color evidence is retained as `BORROWED_EVIDENCE`:
- native late rain/overlay/final work continues after current RIGHT inner return;
- current wrapper releases eye ownership before that late work;
- final `425/6FDF` is eye0-only in preserved v6.13 lineage;
- `DELAY_RIGHT_TEARDOWN_ONLY` has no accepted RESULT.

This evidence constrains the R3 graph but does not make the sibling runtime canary the R3 PRIMARY gate.

## Orthogonal shadow defect
One-shot TS-LIVE-005 structurally restored a native RIGHT shadow bind -> 102 draws -> cleanup transaction after one cache miss. Keep this separate from View/FX membership and from EYE_DONE final-color ownership.

## Governance
R3 is structural REDTEAM. COLD may narrow UNKNOWN/NEXT but cannot silently rewrite OLD-GOOD, executed PASS/FAIL or another role's claim. Any executable mutation requires an incumbent implementation-owner ticket and the mandatory five causal lines.
