# TimeShiftVR

Native VR integration research for **TimeShift / Saber3D**.

## Current status
**ACTIVE — true same-frame OpenXR stereo is proven; the current R3 renderer gate is exact per-View scene/FX ownership.**

The project does not need another generic texture replay or another OMNI pass-ranking sweep. The working stereo transport is real. The current R3 question is where Saber turns a high-level `View*` into the FX queue/list/membership consumed by rain, distortion, light and related passes.

## Frozen retail target
- GOG TimeShift 1.02 x86.
- Retail SHA256: `78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613`.
- CPU-fixed startup donor SHA256: `49bcca23d3d7872fbb578183b77472b64ecd8e3f8d68bfcccb1af6f04d4d8ed6`.

## Protected baseline
### v4.7.2 OLD-GOOD true stereo
- 5858 completed same-frame LEFT/RIGHT pairs.
- 41006 / 41006 eye uploads.
- 3197 OpenXR frames.
- physical Quest IPD / asymmetric per-eye FOV.
- real binocular content reaches the headset.

Current-best effect state remains `OLD-GOOD + DIP exact TEX0+TEX1`.

## Current R3 renderer model
The exact inner renderer is `0x0067F4F0`; arg1 is the high-level Saber `View*`. Current synthetic RIGHT reuses the same `View*` as LEFT.

The current owner surface is:
```text
View*
  -> DAT_00FCACD8
     +0x28/+0x2C per-View preparation
     +0x78 -> +0x9C(View) -> +0x7C MAIN bracket
  -> FX queue/list/membership
  -> consumer
```

`DAT_00FCACD8 +0x8C/+0x90` are structurally tied to object registration/unregistration, and the managed object families include rain, distortion, shadow-map, mirror and light-related flags.

### Current FIRST_MISSING_EDGE
```text
View*
  -> DAT_00FCACD8 +0x9C(View)
  -> FX queue/list/membership
  -> consumer
```

Required RIGHT semantic input: `rightView = 0x0067F4F0 arg1`.

## Borrowed late-tail evidence
A separate sibling/runtime line proves that native late rain/overlay/final work continues after the current RIGHT inner return and that the wrapper releases eye ownership too early for final `425/6FDF` in the preserved lineage.

That evidence is retained as a strong constraint, but under the cross-role law it is `BORROWED_EVIDENCE`, not the R3 PRIMARY gate. `DELAY_RIGHT_TEARDOWN_ONLY` remains unexecuted.

## Orthogonal shadow defect
A preserved one-shot TS-LIVE-005 cache miss restored a native RIGHT shadow bind -> 102 draws -> cleanup transaction. That is structural proof of a local activation-lifetime defect, not a sustained visual verdict and not a universal missing-FX explanation.

## v6.1 disposition
`TIMESHIFTVR_OMNI_EXACT_CLOSURE_v6.1.0` is not current NEXT and must not be run AS-IS.

## Current execution status
```text
COLD = CONTINUE
LIVE = DENIED
VALID_FRESH_LIVE_TICKET = NONE
```

## Start here
1. `LATEST_SYNC.md`.
2. `docs/STATE.md`.
3. `docs/NEXT.md`.
4. `docs/ACTIVE_CLAIMS.md`.
5. `docs/EVIDENCE_BOUNDARY.md` and `docs/BRANCH_PROMOTION_POLICY.md`.
6. Exact preserved RESULT/source corpus for the active edge.

## Working discipline
`REUSE -> ADAPT -> FIX -> EXTEND`

`ONE PRIMARY FACT -> ONE CAUSAL TEST -> ONE VERDICT`

`MAXIMIZE COLD BEFORE LIVE`

R3 remains structural REDTEAM. Do not create another LIVE until the exact ownership edge is cold-saturated and the incumbent implementation owner issues a fresh five-line causal ticket.
