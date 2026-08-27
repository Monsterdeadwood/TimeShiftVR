# TimeShiftVR — PROVEN

Updated: 2026-08-27 +03

Facts here are evidence-backed. Keep automatic structural facts separate from user-observed visual verdicts. Donor/source/debug material generates candidates; exact retail evidence decides proof.

For full dated evidence and artifact hashes, see `docs/EVIDENCE_LEDGER_20260827.md` and `docs/RUNTIME_LINEAGE_20260825.md`.

# Frozen retail identity / startup baseline
- Retail target: GOG TimeShift 1.02 x86.
- Retail `TimeShift.exe` SHA256: `78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613`.
- Exact CPU-fixed donor SHA256: `49bcca23d3d7872fbb578183b77472b64ecd8e3f8d68bfcccb1af6f04d4d8ed6`.
- The >8 logical-processor startup failure is real.
- Affinity-only mitigation is insufficient.
- The CPU-fixed donor survives startup and runners can restore retail afterward.

# Frozen shader/cache foundation
- Retail ShaderCache: 120 `.sdc` containers and 5040 `*_pairs` in the original frozen retail set.
- 5040 = 8 profiles × 42 scenes × 15 passes.
- Pair files expose 192 shader-define names.
- GLT bytes 0..23 are a 192-bit define mask.
- LIVE shader creation was previously matched to COLD SDC identity by raw CRC + byte length.

The expanded 2026-08-27 corpus contains 375 SDC files across retail/donor/version material; this does not replace the exact retail count above.

# Runtime gameplay matrix authority
Stable retail callsites:
- `0x007C34C0`: SetVertexShader wrapper.
- `0x007C3540`: cached VS float-constant setter.
- `0x007C3970`: dirty constant-cache flusher to D3D9.
- `0x007C5C70`: CreateVertexShader wrapper.
- `0x007C75F0`: draw path.

Proven semantics:
- `0x007C3970` is a cache flusher, not the gameplay ViewProjection builder.
- c0-c3 are combined world-to-clip / ViewProjection for the active render-camera context.
- c4 is camera world position.
- generic replacement of every c0-c3 write is unsafe because multiple render-camera contexts occur in one frame.

Renderer backend:
- `d3dDRIVER::vftable` `0x00DB7A84`.
- `d3dREND_DRIVER::vftable` `0x00DB7BD4`.
- backend slot13 -> `0x0079E100` matrix producer.
- backend slot50 -> `0x007C75F0` draw path.
- backend slot51 -> `0x007C7540` camera-constant upload bridge.
- `0x007C7540 -> VSConst(0, this+0x5488, 4)` supplies c0-c3.
- `0x007C7540 -> VSConst(4, this+0xF8, 1)` supplies c4.

# Camera facade lineage
- separate anonymous camera/render facade exists and is not backend `d3dREND_DRIVER`.
- primary facade table: `0x00DBD300`.
- secondary table: `0x00DBD38C` at object `+0x10`.
- facade slot13 -> `0x007FB740`.
- camera-feed slot14 -> `0x007FB790`.
- camera-dispatch slot28 -> `0x007FBF50`.

This remains useful evidence but is not the current serial gate.

# Runtime VR evidence

## v4.7.2 — true same-frame OpenXR stereo
Frozen transport baseline:
- 5858 completed same-frame LEFT/RIGHT pairs.
- 41006 / 41006 LEFT/RIGHT uploads.
- 3197 OpenXR frames.
- Quest IPD around 63.63 mm.
- asymmetric per-eye `XrFovf` available.
- same-frame RIGHT re-entry real and repeatable.
- live D3D9 eye images reach the x64 OpenXR host and headset.

User-observed at that stage:
- real binocular stereo/depth existed.
- HMD orientation convention was not finished.
- shadows were absent in duplicated eye rendering.

v4.7.2 remains **KEEP** as transport baseline.

## v5.0 — shadow resource asymmetry
- native shadow texture: 1024×2048 D16.
- native binds observed: 3817.
- LEFT stereo binds: 256.
- RIGHT stereo binds: 0.
- RIGHT shadow-consuming draws still execute.

This proves a resource/state asymmetry, not that one bind copy fixes visible shadows.

## v5.1.1 — executed broad repair, visual rejection
Automatic:
- 3317 same-frame pairs.
- 40242 gameplay view-source writes.
- 537488 RIGHT shadow-state repairs.
- 183 learned shader pairs.
- 23219 / 23219 eye uploads.

User visual:
- camera/tilt badly wrong.
- black wedges.
- eye desynchronization.

Additional raw fact: one sampled shader pair used six distinct stage-1 textures. Therefore last-LEFT-texture-per-shader is not valid texture identity.

## exact-pair structural correspondence
In the first 256 analyzed stereo pairs:
- LEFT DIP count == RIGHT DIP count in 256/256 pairs.
- 26028/26028 sampled LEFT shadow-bound DIP draws had a RIGHT partner at the same ordinal with matching primitive/geometry/VS/PS identity.

Exact draw ordinal + signature is structurally safer than per-shader texture learning.

## v5.2 — exact shadow-bind intervention executed, visible fix failed
- exact depth captures: 1.
- exact LEFT binds under the target pair: 1398.
- same-pair RIGHT mirrored binds: 1398.
- mirror failures: 0.
- completed same-frame pairs: 2172.
- stack failures: 0.
- re-entry failures: 0.
- matrix-contract failures: 0.
- XR-published pairs: 2169.
- XR readback failures: 0.

