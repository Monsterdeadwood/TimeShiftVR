# TimeShiftVR — SYNC

Updated: 2026-08-27 +03

This repository is the persistent canonical state for TimeShiftVR research. Carry forward verified facts, bounded negatives, explicit visual verdicts, reproducible next gates and artifact lineage. Do not store copyrighted game binaries here.

## Repository state
- repository: `Monsterdeadwood/TimeShiftVR`.
- branch: `main` only.
- issues: none at synchronization time.
- pull requests: none at synchronization time.
- previous latest commit before this sync: `a599f862d2874e18ff97e80cfc1d61d832ba3094` — `Add TimeShiftVR runtime evidence ledger through v5.3` — 2026-08-25.
- the previous canonical docs were therefore stale relative to the 2026-08-27 local evidence line.

## Frozen corpus / target
- corpus: `C:\GOG Games\TimeShift1`.
- shared tools: `C:\GOG Games\VR Research Tools`.
- retail: GOG TimeShift 1.02 x86.
- retail SHA256: `78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613`.
- CPU-fixed donor SHA256: `49bcca23d3d7872fbb578183b77472b64ecd8e3f8d68bfcccb1af6f04d4d8ed6`.

# Canonical document map
1. `docs/STATE.md` — active PROVEN / FALSIFIED / STILL UNKNOWN / STOP RULE.
2. `docs/PROVEN.md` — evidence-backed facts retained across branches.
3. `docs/FALSIFIED.md` — rejected and saturated approaches; duplicate-research guard.
4. `docs/NEXT.md` — one current serial gate and pass/fail routing.
5. `docs/EVIDENCE_LEDGER_20260827.md` — full Aug-27 closure with exact artifact hashes and candidate ranking.
6. `docs/RUNTIME_LINEAGE_20260825.md` — historical v4.7.2 -> v5.3 runtime ledger; preserved, not rewritten as if current.
7. `README.md` — compact project entry point.

# Frozen historical runtime lineage
The following historical facts remain authoritative and are not to be rediscovered:
- v4.7.2 true same-frame OpenXR transport: 5858 pairs, 41006/41006 uploads, 3197 XR frames.
- v5.0 exact 1024×2048 D16 shadow resource asymmetry.
- v5.1.1 structural execution with visual rejection; broad high-level View mutation and per-shader last-texture replay rejected.
- v5.2 exact 1398 -> 1398 shadow-bind mirror executed with zero failures but did not restore visible shadows.
- v5.3 source audit corrected image/physical-eye identity and row-vector RH off-axis sign errors; retained as historical correction.

# 2026-08-27 runtime lineage
The working line returned to the OLD-GOOD v4.7.2 transport/camera baseline and isolated effect-state behavior instead of continuing broad projection/shadow rewrites.

Key generated/executed sequence:
- `TIMESHIFTVR_STEREO_LIGHT_ISOLATION_v6_10_0`.
- `TIMESHIFTVR_MANUAL_10MODE_VR_LAB_v6_11_x`.
- `TIMESHIFTVR_OLDGOOD_EFFECT_10MODE_v6_12_x`.
- `TIMESHIFTVR_OLDGOOD_EFFECT_RESYNC_10MODE_v6_13_x`.
- `TIMESHIFTVR_OLDGOOD_FX_PASS_BOUNDARY_v6_14_0` generated after the manual verdict.

Bounded visual verdict:
- DP exact and DP resync modes damaged lighting.
- the other tested widening/resync modes did not materially recover missing FX.
- OLD-GOOD + DIP exact TEX0+TEX1 remains the current-best effect-state baseline.

Disposition: **texture-replay widening is saturated; require semantic pass ownership before another LIVE mutation.**

# 2026-08-27 COLD lineage

