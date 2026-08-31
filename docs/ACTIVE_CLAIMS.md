# TimeShiftVR — ACTIVE CLAIMS REGISTRY

CONTROL_PLANE_ONLY. This file records concurrency/branch ownership only. It is not evidence and cannot promote a claim.

## Active COLD lanes

| ROLE | CLAIM_ID | BRANCH | BASE_MAIN_SHA | PRIMARY FACT | SCOPE |
|---|---|---|---|---|---|
| R3 | UNASSIGNED | `cold/r3/latefx-ownership` | `ba231fe57804c3d0a92c18308b9cf0bc1b3e6d3e` | determine prepared late-FX queue consumer ownership/mutability and the remaining genuinely per-eye View/receiver/spatial-FX state | COLD_ONLY |
| R4 | UNASSIGNED | `cold/r4/sidecar-ownership` | `ba231fe57804c3d0a92c18308b9cf0bc1b3e6d3e` | prove immutable packet/resource lifetime and independent L/R execution safety before any replacement/sidecar renderer promotion | COLD_ONLY |

## Claim collision law
Before creating a new TimeShiftVR research branch, search this registry and existing branches. Same ROLE + PRIMARY FACT => REUSE/ADAPT/FIX/EXTEND, not duplicate research.

## Main drift law
`BASE_MAIN_SHA` pins the accepted world the COLD lane started from.

Before any COLD conclusion is used to authorize LIVE or promotion:
1. compare `BASE_MAIN_SHA..main`;
2. classify changes touching OLD-GOOD v4.7.2, DIP TEX0+TEX1 baseline, late-FX transaction boundary, same claim or exact target identity;
3. relevant drift => `DRIFT_RECONCILE` before promotion;
4. no blind semantic rebase.

Governance-only/non-overlapping drift may be acknowledged as `MAIN_DRIFT_ACK`.

Once a COLD branch has unique commits, do not automatically move its ref to follow main.
