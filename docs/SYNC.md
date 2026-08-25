# TimeShiftVR — SYNC

Updated: 2026-08-25 08:19 +03

This repository is the persistent canonical state for TimeShiftVR research. Carry forward verified facts, bounded negatives, explicit hypotheses, reproducible next gates, and tool-lineage corrections. Do not store copyrighted game binaries or generated Ghidra caches/results here.

## Corpus / paths
- `C:\GOG Games\TimeShift1`
- shared tools: `C:\GOG Games\VR Research Tools`
- retail target: GOG TimeShift 1.02 x86
- retail SHA256: `78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613`
- CPU-fixed donor SHA256: `49bcca23d3d7872fbb578183b77472b64ecd8e3f8d68bfcccb1af6f04d4d8ed6`

## Historical build map
- `beta2\bin\TimeShift.exe`: 2007 Sierra SP Demo.
- `beta\bin\TimeShift.exe`: 2007 Sierra MP Demo.
- 2006/Atari lineage is older and currently secondary for camera-lineage closure.
- C1/C2 crack aliases were hash-deduplicated during corpus analysis.

## Analyzer / experiment lineage

### Corpus / shader decode
- v1.0: Python 2 assumption failure.
- v1.0.1: Python 3.8+ fix.
- v1.0.2: trailing-quote path fix.
- v1.0.3: 7-Zip discovery / ZIP fallback.
- v2.0: shader-cache analysis.
- v2.1: SDC decoder; recovered group/entry/zlib stream structure.
- v2.2: GLT 192-bit define-mask oracle.
- v2.3: modern sight-associated shader and frozen 32-SM3 VP family.

### Passive D3D9 / gameplay authority
- v3.0.x: passive D3D9 proxy lineage; early build/PowerShell issues corrected.
- v3.0.4: affinity-only baseline falsified.
- v3.0.5: exact full CPU-fixed donor established stable baseline with proxy.
- v3.1.0: gameplay matrix tool had a live-file sharing bug.
- v3.1.1: signal-file fix; two gameplay captures established stable shader/constant callsites and c0-c4 semantics.

### Static renderer owner lineage
- v3.2.0: render-writer slice; Ghidra Java missing.
- v3.2.1: launcher variable/path failure.
- v3.2.2: successful Ghidra slice; `0x007C3970` proven cache flusher and `0x007C3540` cached VS constant setter.
- v3.3.0: state-cache owner oracle.
- v3.3.1: total retail suspect sweep. Useful RTTI/vtable evidence recovered, but generic numeric ranking later bounded as too permissive.
- v3.4.0: broad corpus lineage attempt; superseded.
- v3.4.1: class-aware corpus pass; project-lock collision observed.
- v3.4.2: lock-safe class-aware corpus pass; CPU-fixed donor removed from redundant renderer lineage.

### Exact camera source lineage
- v3.5.0: exact setter slot-load -> indirect CALL dataflow; unique `startRegister=0,count=4` uploader found in retail/SP/MP.
- v3.6.0: camera source owner pass; identified backend `d3dREND_DRIVER`, immediate c0-c4 source offsets and matrix producer family.
- v3.7.0: renderer camera contract pass. Generic `+0x34` cross-build ranking found many false positives; one multi-slot camera-feed group remained strong.
- v3.8.0: exact camera-feed owner pass; isolated one dispatcher per late build and 64-byte camera block construction.
- v3.9.0: TOOL FAIL, Ghidra `SymbolTable.getSymbols(Address)` API mismatch; no verdict.
- v3.9.1: hotfix; RTTI/vtable diff proved facade table is separate from backend `d3dREND_DRIVER` and corrected adjacent-vtable segmentation.
- v4.0.0: active COLD analyzer targeting exact facade slot13 -> backend renderer bridge.

## Canonical architecture now

### Backend constant lane
`engine camera/matrix producer`

`-> d3dREND_DRIVER +0x5488 / +0xF8`

`-> camera constant upload bridge`

`-> d3dDRIVER cached VS setter`

`-> dirty-cache flusher`

`-> D3D9 SetVertexShaderConstantF`

### Retail addresses
- d3dREND matrix producer slot13: `0x0079E100`.
- camera constant upload bridge slot51: `0x007C7540`.
- VS constant setter: `0x007C3540`.
- cache flusher: `0x007C3970`.

### Separate camera facade
- primary vtable: `0x00DBD300`, 35 slots by constructor boundary.
- secondary vtable: `0x00DBD38C`, installed at object `+0x10`.
- facade slot13: `0x007FB740`.
- camera-feed slot14: `0x007FB790`.
- camera-dispatch slot28: `0x007FBF50`.

The facade is not the backend d3dREND_DRIVER vtable.

## Evidence hygiene / stop paths
- Do not treat generic numeric virtual offsets as class identity.
- Do not treat shader creation as gameplay authority.
- Do not treat sight CRC as ADS-exclusive.
- Do not treat a fixed-timer auto-close as an engine crash.
- Do not patch `0x007C3970` as if it were the camera builder.
- Do not mutate all c0-c3 contexts generically.
- See `docs/FALSIFIED.md` for the current closed-path ledger.

## Current global gate

`camera facade slot13 -> backend renderer bridge -> dispatcher upstream context -> one passive LIVE authority test -> per-eye intervention`

Active tool:
`TIMESHIFTVR_CAMERA_FACADE_BRIDGE_COLD_v4_0_0`