User still observed fish-eye/crooked/tilted geometry and no restored shadows. Therefore the simple exact D16 bind mirror is not the complete visible shadow fix.

## projection identity defects found after v5.2
Static review proved two contract bugs in that branch:
- host image-only LEFT/RIGHT swap broke physical image/pose/FOV identity.
- row-vector RH off-axis denominator signs were wrong.

Correct coefficients for that convention:
- X `(l+r)/(r-l)`.
- Y `(u+d)/(u-d)`.

The v5.3 package passed 31 static checks. This is retained as historical source correction, not the active 2026-08-27 gate.

# 2026-08-27 runtime effect evidence
The OLD-GOOD line was preserved while texture/state replay was swept in a controlled 10-mode lab.

Current best mode:
- OLD-GOOD + DIP exact TEX0+TEX1.

User-observed bounded negatives:
- DP exact TEX0+TEX1 breaks lighting.
- DP resync +8 TEX0+TEX1 breaks lighting.
- the tested wider DIP+DP/resync/TEX0..3/shadow-state modes did not materially restore the missing effect families.

This proves that another broader replay window is not justified without new semantic pass ownership.

# 2026-08-27 player-frame / View-stack evidence
- renderer View-stack header is `root+0x618`.
- slot0 View is `root+0x620`.
- `0x00956680` is a generic stack push/copy routine with stride `0x364`, copying through `0x004B0DE0`.
- passive hardware evidence caught dynamic mouse-look writing slot0 inside the second `0x004B0DE0` copy; saved outer ESI = `root+0x618`.
- mirrorSys uses the same push at later indices and is excluded from main slot0 ownership.
- `0x00681DD0/0x00681EC7` perform whole-View write/reset before dynamic submit.
- `0x00681DD0` has direct callsite `0x00409D37` inside `0x004098C0`; `0x006595A0` follows at `0x00409D46`.
- `0x004098C0` lacks a recovered ordinary direct caller, supporting pointer/vtable ownership lineage.

Exact non-mirror gameplay/body producer remains unknown; do not over-promote a copy helper to semantic owner.

# 2026-08-27 donor closure
Recovered candidate shader families:
- HUD PS 759149124.
- rain VS 3008662745 / 1294141040.
- blood PS 1730621601.
- death PS 1208193290.
- distortion PS 3000606172.
- low-health PS 2319713783.
- bullet-time VS 2236193038.
- blur/distortion PS 751228937.
- crosshair/bullet-tracer VS 1922619837 / PS 162489781; donor metadata says this family affects lights.
- remove-time-filter VS 2751074104.

Exact retail time AOB anchor: RVA/file `0x3EB3F`, VA `0x0043EB3F`.

# 2026-08-27 ShaderDB / GLT / RTTI evidence
ShaderDB/RTTI closure:
- workers 32/32.
- PAIRS 9180; unique SHA 374; parse success 374/374.
- canonical GLT slots 192; one slot-name schema.
- retail GLT descriptor assignments 109; slot-index agreements 109.
- GLT metadata fields `0x600..0x62C`, stride 4; static xrefs 919.
- RTTI pass-vtable instances 28; method rows 700.
- SDC files 375; unique SHA 198.
- extracted D3D9 blobs 120716.
- exact donor CRC matches 134.
- legacy `shaders.cache` blobs 16623; exact donor CRC matches 0.

Dynamic-light GLT descriptors:
- slot 33 / `0x108`: `SDR_GLT_PARALLAX_SHADOW`.
- slots 41–44: `DYN_LIGHT0..3_DIFFUSE`.
- slots 45–48: `DYN_LIGHT0..3_SPECULAR`.
- slot 49: `DYN_LIGHT0_CUBEMAP_SHADOW`.
- slot 72: `DYN_LIGHT_BRANCH`.

# 2026-08-27 OMNI COLD closure v5
COLD-clean result:
- workers 32.
- corpus files 22102.
- CT fields 5280.
- PAIR files 9180 / unique SHA 374.
- GLT registry rows 436.
- RTTI method rows 900.
- EXEs 9 / AOB rows 18.
- compilation DB xrefs 55.
- SDC files 375 / unique SHA 198.
- SDC D3D9 blobs 203984.
- exact donor CRC matches 134.
- owner-ranking rows 485.
- cross-version homology rows 122.
- S3D files 17.
- TimeSuit rows 6.

Strong static retail candidates:
- `0x003A9652`: STRONG 736 from GLT registry + PAIR-slot agreement + string xrefs.
- `0x003A6DEC`: STRONG 642 from GLT registry + PAIR-slot agreement.
- virtual-method candidate family: `0x003A5F10`, `0x003A5F20`, `0x003A74A0`, `0x003A7FB0` across `d3dPASS_BASE`, `DISTORT`, `FORD`, `GLT`, `IMAGE_FILTER`, `PARTICLES`, `PROJ_SHD`, `RAIN`, `WATER`.

These are **ranked structural candidates only** until registry/init methods are separated from runtime methods that actually invoke D3D9 device work.

# Current exact COLD correction
The v5 result exposed the correct multi-group SDC layout used by v6.1:
- file header totals first;
- per-group compressed size + record count followed immediately by that group's record metadata triplets;
- all compressed group payloads after the interleaved metadata.

`TIMESHIFTVR_OMNI_EXACT_CLOSURE_v6.1.0` is generated to prove exact SDC record/key mapping, GLT 43-byte permutation records and real D3D9-touching `d3dPASS_*` runtime methods. It is **not yet result-proven**.
