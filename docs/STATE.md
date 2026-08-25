# TimeShiftVR — Canonical State

Updated: 2026-08-25 08:19 +03

## Status
ACTIVE. Renderer/shader decode is closed enough to support exact camera-lineage work. Current authority is the COLD/static camera facade -> backend renderer bridge. No final VR matrix mutation point is authorized yet.

## Frozen target
- Game: GOG TimeShift 1.02 x86.
- Retail SHA256: `78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613`.
- Corpus root: `C:\GOG Games\TimeShift1`.
- Shared tools: `C:\GOG Games\VR Research Tools`.
- CPU-fixed startup donor SHA256: `49bcca23d3d7872fbb578183b77472b64ecd8e3f8d68bfcccb1af6f04d4d8ed6`.

## Closed shader/cache facts
- 120 `.sdc`, 5040 `*_pairs` = 8 profiles × 42 scenes × 15 passes.
- 120/120 SDC containers decode with recovered structure; zlib group streams are validated.
- Totals: 7509 groups, 182995 entries, 7503 decompressed group streams, 365114 shader streams, 181462 unique.
- GLT bytes 0..23 are the 192-bit define mask.
- Runtime shader creation is tied exactly to COLD cache identity by raw CRC + byte length.

## Closed D3D9 / constant path
Retail renderer chain:

`engine producer -> d3dDRIVER cached setter 0x007C3540 -> cache flusher 0x007C3970 -> D3D9 SetVertexShaderConstantF`

- `0x007C3970` is not a camera builder; it flushes dirty cached constants.
- c0-c3 are the active combined ViewProjection/world-to-clip matrix.
- c4 is camera world position.
- Generic mutation at the flusher/setter level is unsafe because multiple camera/render contexts can exist in one frame.

## Closed backend renderer map
Retail RTTI/class evidence:

- `d3dDRIVER::vftable` `0x00DB7A84`.
  - slot 42 / `+0xA8` -> VS constant setter `0x007C3540`.
  - slot 47 / `+0xBC` -> SetVertexShader wrapper `0x007C34C0`.
- `d3dSDR_COMPILER` slot 2 / `+0x08` -> CreateVertexShader wrapper `0x007C5C70`.
- `d3dREND_DRIVER::vftable` `0x00DB7BD4` with RTTI base chain `d3dREND_DRIVER -> vidREND_DRIVER -> rendDRIVER`.
  - slot 13 / `+0x34` -> matrix producer `0x0079E100`.
  - slot 50 / `+0xC8` -> draw path `0x007C75F0`.
  - slot 51 / `+0xCC` -> camera constant upload bridge `0x007C7540`.

## Closed camera source path
Retail upload bridge:

`0x007C7540 -> VSConst(0, this+0x5488, 4) -> c0-c3`

`0x007C7540 -> VSConst(4, this+0xF8, 1) -> c4`

Cross-version homologs preserve the same source offsets/counts:
- SP `0x007B89E0`.
- MP `0x007C1A70`.

Backend matrix-producer homologs also preserve slot 13 and `this+0x5488`:
- retail `0x0079E100`.
- SP `0x00789E40`.
- MP `0x0079E830`.

## Camera facade
A separate anonymous camera/render facade has now been isolated.

Retail constructor-proven object layout:
- object `+0x00` -> primary facade vtable `0x00DBD300`.
- object `+0x10` -> secondary vtable `0x00DBD38C`.
- primary table length by constructor boundary: 35 slots.

Retail primary table:
- slot 13 -> `0x007FB740`, unresolved facade-to-backend bridge.
- slot 14 -> camera-feed `0x007FB790`.
- slot 28 -> camera-dispatch `0x007FBF50`.

Cross-version homologs:
- camera-feed: retail `007FB790`, SP `007F2880`, MP `007FA1E0`.
- camera-dispatch: retail `007FBF50`, SP `007F3040`, MP `007FA9A0`.
- facade slot13: retail `007FB740`, SP `007F2830`, MP `007FA190`.

The dispatcher passes the same `this` into camera-feed. Camera-feed constructs the 64-byte camera block and then calls facade slot13.

## Critical falsification
The facade table is NOT `d3dREND_DRIVER` and is NOT proven as a derived `d3dREND_DRIVER` vtable.

Therefore:

`camera-feed -> [facade vtable + 0x34]`

must not be mislabeled as a direct call to backend `d3dREND_DRIVER::slot13`.

## Current missing fact
Resolve exactly:

`facade slot13 -> one static hop -> backend d3dREND_DRIVER matrix producer`

Active COLD tool:
`TIMESHIFTVR_CAMERA_FACADE_BRIDGE_COLD_v4_0_0`

If that bridge is confirmed across retail + SP + MP, the next target becomes upstream invocation/context ownership of facade dispatcher slot 28.

## Runtime policy
- Keep matrix mutation blocked until gameplay/world context can be separated from menu/scope/shadow/other camera contexts.
- Prefer exact facade/dispatcher context gating over generic shader-constant hooks.
- One missing fact -> one discriminating run.
- COLD before LIVE while COLD remains information-rich.
