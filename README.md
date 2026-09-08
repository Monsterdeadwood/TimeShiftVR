# TimeShiftVR

Native VR integration research for **TimeShift / Saber3D**.

## Current status
**ACTIVE — true same-frame OpenXR stereo is proven; the current renderer gate is exact native EYE_DONE / final-color transaction ownership.**

The project does not need another generic texture replay or another OMNI pass-ranking sweep. The working stereo transport is already real; the remaining high-value question is why Saber's natural late rain/overlay/final-color transaction executes after the synthetic RIGHT inner render has already released eye ownership.

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

Current-best effect state remains:
`OLD-GOOD + DIP exact TEX0+TEX1`.

## Current renderer model
The exact inner renderer is `0x0067F4F0`.

Preserved execution/static evidence now supports:
```text
LEFT inner 0x0067F4F0
RIGHT inner 0x0067F4F0
RETURN_RIGHT
  ↓
native parent continues
  ↓
0x00680EF0 / late view update
  ↓
rain / overlays / late FX
  ↓
425BF981 / 6FDF4543 final
  ↓
output
```

The current wrapper clears `eye_phase` / `stereo_active` at `RETURN_RIGHT`, before that natural finalization. Therefore the current active claim is no longer “which d3dPASS name owns FX?” but the exact semantic boundary and state ownership of the late transaction.

Canonical ledger term:
`FINAL_COLOR_TRANSACTION_OWNERSHIP_DIVERGENCE`.

## Important orthogonal defect
A separate exact-retail shadow/light activation cache exists around `0x006EB650` generation/lastApplied state. A preserved one-shot TS-LIVE-005 causal result mechanically restored the native RIGHT shadow transaction for one selected pair.

That does not prove the late rain/final-color issue is solved. Keep shadow-cache and EYE_DONE defects separate.

## v6.1 disposition
`TIMESHIFTVR_OMNI_EXACT_CLOSURE_v6.1.0` is **not** the current gate and must not be run AS-IS. Later source audit found material verdict/function-boundary/owner-classification defects. Preserve useful SDC parsing ideas only through corrected lineage.

## Current execution status
```text
LIVE = DENIED
VALID_FRESH_LIVE_TICKET = NONE
```

`DELAY_RIGHT_TEARDOWN_ONLY` is an unexecuted causal candidate, not a PASS/FAIL result. R3 remains structural REDTEAM; executable mutation belongs to the incumbent implementation owner after COLD closes the exact teardown/queue boundary.

## Start here
1. `LATEST_SYNC.md`.
2. `docs/STATE.md`.
3. `docs/NEXT.md`.
4. `docs/ACTIVE_CLAIMS.md`.
5. R3 branch: `cold/r3/latefx-ownership:docs/COLD/R3_EYE_DONE_TRANSACTION_SYNC_20260908.md`.
6. `docs/EVIDENCE_BOUNDARY.md` and `docs/BRANCH_PROMOTION_POLICY.md`.

## Working discipline
`REUSE -> ADAPT -> FIX -> EXTEND`

`ONE PRIMARY FACT -> ONE CAUSAL TEST -> ONE VERDICT`

`MAXIMIZE COLD BEFORE LIVE`

`VISUAL HEADSET VERDICT != AUTOMATIC STRUCTURAL PASS`

Do not create another LIVE until a fresh implementation-owner ticket has the mandatory five causal lines and preserves OLD-GOOD.