## Camera / player-frame ownership
- `TIMESHIFTVR_OWNER_SOURCE_FIRE_RESULT_20260827_034120.zip`.
- `TIMESHIFTVR_STACK_LOCAL_CAMERA_OWNER_COLD_RESULT_20260827_040323.zip`.
- `TIMESHIFTVR_VIRTUAL_CAMERA_OWNER_COLD_RESULT_20260827_044735.zip`.
- `TIMESHIFTVR_TRUE_MAIN_PLAYER_FRAME_COLD_RESULT_20260827_135326.zip`.

Main proven renderer state:
- View-stack header `root+0x618`, slot0 `root+0x620`.
- `0x00956680` generic View push/copy, stride `0x364`, via `0x004B0DE0`.
- mirrorSys excluded from main slot0 ownership by index/cadence evidence.
- exact non-mirror gameplay/body producer still open.

## Donor / corpus closure
- `TIMESHIFTVR_DONOR_CLOSURE_RESULT_20260827_052826.zip`.
- `TIMESHIFTVR_MAX_COLD_HARVEST_RESULT_20260827_053816.zip`.

Important donor families include rain, distortion, bullet-time and crosshair/bullet-tracer; donor metadata marks the crosshair/bullet-tracer family as affecting lights. Retail proof remains separate.

## PAIR / SDC / GLT / RTTI closure
- `TIMESHIFTVR_PAIR_SDC_COMPDB_CLOSURE_RESULT_20260827_135123.zip`.
- `TIMESHIFTVR_SHADERDB_RTTI_CLOSURE_RESULT_20260827_141602.zip`.
- `TIMESHIFTVR_OMNI_COLD_CLOSURE_RESULT_20260827_144128.zip`.

Cumulative proven evidence:
- PAIRS 9180 / 374 unique parsed SHA.
- canonical GLT 192-slot schema.
- 109 retail descriptor assignments / 109 slot-index agreements.
- dynamic-light/shadow slots 33, 41–49, 72 mapped.
- expanded SDC corpus 375 files / 198 unique SHA.
- 203984 compiled D3D9 shader blobs in the v5 OMNI closure.
- 134 exact donor CRC matches.
- 900 RTTI method rows and 485 owner-ranking rows.
- strong retail structural candidates `0x003A9652` and `0x003A6DEC` plus d3dPASS virtual-method family around `0x003A5F10`, `0x003A5F20`, `0x003A74A0`, `0x003A7FB0`.

These candidates are not promoted to final runtime semantics until D3D9-touching methods are separated from registry/init code.

# Active gate after synchronization
`TIMESHIFTVR_OMNI_EXACT_CLOSURE_v6.1.0.zip`

Status: **GENERATED / COLD ONLY / awaiting RESULT**.

Package SHA256:
`7bfdb72c5dc71719d7b1cf487be3df35c120798ab1dc345381800fac80aa83dc`

v6.1 reuses and corrects the v5 OMNI line rather than starting a new architecture. It fixes the multi-group SDC metadata model and closes:
- exact compiled shader -> SDC record/key identity;
- donor shader co-residence;
- GLT 43-byte permutation tails;
- actual `d3dPASS_*` virtual methods that directly touch D3D9.

# Evidence policy
- automatic counters prove execution, not visual correctness.
- headset observation is authoritative for visual fusion/lighting/effect quality.
- exact retail proof outranks donor/source labels.
- exact compiled shader identity outranks text proximity.
- RTTI + GLT + callgraph + D3D9 activity intersection outranks any one ranking score.
- do not stack conflicting intrusive D3D9 wrappers.
- one PRIMARY FACT per LIVE experiment; collect broad compatible secondary evidence only when causality remains clean.
- REUSE -> ADAPT -> FIX -> EXTEND before inventing a new analyzer or runtime architecture.

# STOP RULE
No new missing-FX LIVE until v6.1 COLD exact closure is judged. If it yields a bounded pass owner, the next LIVE may test one exact semantic boundary while preserving the OLD-GOOD baseline. If it does not, extend the same COLD line from the failed invariant.
