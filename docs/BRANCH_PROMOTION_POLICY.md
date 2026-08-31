# TimeShiftVR — BRANCH / PROMOTION POLICY

Updated: 2026-08-31.

This policy prevents COLD R3/R4 research from contaminating accepted OLD-GOOD/runtime truth or R2 replay evidence.

## Branch classes

### `main`
Accepted canon only: governance, exact evidence records, `GLOBAL_LOCKED`, `ROLE_PROVEN`, accepted STATE/SYNC/NEXT and reconciled historical evidence.

### `cold/<role>/<claim>`
Research-only. Active lanes:
- `cold/r3/latefx-ownership`
- `cold/r4/sidecar-ownership`

R2 replay, R3 renderer-graph and R4 sidecar remain separate scopes.

### `live/<role>/<claim>/<run>`
Created only after COLD saturation and the exact five-line LIVE preflight. MUST branch fresh from current `main`, never from COLD. Copy only the bounded experiment delta for one PRIMARY FACT.

### `promote/<role>/<claim>`
Created fresh from current `main` after independently promotable static proof or a valid exact-retail RESULT. Contains only the accepted promotion delta.

## Hard no-wholesale-merge law
- NEVER merge `cold/*` into `main` wholesale.
- NEVER merge `live/*` into `main` wholesale.
- Promotion is reconstructed claim-by-claim on fresh `promote/*`.
- Valid causal FAIL may promote to FALSIFIED when transport and baseline were valid.

## Canonical-file write barrier on COLD
COLD branches must not modify as authoritative truth:
- `docs/PROVEN.md`
- `docs/FALSIFIED.md`
- `docs/STATE.md`
- `docs/SYNC.md`
- `docs/NEXT.md`
- `LATEST_SYNC.md`
- OLD-GOOD v4.7.2 or other protected baseline manifests/global claim state.

Proposed canonical deltas remain under `docs/COLD/` with `SCOPE=COLD_ONLY`.

## Promotion gate
Record `CLAIM_ID`, ROLE, exact target/build, evidence class, prior/new scope, artifact/source identity, PASS/FAIL, baseline status, contradictions resolved and canonical files changed.

Static proof can promote static ABI/layout/shader/pass identity. Queue mutability, eye ownership, cadence, visual effect or causal runtime behavior require exact execution unless strictly static by claim definition.

## Cross-role law
R2/R3/R4 imports are `BORROWED_EVIDENCE` until independently closed in the receiving role.

## Read order
1. `docs/EVIDENCE_BOUNDARY.md`
2. `docs/BRANCH_PROMOTION_POLICY.md`
3. `docs/PORTFOLIO_SYNC_20260831.md`
4. assigned ROLE_LOCK state/evidence
5. exact RESULT/source for the active claim
