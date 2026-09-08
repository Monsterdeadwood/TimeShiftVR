# TimeShiftVR - ACTIVE COLD LANES REGISTRY

CONTROL_PLANE_ONLY. Canonical claim status is owned by `CLAIM_GRAPH.json` together with `RESEARCH_CONTRACT.yaml` and canonical state.

## Active COLD lanes

| ROLE | COLD_LANE | CANONICAL_BINDING | BRANCH | BASE_MAIN_SHA | STATUS | PRIMARY FACT | SCOPE |
|---|---|---|---|---|---|---|---|
| R3 | `TS-R3-FX-MEMBERSHIP-OWNERSHIP` | `TS-FX-PASS-OWNER` | `cold/r3/latefx-ownership` | `ba231fe57804c3d0a92c18308b9cf0bc1b3e6d3e` | `COLD_ACTIVE / MAIN_DRIFT_ACK_20260908` | close exact `View* -> DAT_00FCACD8 +0x9C(View) -> FX queue/list/membership -> consumer`; classify enclosing `+0x78/+0x9C/+0x7C` as shared/per-View/destructive/temporal and use EYE_DONE/680EF0 only as borrowed sibling constraint | COLD_ONLY |
| R4 | `TS-R4-SIDECAR-OWNERSHIP` | `UNBOUND_COLD_LANE` | `cold/r4/sidecar-ownership` | `ba231fe57804c3d0a92c18308b9cf0bc1b3e6d3e` | `COLD_ACTIVE / MAIN_DRIFT_ACK_20260908` | prove immutable packet/resource lifetime and independent L/R execution safety before any replacement/sidecar renderer promotion | COLD_ONLY |

R3 remains bound to the existing active canonical claim `TS-FX-PASS-OWNER`; no duplicate claim is created.

## R3 scope law
PRIMARY R3:
```text
View*
-> DAT_00FCACD8 +0x9C(View)
-> FX queue/list/membership
-> consumer
```

Required RIGHT semantic input is the `View*` passed as `0x0067F4F0 arg1`.

Borrowed, not R3-owned:
- late `EYE_DONE` / final-color transaction evidence;
- `0x00680EF0` rain-queue runtime canary;
- `DELAY_RIGHT_TEARDOWN_ONLY`.

Those facts constrain R3 but stay `BORROWED_EVIDENCE` until independently closed in R3 according to the cross-role law.

## Governance consequences
- v6.1 AS-IS is not current NEXT;
- TS-LIVE-005 one-shot shadow-cache restoration remains orthogonal structural evidence;
- R3 remains structural REDTEAM and does not create a competing implementation branch;
- no new LIVE follows from this registry.

## Claim collision law
Before creating a new TimeShiftVR branch, inspect this registry and `CLAIM_GRAPH.json`. Same ROLE + PRIMARY FACT means `REUSE -> ADAPT -> FIX -> EXTEND`, not duplicate research.

## Main drift law
Before COLD evidence is promoted or used to authorize LIVE, reconcile its `BASE_MAIN_SHA` against current main and classify any drift touching OLD-GOOD, exact target identity, claim binding, View/FX ownership or sibling renderer ownership. Governance-only drift may be ACKed; semantic drift requires reconciliation.
