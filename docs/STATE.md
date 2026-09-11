# TimeShiftVR — Canonical State

Updated: 2026-09-12 +03

## Status
**ACTIVE. True same-frame OpenXR stereo remains proven. The previous `View* -> DAT_00FCACD8 +0x9C -> FX membership` model is now FALSIFIED on the exact retail target. R3 remains COLD-only and must identify the real View-dependent late-FX owner/consumer from the inner render-dispatch surface or a neighboring owner.**

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

## Exact R3 render-graph foundation
### `0x0067F4F0` is the proven inner per-view renderer
Exact-target runtime/static evidence establishes:
- synthetic stereo executes `0x0067F4F0` for LEFT and RIGHT;
- its first stack argument is the high-level Saber `View*`;
- current synthetic RIGHT reuses the same high-level `View*` as LEFT even though late D3D9 matrices are made eye-specific;
- native code inside/around the executor repeatedly commits and consumes that `View*`, so a correct RIGHT semantic View cannot be replaced by a one-time late matrix patch alone.

### `DAT_00FCACD8` remains an important owner surface, but `+0x9C` is not the missing membership owner
Recovered structural evidence places `DAT_00FCACD8` on scene/render ownership:
- `+0x8C` = object register/enter path;
- `+0x90` = object unregister/leave path;
- `+0x28/+0x2C` participate in the per-View path;
- MAIN uses a View mask of `1`, native secondary Views use `1 << ViewStackIndex`;
- objects managed through this area carry rain, distortion, shadow-map, mirror and light-related flags.

Native MAIN contains the bracket:
```text
stage10
+0x78()
+0x9C(View)
+0x7C()
```
with recovered vtable base `0x00D8D810` and exact targets:
- `+0x2C -> 0x0067F4F0`;
- `+0x78 -> 0x00680EC0`;
- `+0x7C -> 0x00680EF0`;
- `+0x98 -> 0x00681310`;
- `+0x9C -> 0x00681500`.

## 2026-09-10 exact-retail correction — PROVEN / FALSIFIED
Source RESULT:
- `TIMESHIFTVR_VIEW_FX_OWNER_COLD_RESULT_20260910_032138.zip`
- ZIP SHA256 `3f67af95e23d463084082d6636a82ffa3fa2871a56633ba48be973f4411f3203`
- exact retail proof target SHA256 `78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613`
- Ghidra 12.1.2 / Temurin 21.0.11, exit 0, COLD only, baseline untouched.

Promoted exact facts:
- `+0x9C = 0x00681500`;
- recovered `0x00681500` dataflow reads global RGBA `0x01096544` and display dimensions and builds/submits a four-vertex fullscreen primitive;
- no recovered View-derived read exists in `0x00681500` or its captured direct dataflow.

Therefore:
- **FALSIFIED:** `+0x9C` as the missing `View -> FX queue/list/membership` ownership edge;
- `+0x9C` is retained only as a global fullscreen-overlay candidate unless contradictory exact-retail evidence appears.

## 2026-09-10 v6.3.1 secondary harvest — exact static evidence, semantic verdict still open
Source RESULT:
- `TIMESHIFTVR_VIEW_FX_OWNER_COLD_V631_RESULT_20260910_040445.zip`
- ZIP SHA256 `a18c0d88604b261285a8cd04856149ebb0d98bdbd50701e0faf9b5515f56e553`
- result status: `COLD_V631_COLLECTION_COMPLETE__REAL_VIEW_LATE_FX_OWNER_PENDING_REVIEW`.

Exact harvest added:
- forced entry/ABI recovery for `0x0067F400`, `0x00680EC0`, `0x0067EE40`;
- complete selected ABI/disassembly coverage for inner slots `+0x48..+0x74`;
- `+0x98 = 0x00681310` coverage;
- primary `0x00D8D810` vs sibling `0x00DAA7C8` vtable comparison;
- manager/View/overlay/render-service anchor xrefs;
- 273 focus closure functions, 1191 callgraph rows, 4508 memory-reference rows, 1097 anchor xrefs.

Important negative facts:
- manager-anchored slot-call candidate table contains zero candidates;
- all primary/sibling vtable targets from `+0x28` through the inner `+0x48..+0x74` and through `+0xA0` match at the compared cells except earlier object-identity entries; this comparison does not reveal a unique late-FX owner by itself;
- ranking output is candidate generation only and is **not semantic proof**.

## Current R3 FIRST_MISSING_EDGE
```text
semantic View* (0x0067F4F0 arg1)
  -> inner dispatch +0x48..+0x74 OR neighboring owner
  -> concrete View-dependent late-FX state/consumer
  -> rain / distortion / light / final composition lifetime
```

Primary question:
**Which exact inner-dispatch target or neighboring owner consumes the semantic View and owns the late FX/final work missing from synthetic RIGHT, and what concrete downstream consumer/lifetime makes that work eye-specific or shared?**

Do not replace this with another broad analyzer or LIVE mutation while the existing v6.3.1 corpus can still answer colder sub-edges.

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
- `DAT_00FCACD8 +0x9C` as View-to-FX queue/list/membership owner;
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
- treating EYE_DONE/`680EF0` runtime canary as R3-owned merely because it constrains R3;
- treating collection row counts, address resolution, or ranking score as semantic PASS.

## STILL UNKNOWN
1. Which `+0x48..+0x74` inner pass, neighboring manager path, or downstream owner carries the real View-dependent late-FX state.
2. Exact View-derived dataflow from semantic `View*` into the late consumer.
3. `+0x98 = 0x00681310` semantics and complete writers/readers/lifetime of overlay RGBA `0x01096544`.
4. Exact rain/distortion/light/final consumer and whether its ownership is per-View, per-ViewStack slot, pair-shared, frame-global, or hybrid.
5. Whether any destructive drain/clear/publish point explains LEFT-good / RIGHT-missing behavior.
6. How borrowed EYE_DONE/late-tail evidence constrains that lifetime without being promoted to an R3 runtime verdict.
7. Sustained visual consequence of the separately proven one-shot shadow-cache rearm.

## Current execution status
`COLD = CONTINUE`
`LIVE = DENIED`
`VALID_FRESH_LIVE_TICKET = NONE`

## STOP RULE
- do not revive `+0x9C = membership owner` without new contradictory exact-retail evidence;
- do not run v6.1 AS-IS;
- do not create another generic pass-ranking/OMNI analyzer while the v6.3.1 corpus remains unsaturated;
- do not repeat generic texture/state replay;
- do not duplicate producer-side shadow preparation;
- do not create a rightView LIVE until the actual View-consuming owner/consumer and required lifetime are statically closed;
- do not duplicate the late tail until queue/temporal ownership is classified;
- do not treat `DELAY_RIGHT_TEARDOWN_ONLY` as PASS/FAIL;
- R3 remains structural REDTEAM and hands executable one-mutation tickets to the incumbent implementation owner only after COLD saturation.
