# TimeShiftVR

Native VR integration research for **TimeShift / Saber3D lineage**.

## Current status
**ACTIVE — COLD/STATIC CORPUS ARCHAEOLOGY FIRST.**

The repository starts from the verified local corpus at:
`C:\GOG Games\TimeShift1`

Shared research tools:
`C:\GOG Games\VR Research Tools`

Known beta media path:
`C:\GOG Games\TimeShift1\beta2\Timeshift_SP_Beta.mdf`

The immediate engineering job is not to guess a VR hook. It is to finish the renderer/shader container map, identify exact executable/render/camera authority across retail and historical builds, then choose one narrow reversible runtime gate.

## Verified corpus findings
- Retail shader corpus: **120 `.sdc` files**.
- Companion cache corpus: **5040 `*_pairs` files**.
- Exact factorization: **8 shader profiles × 42 scenes × 15 passes = 5040**.
- `*_pairs` begin with **192 length-prefixed shader-define names**.
- **14 of 15 pass categories** behave as shared dictionaries with no scene payload.
- `glt` is scene-specific: **336 distinct GLT files** (= 8 profiles × 42 scenes).
- Observed GLT payload records are **exactly 43 bytes**.
- `menu` uses a separate shader-set.
- All 120 `.sdc` files fit the container-size relation:
  `12 + 8*group_count + 12*entry_count + compressed_bulk_total`.
- The first three `u32` fields are therefore strong structural candidates for `GroupCount`, `EntryCount`, and `CompressedBulkTotal`; naming remains provisional until decoder validation.
- A raw D3D9-oriented scan of `.sdc` bulk produced no useful payload hits because the bulk is compressed; that negative must not be mistaken for proof that the renderer is not D3D9.

## Historical build map
- `beta2` = **2007 SP Demo**.
- `beta` = **2007 MP Demo**.
- 2006 lineage contains **Meqon** physics evidence.
- 2007 lineage contains **Havok 4.6** and a newer Saber3D branch.

## Analyzer lineage retained from the research session
- v1.0 — failed because of Python 2 assumptions.
- v1.0.1 — Python 3.8+ compatibility fix.
- v1.0.2 — fixed trailing-quote path handling.
- v1.0.3 — added 7-Zip discovery / ZIP fallback.
- v2.0 — shader-cache analysis stage.
- v2.1 — SDC decoder stage.

These analyzers are **COLD/STATIC** research tools. The intended discipline is read-only against source corpora; generated caches/results live outside the game trees.

## Current gate
`SDC DECOMPRESSION / SHADER PAYLOAD MAP -> RETAIL+BETA PE/IMPORT/CAMERA MAP -> ONE NARROW LIVE RENDER GATE`

Do not claim native stereo/VR support, a final render API, or a camera hook until directly evidenced.

## Start here
1. `docs/STATE.md` — active canonical state
2. `docs/PROVEN.md` — facts that must not be rediscovered
3. `docs/NEXT.md` — current serial gate
4. `docs/SYNC.md` — provenance and synchronization notes

## Working model
`SYNC -> STATIC HARVEST -> PROVEN/FALSIFIED -> CONVERGE -> ONE REVERSIBLE LIVE GATE -> SYNC`

**PARALLELIZE EVIDENCE — SERIALIZE MUTATION.**
