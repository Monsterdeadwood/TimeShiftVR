# TimeShiftVR — PROVEN

Updated: 2026-08-25 08:19 +03

Facts in this file are evidence-backed and should not be re-labeled as hypotheses without contradictory evidence.

## Frozen retail identity / startup baseline
- Retail target: GOG TimeShift 1.02 x86.
- Retail `TimeShift.exe` SHA256: `78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613`.
- Exact CPU-fixed donor SHA256: `49bcca23d3d7872fbb578183b77472b64ecd8e3f8d68bfcccb1af6f04d4d8ed6`.
- The >8 logical-processor startup failure is real: retail code uses processor-count / affinity information through fixed-size storage.
- Affinity-only mitigation is insufficient.
- The full CPU-fixed donor survives the startup gate and remains stable with the passive D3D9 proxy.
- Renderer target neighborhoods around the current renderer RVAs are byte-identical between retail and the CPU-fixed donor; the donor is therefore a startup control, not independent renderer lineage.

## Shader/cache corpus
- Retail ShaderCache contains 120 `.sdc` containers and 5040 `*_pairs` files.
- 5040 factorizes exactly as 8 profiles × 42 scenes × 15 passes.
- Pair files expose 192 shader-define names.
- 14/15 pass categories are common/shared dictionaries; `glt` is scene-specific.
- `glt`: 336 distinct files, each with observed 43-byte records.
- `menu` uses a separate shader-set.

## SDC / GLT decode closure
- 120/120 `.sdc` files parse with the recovered structure.
- Corpus totals: 7509 groups, 182995 entries, 7503 zlib-decompressed group streams.
- Decoding yields 365114 shader streams, 181462 unique.
- GLT bytes 0..23 are a 192-bit define mask; this mapping validates across all profiles/scenes tested.

## Shader identity
- Historical iZ3D sight VS: raw CRC `0xCC3E398D`, normal CRC `0x33C1C672`, `vs_2_0`, 508 bytes.
- Modern sight-associated SM3 VS: raw CRC `0x8D672642`, normal CRC `0x7298D9BD`, `vs_3_0`, 392 bytes.
- The modern sight-associated shader exists exactly across all seven SM3 profiles with 12 occurrences each.
- The frozen SM3 base VP family contains exactly 32 vertex shaders consuming c0-c3.
- LIVE runtime shader creation matches COLD SDC identity: 74 runtime `CreateVertexShader` rows, 44 unique raw CRCs, 74/74 matching decoded COLD payloads by raw CRC + length.

## Runtime gameplay matrix authority
- Stable retail runtime callsites:
  - `+0x003C34C0` / `0x007C34C0`: SetVertexShader wrapper.
  - `+0x003C3540` / `0x007C3540`: cached VS float-constant setter.
  - `+0x003C3970` / `0x007C3970`: dirty constant-cache flusher to D3D9.
  - `+0x003C5C70` / `0x007C5C70`: CreateVertexShader wrapper.
  - `+0x003C75F0` / `0x007C75F0`: draw path.
- `0x007C3970` is a cache FLUSHER, not the camera/ViewProjection builder.
- `0x007C3540` is the shadow-cache setter that compares/copies VS float4 constants and marks dirty ranges.
- Runtime target draws show c0-c3 last written through the `0x007C3540 -> 0x007C3970 -> D3D9 SetVertexShaderConstantF` path.
- c0-c3 are a combined world-to-clip / ViewProjection matrix for the active render-camera context.
- c4 is the camera world position. Matrix inversion/recovery from c0-c3 independently matches c4 to very small error.
- Initial projection observed in gameplay corresponds to vertical FOV 56.25°, aspect 4:3, near plane about 0.1. The far-plane estimate remains inference rather than a frozen fact.

## Gameplay shader/context evidence
- Raw CRC `0x416CFC1B` is the best observed gameplay-world gate across the two gameplay captures.
- Raw CRC `0x8D672642` is sight-associated but not ADS-exclusive and appears outside pure ADS gameplay.
- Multiple camera/render contexts can occur within one frame; generic replacement of every c0-c3 write is unsafe.

