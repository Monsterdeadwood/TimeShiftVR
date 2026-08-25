# TimeShiftVR — PROVEN

Updated: 2026-08-25 22:54 +03

Facts in this file are evidence-backed. Keep **automatic structural facts** separate from **user-observed visual verdicts**.

## Frozen retail identity / startup baseline
- Retail target: GOG TimeShift 1.02 x86.
- Retail `TimeShift.exe` SHA256: `78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613`.
- Exact CPU-fixed donor SHA256: `49bcca23d3d7872fbb578183b77472b64ecd8e3f8d68bfcccb1af6f04d4d8ed6`.
- The >8 logical-processor startup failure is real.
- Affinity-only mitigation is insufficient.
- The full CPU-fixed donor survives startup and remains stable with the passive D3D9 proxy.
- Current runners can temporarily stage the donor and restore the original retail EXE; v5.2 evidence confirms the retail hash was preserved after the run.

## Shader/cache corpus
- Retail ShaderCache contains 120 `.sdc` containers and 5040 `*_pairs` files.
- 5040 = 8 profiles × 42 scenes × 15 passes.
- Pair files expose 192 shader-define names.
- 120/120 SDC containers parse with the recovered structure.
- Corpus totals: 7509 groups, 182995 entries, 7503 zlib-decompressed group streams.
- Decoding yields 365114 shader streams, 181462 unique.
- GLT bytes 0..23 are a 192-bit define mask.
- LIVE shader creation matches COLD SDC identity by raw CRC + byte length.

## Runtime gameplay matrix authority
Stable retail callsites:
- `0x007C34C0`: SetVertexShader wrapper.
- `0x007C3540`: cached VS float-constant setter.
- `0x007C3970`: dirty constant-cache flusher to D3D9.
- `0x007C5C70`: CreateVertexShader wrapper.
- `0x007C75F0`: draw path.

Proven semantics:
- `0x007C3970` is a cache flusher, not the camera/ViewProjection builder.
- c0-c3 are a combined world-to-clip / ViewProjection matrix for the active render-camera context.
- c4 is camera world position.
- multiple camera/render contexts can occur in one frame, therefore generic replacement of every c0-c3 write is unsafe.

## Renderer class / source lane
Retail RTTI/class evidence:
- `d3dDRIVER::vftable` `0x00DB7A84`.
- `d3dREND_DRIVER::vftable` `0x00DB7BD4`, base chain `d3dREND_DRIVER -> vidREND_DRIVER -> rendDRIVER`.
- backend slot13 / `+0x34` -> matrix producer `0x0079E100`.
- backend slot50 / `+0xC8` -> draw path `0x007C75F0`.
- backend slot51 / `+0xCC` -> camera constant upload bridge `0x007C7540`.

Exact source bridge:
- `0x007C7540 -> VSConst(0, this+0x5488, 4)` -> c0-c3.
- `0x007C7540 -> VSConst(4, this+0xF8, 1)` -> c4.

Cross-version homologs preserve the same lane in Sierra SP and MP.

## Camera facade lineage
- A separate anonymous camera/render facade exists and is not the backend `d3dREND_DRIVER` vtable.
- Retail primary facade table: `0x00DBD300`.
- secondary table: `0x00DBD38C` at object `+0x10`.
- primary facade slot13 -> `0x007FB740`.
- camera-feed slot14 -> `0x007FB790`.
- camera-dispatch slot28 -> `0x007FBF50`.
- cross-version homologs preserve feed/dispatch/facade structure.

This COLD lineage is frozen evidence, but it is no longer the active project blocker because the working runtime line progressed beyond it.

# Runtime VR evidence

## v4.7.2 — true same-frame OpenXR stereo
The v4.7.2 MVP established the current frozen transport baseline.

Automatic evidence:
- **5858** completed same-frame LEFT/RIGHT stereo pairs.
- **41006 / 41006** LEFT/RIGHT eye uploads.
- **3197** OpenXR frames.
- Quest IPD observed around **63.63 mm**.
- asymmetric per-eye `XrFovf` is available.
- same-frame RIGHT re-entry is real and repeatable.
- live D3D9 eye images reach the x64 OpenXR host and headset.

User-observed evidence:
- actual binocular stereo/depth existed.
- HMD orientation convention was not yet correct; yaw/roll behavior was reversed/wrong.
- shadows were absent in the duplicated eye path.

Therefore v4.7.2 is **KEEP as stereo transport baseline**, not as finished visual renderer.

## v4.9 — profiler + corrected row-view line
The later working line retained v4.7.2 stereo and added:
- corrected row-view HMD orientation logic;
- D3D9 resource/pass census;
- controller/OpenXR input census;
- adaptive same-frame stack calibration;
- gameplay-view gating;
- automatic restoration.

## v5.0 — exact shadow-resource asymmetry
Live evidence isolated the native shadow resource:
- texture dimensions: **1024×2048**.
- depth format: **D16**.
- native binds observed: **3817**.
- LEFT stereo binds in the measured corpus: **256**.
- RIGHT stereo binds: **0**.
- shadow-consuming RIGHT draws still execute.

