# TimeShiftVR — Canonical State

Updated: 2026-08-25 22:54 +03

## Status
ACTIVE. True same-frame OpenXR stereo is proven. The current blocker is **projection / physical-eye identity**, not generic camera-facade discovery.

Canonical next LIVE:
`TIMESHIFTVR_PROJECTION_IDENTITY_RECOVERY_v5.3.0_30S_ONECLICK`

The v5.1 broad camera/shadow repair is rejected. The v5.2 exact shadow bind executed correctly but did not restore visible shadows. v5.3 therefore freezes the stable stereo core and removes the two known eye/projection contract errors before any further lighting mutation.

## Frozen target
- Game: GOG TimeShift 1.02 x86.
- Retail SHA256: `78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613`.
- Corpus root: `C:\GOG Games\TimeShift1`.
- Shared tools: `C:\GOG Games\VR Research Tools`.
- CPU-fixed startup donor SHA256: `49bcca23d3d7872fbb578183b77472b64ecd8e3f8d68bfcccb1af6f04d4d8ed6`.

## Frozen COLD foundation
The old renderer/camera archaeology remains proven, but is no longer the active gate.

### Shader/cache
- 120 `.sdc`, 5040 `*_pairs` = 8 profiles × 42 scenes × 15 passes.
- 120/120 SDC containers decode with recovered structure.
- GLT bytes 0..23 are the 192-bit define mask.
- Runtime shader creation matches COLD payload identity by raw CRC + byte length.

### D3D9 constant lane
Retail:
`engine producer -> 0x007C3540 cached setter -> 0x007C3970 flusher -> D3D9 SetVertexShaderConstantF`

- c0-c3 = active combined ViewProjection/world-to-clip.
- c4 = camera world position.
- `0x007C3970` is a flusher, not a camera builder.
- Backend `d3dREND_DRIVER + 0x5488` is the immediate c0-c3 source; `+0xF8` feeds c4.

### Camera facade
- Anonymous facade primary vtable: `0x00DBD300`.
- facade slot13: `0x007FB740`.
- camera-feed slot14: `0x007FB790`.
- camera-dispatch slot28: `0x007FBF50`.
- The facade is separate from backend `d3dREND_DRIVER`.

This evidence should be retained for owner work, but no longer blocks the working VR build.

## Frozen runtime baseline — v4.7.2
The v4.7.2 true-stereo MVP is the transport baseline that later branches must not regress:
- 5858 completed same-frame LEFT/RIGHT pairs.
- 41006 / 41006 LEFT/RIGHT uploads.
- 3197 OpenXR frames.
- Quest IPD around 63.63 mm.
- asymmetric per-eye OpenXR FOV is available.
- same-frame RIGHT re-entry is real.
- headset receives live binocular content.

User-observed limitations at this stage:
- HMD yaw/roll convention was wrong/reversed.
- shadows were absent in the duplicated eye path.

## v4.9 / v5.0 runtime evidence
The working line retained the v4.7.2 same-frame stereo scheduler and added corrected row-view HMD orientation plus D3D9 pass/resource profiling.

v5.0 isolated a concrete shadow asymmetry:
- exact native shadow texture: 1024×2048 D16.
- native binds observed: 3817.
- LEFT stereo binds: 256.
- RIGHT stereo binds: 0.
- matching RIGHT shadow-consuming draws still occur.

This proves a LEFT/RIGHT resource-state asymmetry, but not that one missing bind alone is the entire visible shadow bug.

## v5.1.1 — structural transport PASS, visual repair FAIL
Executed result:
`TIMESHIFTVR_XR_TRUE_STEREO_HMD_MVP_v5_1_1_RESULT_20260825_223246.zip`

Automatic facts:
- 3317 same-frame pairs.
- 40242 gameplay view-source repair writes.
- 537488 RIGHT shadow-state repair draws.
- 183 learned shadow consumer shader pairs.
- 23219 LEFT uploads / 23219 RIGHT uploads.
- XR transport remained live.
- retail baseline restored correctly after run.

User-observed verdict:
- camera/tilt became very wrong.
- black wedges appeared.
- eyes desynchronized.

Root cause found in corpus:
- the high-level `view+0x40` camera mutation is upstream of broader rendering/culling/lighting ownership and is too invasive.
- the per-shader shadow replay is invalid because a sampled VS/PS pair uses **six different stage-1 textures**; storing only the last LEFT `tex1` and replaying it on unrelated RIGHT occurrences collapses state.

