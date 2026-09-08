# TimeShiftVR - ACTIVE COLD LANES REGISTRY

CONTROL_PLANE_ONLY. The filename `docs/ACTIVE_CLAIMS.md` is retained for compatibility, but this file does **not** own canonical claim status.

Canonical `ACTIVE / PENDING / QUEUED / PROVEN / FALSIFIED / SUPERSEDED` status is owned only by `CLAIM_GRAPH.json` together with `RESEARCH_CONTRACT.yaml` and canonical state. This registry records isolated COLD lanes currently being worked.

## Active COLD lanes

| ROLE | COLD_LANE | CANONICAL_BINDING | BRANCH | BASE_MAIN_SHA | STATUS | PRIMARY FACT | SCOPE |
|---|---|---|---|---|---|---|---|
| R3 | `TS-R3-LATEFX-OWNERSHIP` | `TS-FX-PASS-OWNER` | `cold/r3/latefx-ownership` | `ba231fe57804c3d0a92c18308b9cf0bc1b3e6d3e` | `COLD_ACTIVE / MAIN_DRIFT_ACK_20260908` | close exact native EYE_DONE / late-finalization ownership after `0x0067F4F0`: physical teardown boundary, `+0x78/+0x9C/+0x7C` per-view semantics, FX queue/list lifetime, and whether the one existing natural late tail can remain owned by RIGHT without changing execution counts | COLD_ONLY |
| R4 | `TS-R4-SIDECAR-OWNERSHIP` | `UNBOUND_COLD_LANE` | `cold/r4/sidecar-ownership` | `ba231fe57804c3d0a92c18308b9cf0bc1b3e6d3e` | `COLD_ACTIVE / MAIN_DRIFT_ACK_20260908` | prove immutable packet/resource lifetime and independent L/R execution safety before any replacement/sidecar renderer promotion | COLD_ONLY |

R3 is now explicitly bound to the existing active canonical claim `TS-FX-PASS-OWNER`; this is a narrowing of the same missing-FX ownership problem, not a new duplicate claim. Branch-local conclusions remain COLD until separately promoted at exact scope.

R4 remains unbound and must not absorb R3's native Saber transaction-ownership question.

## R3 current entrypoint
On `cold/r3/latefx-ownership`, read:
`docs/COLD/R3_EYE_DONE_TRANSACTION_SYNC_20260908.md`.

Key governance consequences:
- old `TIMESHIFTVR_OMNI_EXACT_CLOSURE_v6.1.0` is not the current serial gate and must not be run AS-IS;
- `TS-LIVE-005` shadow-cache restoration is a separate local defect from final-color EYE_DONE ownership;
- `DELAY_RIGHT_TEARDOWN_ONLY` is an unexecuted causal candidate, not a PASS/FAIL result;
- R3 remains structural REDTEAM and does not create a competing implementation branch.

## Claim collision law
Before creating a new TimeShiftVR branch, inspect this registry and `CLAIM_GRAPH.json`. Same ROLE + PRIMARY FACT means `REUSE -> ADAPT -> FIX -> EXTEND`, not duplicate research.

Do not infer another role from TAB numbering alone.

## Main drift law
`BASE_MAIN_SHA` pins the accepted world the COLD lane started from.

Before any COLD conclusion is used to authorize LIVE or promotion:
1. compare `BASE_MAIN_SHA..main`;
2. classify changes touching OLD-GOOD v4.7.2, DIP TEX0+TEX1 baseline, native late-FX transaction boundary, exact target identity, canonical binding or sibling renderer ownership;
3. relevant drift means `DRIFT_RECONCILE` before promotion;
4. governance-only/non-overlapping drift may be explicitly ACKed;
5. do not blindly rebase semantic conclusions.

Once a COLD branch has unique commits, do not automatically move its ref to follow main.
