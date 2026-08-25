# TimeShiftVR

Native VR integration research for **TimeShift / Saber3D**.

## Current status
**ACTIVE — CAMERA FACADE -> BACKEND RENDERER BRIDGE.**

The project has moved beyond generic shader-cache archaeology. The current blocker is now a narrow COLD/static camera-ownership bridge.

Frozen local corpus:
`C:\GOG Games\TimeShift1`

Shared research tools:
`C:\GOG Games\VR Research Tools`

## Frozen retail target
- GOG TimeShift 1.02 x86.
- Retail SHA256: `78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613`.
- CPU-fixed startup donor SHA256: `49bcca23d3d7872fbb578183b77472b64ecd8e3f8d68bfcccb1af6f04d4d8ed6`.

## What is already closed
- 120 `.sdc`, 5040 `*_pairs` = 8 profiles × 42 scenes × 15 passes.
- Full SDC structure/decompression and GLT 192-bit define-mask mapping.
- COLD shader bytecode identity matches LIVE D3D9 shader creation.
- Retail VS constant path:
  `0x007C3540 cached setter -> 0x007C3970 flusher -> D3D9`.
- c0-c3 are combined ViewProjection/world-to-clip for the active render camera.
- c4 is camera world position.
- Backend `d3dREND_DRIVER` is identified by RTTI.
- Backend matrix producer:
  - retail `0x0079E100`.
  - Sierra SP `0x00789E40`.
  - Sierra MP `0x0079E830`.
- Camera constant upload bridge:
  - retail `0x007C7540`.
  - SP `0x007B89E0`.
  - MP `0x007C1A70`.
- Immediate sources:
  - `d3dREND_DRIVER + 0x5488` -> c0-c3.
  - `d3dREND_DRIVER + 0x00F8` -> c4.

## Camera facade isolated
A separate anonymous facade object has its own interface tables.

Retail primary table `0x00DBD300`:
- slot 13 -> `0x007FB740`, current unresolved facade/backend bridge.
- slot 14 -> camera-feed `0x007FB790`.
- slot 28 -> camera-dispatch `0x007FBF50`.

Constructor evidence also installs secondary table `0x00DBD38C` at object `+0x10`.

Cross-version homologs preserve the feed/dispatch/facade-slot13 structure in Sierra SP and MP.

The facade is **not** the backend `d3dREND_DRIVER` vtable and must not be treated as a derived copy without new evidence.

## Current gate

`camera facade slot13 -> ? -> d3dREND_DRIVER matrix producer`

Active analyzer:
`TIMESHIFTVR_CAMERA_FACADE_BRIDGE_COLD_v4_0_0`

If this closes across retail + SP + MP, the next gate is the upstream invocation/context ownership of camera-dispatch slot 28.

## Working discipline
`WORKING BUILD FIRST`

`REVERSE ONLY BLOCKERS`

`ONE MISSING FACT -> ONE TEST -> ONE VERDICT`

`PARALLELIZE EVIDENCE -> SERIALIZE MUTATION`

Do not mutate c0-c4 until gameplay/world camera context is separated from menu/scope/shadow/other renderer cameras.

## Start here
1. `docs/STATE.md` — active canonical state.
2. `docs/PROVEN.md` — facts that must not be rediscovered.
3. `docs/FALSIFIED.md` — closed wrong paths.
4. `docs/NEXT.md` — current serial gate.
5. `docs/SYNC.md` — synchronization ledger / analyzer lineage.
