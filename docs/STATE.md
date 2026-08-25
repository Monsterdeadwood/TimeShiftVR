# TimeShiftVR — Canonical State

Updated: 2026-08-25

## Status
ACTIVE. Current authority is static corpus archaeology. No runtime VR/stereo claim is accepted yet.

## Local corpus authority
- Corpus root: `C:\GOG Games\TimeShift1`
- Shared tools: `C:\GOG Games\VR Research Tools`
- Known SP beta image: `C:\GOG Games\TimeShift1\beta2\Timeshift_SP_Beta.mdf`

## Closed facts
- Retail shader corpus contains 120 `.sdc` files.
- Companion corpus contains 5040 `*_pairs` files.
- 5040 = 8 profiles × 42 scenes × 15 passes.
- `*_pairs` expose 192 length-prefixed shader define names.
- 14/15 pass categories are shared dictionaries; `glt` is scene-specific.
- `glt`: 336 distinct files; observed payload records are 43 bytes.
- `menu` has a separate shader-set.
- Every `.sdc` tested fits `12 + 8*groups + 12*entries + compressed_bulk_total`.
- Raw payload scans cannot classify the renderer while SDC bulk remains compressed.
- `beta2` is the 2007 SP Demo; `beta` is the 2007 MP Demo.
- 2006 lineage shows Meqon; 2007 lineage shows Havok 4.6 and newer Saber3D.

## Open questions
- Exact compression algorithm and complete SDC entry semantics.
- Exact mapping from SDC entries to compiled vertex/pixel shader payloads.
- Exact retail and beta renderer API/import topology.
- Camera/view/projection ownership and where one stereo pair can be produced in one host frame.
- Whether historical builds contain useful debug/reflection/symbol residue absent from retail.

## Global current gate
Finish SDC decompression and shader payload mapping, then correlate retail/beta executable imports and camera/render callsites. Only after that choose one narrow reversible LIVE experiment.

## Non-authorized shortcuts
- Do not infer D3D9 absence from compressed-SDC string misses.
- Do not declare native stereo/VR support from shader cache naming alone.
- Do not start broad runtime mutation before exact render/camera authority is narrowed.
