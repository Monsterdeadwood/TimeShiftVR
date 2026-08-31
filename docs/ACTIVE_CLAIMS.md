# TimeShiftVR - ACTIVE COLD LANES REGISTRY

CONTROL_PLANE_ONLY. The filename `docs/ACTIVE_CLAIMS.md` is retained for compatibility, but this file does **not** own canonical claim status.

Canonical `ACTIVE / PENDING / QUEUED / PROVEN / FALSIFIED / SUPERSEDED` status is owned only by `CLAIM_GRAPH.json` together with `RESEARCH_CONTRACT.yaml` and the canonical state. This registry only records isolated COLD branches currently being worked.

## Active COLD lanes

| ROLE | COLD_LANE | CANONICAL_BINDING | BRANCH | BASE_MAIN_SHA | PRIMARY FACT | SCOPE |
|---|---|---|---|---|---|---|
| R3 | `TS-R3-LATEFX-OWNERSHIP` | `UNBOUND_COLD_LANE` | `cold/r3/latefx-ownership` | `ba231fe57804c3d0a92c18308b9cf0bc1b3e6d3e` | determine prepared late-FX queue consumer ownership/mutability and the remaining genuinely per-eye View/receiver/spatial-FX state | COLD_ONLY |
| R4 | `TS-R4-SIDECAR-OWNERSHIP` | `UNBOUND_COLD_LANE` | `cold/r4/sidecar-ownership` | `ba231fe57804c3d0a92c18308b9cf0bc1b3e6d3e` | prove immutable packet/resource lifetime and independent L/R execution safety before any replacement/sidecar renderer promotion | COLD_ONLY |

These COLD lanes do not replace the canonical claim currently marked ACTIVE in `CLAIM_GRAPH.json`. `UNBOUND_COLD_LANE` has no canonical claim-status authority.

## Claim collision law
Before creating a new TimeShiftVR COLD branch, inspect both this registry and `CLAIM_GRAPH.json`. Same ROLE + PRIMARY FACT means REUSE / ADAPT / FIX / EXTEND, not duplicate research. A future canonical binding requires explicit promotion.

## Main drift law
`BASE_MAIN_SHA` pins the accepted world the COLD lane started from.

Before any COLD conclusion is used to authorize LIVE or promotion:
1. compare `BASE_MAIN_SHA..main`;
2. classify changes touching OLD-GOOD v4.7.2, DIP TEX0+TEX1 baseline, late-FX transaction boundary, any future canonical binding or exact target identity;
3. relevant drift means `DRIFT_RECONCILE` before promotion;
4. no blind semantic rebase.

Governance-only/non-overlapping drift may be acknowledged as `MAIN_DRIFT_ACK`.

Once a COLD branch has unique commits, do not automatically move its ref to follow main.
