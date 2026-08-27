# TimeShiftVR

Native VR integration research for **TimeShift / Saber3D**.

## Current status
**ACTIVE — TRUE SAME-FRAME OPENXR STEREO IS PROVEN; THE CURRENT SERIAL GATE IS EXACT COLD SDC / GLT / d3dPASS RUNTIME-OWNER CLOSURE.**

The working transport is no longer the blocker. The project has a real same-frame D3D9 -> x64 OpenXR stereo path, and the current best effect-state line preserves the OLD-GOOD v4.7.2 stereo/camera contract. The remaining rendering problem is missing/unstable lighting and effect families, and the latest evidence says that simply widening texture replay is not the right next move.

Frozen local corpus:
`C:\GOG Games\TimeShift1`

Shared research tools:
`C:\GOG Games\VR Research Tools`

## Frozen retail target
- GOG TimeShift 1.02 x86.
- Retail SHA256: `78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613`.
- CPU-fixed startup donor SHA256: `49bcca23d3d7872fbb578183b77472b64ecd8e3f8d68bfcccb1af6f04d4d8ed6`.

# Frozen VR baseline
## v4.7.2 OLD-GOOD true stereo
- 5858 completed same-frame LEFT/RIGHT pairs.
- 41006 / 41006 eye uploads.
- 3197 OpenXR frames.
- Quest IPD around 63.63 mm.
- asymmetric physical per-eye FOV available.
- same-frame RIGHT re-entry proven.
- real binocular content reaches the headset.

Later effect work must preserve this transport baseline.

# Important rejected runtime paths
- broad v5.1 high-level gameplay View mutation: structural execution, visual reject.
- per-shader last-LEFT-texture shadow replay: invalid resource identity.
- v5.2 one exact 1024×2048 D16 bind mirror: executed exactly, visible shadows still absent.
- host-side image-only eye swap / old projection-sign compensation: rejected by source contract.
- DP-only exact/resync effect replay on the OLD-GOOD baseline: damages lighting.
- wider DIP+DP/resync/TEX0..3/shadow-state replay: no material visual recovery in the controlled sweep.

The project therefore does **not** need another cosmetic texture-replay variant.

# 2026-08-27 COLD breakthrough
The latest closure substantially mapped the semantic render-pass space.

## Player-frame / View-stack lane
- renderer View-stack header `root+0x618`.
- slot0 View `root+0x620`.
- `0x00956680` generic View push/copy, stride `0x364`, through `0x004B0DE0`.
- mirrorSys excluded from main slot0 ownership.
- exact non-mirror gameplay/body source remains open.

## Exact shader / GLT / RTTI evidence
Expanded closure:
- PAIRS 9180 / 374 unique parsed SHA.
- canonical GLT schema: 192 slots.
- 109 retail GLT descriptor assignments with 109 slot-index agreements.
- 375 SDC files / 198 unique SHA in the expanded corpus.
- 203984 compiled D3D9 shader blobs in the v5 OMNI closure.
- 134 exact donor CRC matches.
- 900 RTTI method rows.
- 485 owner-ranking rows.

Dynamic-light/shadow anchors include:
- slot 33 `SDR_GLT_PARALLAX_SHADOW`.
- slots 41–44 `DYN_LIGHT0..3_DIFFUSE`.
- slots 45–48 `DYN_LIGHT0..3_SPECULAR`.
- slot 49 `DYN_LIGHT0_CUBEMAP_SHADOW`.
- slot 72 `DYN_LIGHT_BRANCH`.

Strong retail static candidates include `0x003A9652`, `0x003A6DEC`, and a `d3dPASS_*` virtual-method family around `0x003A5F10`, `0x003A5F20`, `0x003A74A0`, `0x003A7FB0`.

These are still candidates until registry/init methods are separated from methods that actually touch D3D9 at runtime.

# Current canonical gate
`TIMESHIFTVR_OMNI_EXACT_CLOSURE_v6.1.0.zip`

Status: **GENERATED / COLD ONLY / awaiting RESULT**.

v6.1 reuses the v5 OMNI line and fixes the newly recovered multi-group SDC layout. It is designed to close:
- exact compiled shader -> SDC record + `keyA/keyB` identity;
- donor VS/PS co-residence;
- GLT 43-byte permutation records;
- actual `d3dPASS_*` virtual methods with direct `IDirect3DDevice9` COM activity.

Only after that COLD gate identifies a bounded semantic owner should the project return to LIVE mutation.

# Working discipline
`WORKING BUILD FIRST`

`REUSE -> ADAPT -> FIX -> EXTEND`

`ONE PRIMARY FACT -> ONE CAUSAL TEST -> ONE VERDICT`

`MAXIMIZE COLD BEFORE LIVE`

`VISUAL HEADSET VERDICT != AUTOMATIC STRUCTURAL PASS`

# Start here
1. `docs/STATE.md` — active canonical state.
2. `docs/NEXT.md` — current serial gate and pass/fail routing.
3. `docs/PROVEN.md` — facts that must not be rediscovered.
4. `docs/FALSIFIED.md` — rejected/saturated paths and STOP rules.
5. `docs/EVIDENCE_LEDGER_20260827.md` — full Aug-27 evidence ledger with artifact hashes.
6. `docs/SYNC.md` — synchronization and lineage map.
7. `docs/RUNTIME_LINEAGE_20260825.md` — preserved historical v4.7.2 -> v5.3 ledger.