## Renderer class / vtable map
- Retail RTTI exposes `d3dDRIVER::vftable` at `0x00DB7A84`.
- In `d3dDRIVER`:
  - slot 42 / `+0xA8` -> `0x007C3540`, cached VS float-constant setter.
  - slot 47 / `+0xBC` -> `0x007C34C0`, SetVertexShader wrapper.
- `d3dSDR_COMPILER` slot 2 / `+0x08` -> `0x007C5C70`, CreateVertexShader wrapper.
- Retail backend `d3dREND_DRIVER::vftable` is at `0x00DB7BD4` and RTTI shows the base chain `d3dREND_DRIVER -> vidREND_DRIVER -> rendDRIVER`.
- In retail `d3dREND_DRIVER`:
  - slot 13 / `+0x34` -> `0x0079E100`, matrix producer.
  - slot 50 / `+0xC8` -> `0x007C75F0`, draw path.
  - slot 51 / `+0xCC` -> `0x007C7540`, camera-constant upload bridge.

## Exact c0-c4 source bridge
- Retail `0x007C7540` calls the VS constant setter as:
  - `VSConst(0, this + 0x5488, 4)` -> c0-c3.
  - `VSConst(4, this + 0x00F8, 1)` -> c4.
- Sierra SP homolog: `0x007B89E0` with the same source offsets/counts.
- Sierra MP homolog: `0x007C1A70` with the same source offsets/counts.
- Therefore `d3dREND_DRIVER + 0x5488` is the immediate four-float4 source consumed for c0-c3, and `+0x00F8` is the immediate float4 source consumed for c4.

## Cross-version matrix producer lineage
- Backend matrix-producer homologs:
  - retail `0x0079E100`.
  - Sierra SP `0x00789E40`.
  - Sierra MP `0x0079E830`.
- All three occupy backend slot 13 / `+0x34` and write/copy the 4×4 matrix into `this+0x5488` before the upload bridge.
- The late Sierra setter/flusher lineage is exceptionally strong: retail/SP/MP homologs match in instruction/basic-block/call shape and normalized mnemonic structure.

## Camera facade lineage
- A separate anonymous camera/render facade exists and is NOT the same vtable as backend `d3dREND_DRIVER`.
- Retail constructor lane installs:
  - object `+0x00` -> primary facade table `0x00DBD300`.
  - object `+0x10` -> secondary table `0x00DBD38C`.
- The primary retail facade table has 35 slots when segmented by the constructor-proven boundary.
- Retail facade primary table:
  - slot 14 -> camera-feed `0x007FB790`.
  - slot 28 -> camera-dispatch `0x007FBF50`.
  - slot 13 -> facade bridge candidate `0x007FB740`.
- Cross-version camera-feed homologs: retail `0x007FB790`, SP `0x007F2880`, MP `0x007FA1E0`.
- Cross-version camera-dispatch homologs: retail `0x007FBF50`, SP `0x007F3040`, MP `0x007FA9A0`.
- Dispatcher passes the same ECX/`this` into camera-feed.
- Camera-feed builds the 64-byte camera block and calls its own facade slot 13.

## Bounded negative / falsification already closed
- The anonymous camera facade is not a derived `d3dREND_DRIVER` vtable: slot-by-slot identity is 0 and RTTI does not establish that inheritance relation.
- Therefore camera-feed's `CALL [this->vtable+0x34]` is facade slot 13, not backend `d3dREND_DRIVER::slot13` directly.

## Current unresolved bridge
The remaining COLD fact is narrow:

`camera facade slot13 -> ? -> backend d3dREND_DRIVER matrix producer`

Retail facade slot13: `0x007FB740`.
SP facade slot13: `0x007F2830`.
MP facade slot13: `0x007FA190`.

The active analyzer for this gate is `TIMESHIFTVR_CAMERA_FACADE_BRIDGE_COLD_v4_0_0`.