This proves a real LEFT/RIGHT shadow-state asymmetry. It does **not** by itself prove that copying this one bind will restore visible shadows.

## v5.1.0 build failure
The first v5.1.0 delivery had a compile-order error around `write_phase_file`; it produced **no VR verdict**.

The v5.1.1 hotfix corrected the forward declaration only and preserved the intended v5.1 repair logic.

## v5.1.1 executed repair corpus
Result:
`TIMESHIFTVR_XR_TRUE_STEREO_HMD_MVP_v5_1_1_RESULT_20260825_223246.zip`

Automatic facts:
- completed same-frame pairs: **3317**.
- gameplay view-source repair writes: **40242**.
- RIGHT shadow-state repairs: **537488**.
- learned shadow consumer shader pairs: **183**.
- LEFT uploads: **23219**.
- RIGHT uploads: **23219**.
- gameplay-view source latch armed successfully.
- D16 shadow texture identified successfully.
- baseline restoration passed.

User-observed verdict:
- camera/tilt became badly wrong.
- black wedges appeared.
- eyes desynchronized.

Additional corpus fact:
- sampled shadow-consuming shader pairs do not map to one stable stage-1 texture; a single pair was observed using **six different stage-1 textures**.

Therefore:
- the high-level gameplay `view+0x40` repair is too invasive for the final owner strategy;
- the v5.1 per-shader “remember last LEFT texture and replay it in RIGHT” strategy is invalid.

## Exact-pair structural correspondence discovered after v5.1.1
In the first 256 stereo pairs analyzed for the later safe-pair branch:
- LEFT DIP count == RIGHT DIP count in **256 / 256** pairs.
- **26028 / 26028** sampled LEFT shadow-bound DIP draws had an exact RIGHT draw at the same DIP ordinal with matching:
  - primitive data;
  - geometry indices;
  - VS;
  - PS.

This is strong evidence that exact per-draw ordinal matching is a much safer state-replay key than per-shader learning.

## v5.2 causal rollback + exact RIGHT shadow bind
Result:
`TIMESHIFTVR_CAUSAL_ROLLBACK_SHADOW_BIND_RESULT_20260825_221925.zip`

Frozen intervention:
- v5.1 high-level camera mutation removed.
- main-world-only split removed.
- forced Z reflection removed.
- v4.9/v5.0 BODY_PLUS_HMD + ROW_VIEW_CORRECTED behavior restored.
- same-frame stereo retained.
- exact 1024×2048 shadow-depth bind mirrored into RIGHT only after LEFT proved the exact bind in the same pair.

Automatic facts:
- exact depth resource captures: **1**.
- exact LEFT stage-0 binds under VS `C859FB42` / PS `0BCF4693`: **1398**.
- RIGHT same-pair mirrored binds: **1398**.
- mirror failures: **0**.
- completed same-frame pairs: **2172**.
- stack failures: **0**.
- re-entry failures: **0**.
- matrix-contract failures: **0**.
- XR-published pairs: **2169**.
- XR readback failures: **0**.
- active retail EXE preserved and temporary CPU-fix removed.

User-observed verdict:
- fish-eye / crooked camera remained.
- strong tilt remained.
- shadows were still absent.

Therefore the simple exact shadow-depth bind hypothesis is **causally executed but visually falsified as the complete shadow fix**.

## Projection identity defect discovered after v5.2
Static/source review identified two concrete eye/projection contract bugs:
1. host-side LEFT/RIGHT image-payload swap separated game-eye imagery from the native physical `XrView` pose/FOV identity;
2. row-vector RH off-axis projection used the wrong denominator signs.

Correct coefficients for the current convention:
- horizontal offset: `(l+r)/(r-l)`.
- vertical offset: `(u+d)/(u-d)`.

These bugs are sufficient to justify a projection-only recovery run before more shadow mutation.

## v5.3 static preflight
Package:
`TIMESHIFTVR_PROJECTION_IDENTITY_RECOVERY_v5.3.0_30S_ONECLICK.zip`

Static audit result: **31 checks PASS**.

Confirmed by source audit:
- same-frame RIGHT re-entry/return retained.
- pair counter retained.
- LEFT image -> LEFT physical eye identity.
- RIGHT image -> RIGHT physical eye identity.
- old host-side image-only swap absent.
- corrected off-axis denominator signs present.
- old mirrored-sign formulas absent.
- ROW_VIEW_CORRECTED orientation retained.
- BODY_PLUS_HMD camera lock retained.
- main-world-only owner surgery absent.
- forced Z reflection absent.
- active RIGHT shadow texture mirror absent.
- Windows mouse injection tokens absent.
- one-shot final backbuffer capture occurs before SBS overwrite.
- passive post-`RETURN_RIGHT` shadow/final-color telemetry retained.
- 30-second capture default wired.
- no bundled game EXE/DLL.

v5.3 is **statically ready but not yet visually proven**.