Therefore v5.1 broad repair is **REJECTED**.

## v5.2 causal rollback + exact shadow bind
Executed result:
`TIMESHIFTVR_CAUSAL_ROLLBACK_SHADOW_BIND_RESULT_20260825_221925.zip`

Intervention:
- rollback v5.1 high-level camera mutation.
- rollback main-world-only/Z-reflection surgery.
- retain same-frame stereo.
- mirror only the exact proven shadow-depth resource for the exact consumer pair.

Automatic facts:
- exact 1024×2048 depth texture captures: 1.
- 1398 exact LEFT binds.
- 1398 same-pair RIGHT mirrored binds.
- 0 mirror failures.
- 2172 same-frame pairs.
- 0 stack failures.
- 0 re-entry failures.
- 0 matrix-contract failures.
- 2169 XR-published pairs.
- 0 XR readback failures.
- retail EXE preserved/restored correctly.

User-observed verdict:
- fish-eye / crooked camera remained.
- strong tilt remained.
- shadows still absent.

Conclusion:
**the exact shadow-bind intervention executed, but it did not repair visible shadows.** Do not repeat this simple bind hypothesis.

## Projection contract defect found after v5.2
Two concrete contract errors were identified:
1. host-side LEFT/RIGHT image payload swapping broke physical image/pose/FOV identity;
2. row-vector RH off-axis projection used the wrong denominator signs.

These errors can explain fish-eye/crooked binocular geometry and contaminate visual interpretation of later rendering fixes.

## Current canonical build — v5.3
Package:
`TIMESHIFTVR_PROJECTION_IDENTITY_RECOVERY_v5.3.0_30S_ONECLICK.zip`

Static audit: **31 checks PASS**.

v5.3 contract:
- LEFT game image -> LEFT physical XrView pose/FOV.
- RIGHT game image -> RIGHT physical XrView pose/FOV.
- off-axis X coefficient: `(l+r)/(r-l)`.
- off-axis Y coefficient: `(u+d)/(u-d)`.
- ROW_VIEW_CORRECTED orientation retained.
- BODY_PLUS_HMD camera lock retained.
- no host image-only eye swap.
- no main-world-only owner split.
- no forced Z reflection.
- no active RIGHT shadow texture mutation.
- no Windows mouse injection from HMD.
- real final backbuffer captured once before desktop SBS overwrite.
- passive ranking of draws after `RETURN_RIGHT` for later final-light/final-color ownership.

## Parallel generated branch — HOLD
Package:
`TIMESHIFTVR_SAFE_PAIR_REPAIR_v5_2_0.zip`

This branch fixes the unsafe v5.1 texture-learning strategy using exact LEFT/RIGHT DIP ordinal and draw-signature matching. In the analyzed first 256 pairs:
- LEFT DIP count == RIGHT DIP count for 256/256 pairs.
- 26028 / 26028 sampled LEFT shadow-bound DIP draws had an exact RIGHT draw at the same DIP ordinal with matching primitive data, geometry indices, VS and PS.

This is a useful repair candidate, but it is **not yet canonical** because v5.3 projection identity must be judged first.

## Current missing fact
Does v5.3 restore sane physical-eye geometry and HMD orientation while preserving the v4.7.2 same-frame stereo baseline?

### PASS
- no fish-eye/crooked binocular geometry caused by eye identity/sign errors;
- head yaw/pitch/roll behaves coherently;
- LEFT/RIGHT remain live and distinct;
- stable same-frame stereo and XR submission remain intact.

If shadows remain absent after this PASS, move to the later final-light/final-color boundary after `RETURN_RIGHT` using the passive backbuffer/draw evidence from v5.3.

### FAIL
Do not mutate shadows or camera ownership further. Diagnose the remaining projection/camera convention using the smallest causal test.

## Runtime policy
- v4.7.2 transport is frozen baseline.
- Visual headset evidence is authoritative for visual quality; automatic counters only prove that an intervention executed.
- Do not restore v5.1 broad camera/source mutation.
- Do not restore per-shader last-texture shadow replay.
- Do not repeat the simple v5.2 shadow-depth bind as if it were still an open hypothesis.
- Do not reopen broad reverse engineering while v5.3 can answer the next missing fact directly.
