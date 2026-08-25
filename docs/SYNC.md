# TimeShiftVR — SYNC

Updated: 2026-08-25

This repository is the persistent canonical state for TimeShiftVR research. Synchronization rule: only carry forward verified facts, bounded negatives, explicit hypotheses, and reproducible next gates.

## 2026-08-25 imported research state

### Corpus / paths
- `C:\GOG Games\TimeShift1`
- shared tools: `C:\GOG Games\VR Research Tools`
- beta2 SP image: `C:\GOG Games\TimeShift1\beta2\Timeshift_SP_Beta.mdf`

### Static analyzer lineage
- v1.0: Python 2 assumption failure.
- v1.0.1: Python 3.8+ fix.
- v1.0.2: trailing-quote path fix.
- v1.0.3: 7-Zip discovery / ZIP fallback.
- v2.0: shader-cache analysis.
- v2.1: SDC decoder stage.

### Canonical imported findings
- 120 `.sdc`.
- 5040 `*_pairs` = 8 profiles × 42 scenes × 15 passes.
- 192 define names at pair-file start.
- 14 shared pass dictionaries; scene-varying `glt` only.
- 336 distinct GLT files; 43-byte GLT payload records.
- separate menu shader-set.
- exact SDC physical-size relation retained in `PROVEN.md`.
- beta2=2007 SP Demo; beta=2007 MP Demo.
- 2006 Meqon vs 2007 Havok 4.6/newer Saber3D lineage split.

## Evidence hygiene
- Compression-obscured string misses are bounded negatives only.
- Historical build labels are not interchangeable with retail identity.
- Never promote an inferred field name into PROVEN solely because its arithmetic fits.
- Generated decodes, Ghidra projects, caches, logs and archives belong in work/result areas, not source game trees.

## Current global gate
`SDC decode closure -> renderer/camera static authority -> one discriminating LIVE probe`
