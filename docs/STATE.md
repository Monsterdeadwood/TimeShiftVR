# TimeShiftVR — Canonical State

Updated: 2026-09-08 +03

## Status
**ACTIVE. True same-frame OpenXR stereo remains proven. The current R3 missing-FX gate is exact per-View scene/FX ownership, not another texture replay, not OMNI v6.1, and not sibling EYE_DONE runtime ownership.**

Canonical active claim: `TS-FX-PASS-OWNER`.

## Frozen target
- Game: GOG TimeShift 1.02 x86.
- Retail SHA256: `78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613`.
- Corpus root: `C:\GOG Games\TimeShift1`.
- CPU-fixed startup donor SHA256: `49bcca23d3d7872fbb578183b77472b64ecd8e3f8d68bfcccb1af6f04d4d8ed6`.

## Protected working baseline
### v4.7.2 OLD-GOOD true stereo
Retain without reopening absent contradictory exact evidence:
- 5858 completed same-frame LEFT/RIGHT pairs;
- 41006 / 41006 eye uploads;
- 3197 OpenXR frames;
- physical Quest IPD / asymmetric per-eye FOV;
- real binocular content reaches the headset.

Current-best effect-state behavior remains `OLD-GOOD + DIP exact TEX0+TEX1`.
Generic DP/wider DIP/DP/TEX/state replay remains saturated or damaging and is not the current research direction.

## v6.1 OMNI disposition
`TIMESHIFTVR_OMNI_EXACT_CLOSURE_v6.1.0` is **not** the next executable/analyzer gate. Later source audit found the AS-IS implementation scientifically unsafe as a canonical verdict source. Preserve corrected SDC/corpus ideas only; do not run or promote v6.1 AS-IS and do not invent another generic OMNI analyzer.

## Exact R3 render-graph convergence
### `0x0067F4F0` is the proven inner per-view renderer
Exact-target runtime/static evidence establishes:
- synthetic stereo executes `0x0067F4F0` for LEFT and RIGHT;
- its first stack argument is the high-level Saber `View*`;
- current synthetic RIGHT reuses the same high-level `View*` as LEFT even though late D3D9 matrices are made eye-specific;
- native code inside/around the executor repeatedly commits and consumes that `View*`, so a correct RIGHT semantic View cannot be replaced by a one-time late matrix patch alone.

### `DAT_00FCACD8` is the current R3 owner surface
Recovered structural evidence places `DAT_00FCACD8` on scene/render-list ownership:
- `+0x8C` = object register/enter path;
- `+0x90` = object unregister/leave path;
- `+0x28/+0x2C` = per-View preparation path;
- MAIN uses a View mask of `1`, native secondary Views use `1 << ViewStackIndex`;
- objects managed through this area carry rain, distortion, shadow-map, mirror and light-related flags.

Native MAIN additionally contains the bracket:
```text
stage10
+0x78()
+0x9C(View)
+0x7C()
```
with recovered vtable base `0x00D8D810`, `+0x2C -> 0x0067F4F0`, `+0x7C -> 0x00680EF0`, and cells `+0x78 = 0x00D8D888`, `+0x9C = 0x00D8D8AC`.

## Current R3 FIRST_MISSING_EDGE
```text
View*
  -> DAT_00FCACD8 +0x9C(View)
  -> FX queue / list / membership
  -> consumer
```

Required RIGHT semantic input:
```text
rightView = 0x0067F4F0 arg1
```

This is the current PRIMARY R3 edge. Exact semantics of `+0x78/+0x9C/+0x7C`, the queue/list structures they own, and the downstream consumer are still UNKNOWN.

## BORROWED sibling evidence — late EYE_DONE / final-color tail
Do not discard this evidence, but do not make it the R3 PRIMARY owner.

Preserved sibling/runtime evidence establishes:
- native parent work continues after `0x0067F4F0`;
- current wrapper clears `eye_phase/stereo_active` before late rain/overlay/final work;
- final `425BF981/6FDF4543` remains eye0-only in preserved v6.13 lineage;
- older captures show strong rain/final composition on the real backbuffer absent from private eye captures;
- `DELAY_RIGHT_TEARDOWN_ONLY` remains unexecuted.

Under the cross-role law this is `BORROWED_EVIDENCE`: a strong constraint on any future R3 ownership model, not proof that R3 owns the EYE_DONE runtime canary.

## Orthogonal shadow/light cache defect
The exact-retail chain `0x006E6220 -> 0x006EB650 -> 0x006EBB40 -> 0x007C7000 -> 0x007C7470` contains a generation/lastApplied cache gate. Preserved one-shot `TS-LIVE-005-RIGHT-LIGHT-CACHE-REARM` mechanically restored a native RIGHT bind -> 102 draws -> cleanup transaction for one selected pair.

This is PROVEN structural evidence of a local activation-lifetime defect. It is not a sustained visual fix and not a universal explanation for rain/final composition.

## FALSIFIED / do not repeat
- broad v5.1 live main-View mutation;
- generic last-LEFT texture replay as the renderer fix;
- D16 mirror as complete visible shadow fix;
- DP-only exact/resync replay;
- wider generic DIP/DP/TEX/state replay without a new owner;
- `09AF vs 6FDF` as a simple shader-choice branch;
- literal native secondary/mirror semantics for XR RIGHT;
- unique View mask alone as a complete FX owner;
- blind repeat of producer-side `0x006E6220`;
- whole `0x0067F100 x2` as first repair;
- manual `6FDF` replay as primary repair;
- treating `0x0067F4F0 RET` as proven EYE_DONE;
- treating EYE_DONE/`680EF0` runtime canary as R3-owned merely because it constrains R3.

## STILL UNKNOWN
1. Exact implementation and side effects of `DAT_00FCACD8 +0x9C(View)`.
2. Whether `+0x78 -> +0x9C(View) -> +0x7C` is MAIN_VIEW_FX_PREP, final queue commit, or mixed shared/per-view work.
3. Exact FX queue/list/membership fields reached from `+0x9C` and their producer/consumer ownership.
4. Whether the membership identity is per-View, per-ViewStack slot, frame-global, or a hybrid.
5. Which rain/distortion/light/final consumers read that state.
6. How borrowed EYE_DONE/late-tail evidence constrains the consumer lifetime without being promoted to an R3 runtime verdict.
7. Sustained visual consequence of the separately proven one-shot shadow-cache rearm.

## Current execution status
`COLD = CONTINUE`
`LIVE = DENIED`
`VALID_FRESH_LIVE_TICKET = NONE`

## STOP RULE
- do not run v6.1 AS-IS;
- do not create another generic pass-ranking analyzer;
- do not repeat generic texture/state replay;
- do not duplicate producer-side shadow preparation;
- do not create a rightView LIVE until the exact native View convention and required membership/queue prep are statically closed;
- do not duplicate the late tail until queue/temporal ownership is classified;
- do not treat `DELAY_RIGHT_TEARDOWN_ONLY` as PASS/FAIL;
- R3 remains structural REDTEAM and hands executable one-mutation tickets to the incumbent implementation owner after COLD saturation.
