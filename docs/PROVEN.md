# TimeShiftVR — PROVEN

Updated: 2026-08-25

Facts in this file are evidence-backed and should not be re-labeled as hypotheses without contradictory evidence.

## Shader/cache corpus
- 120 retail `.sdc` containers are present in the analyzed corpus.
- 5040 `*_pairs` files are present.
- 5040 factorizes exactly as 8 profiles × 42 scenes × 15 passes.
- Pair files begin with 192 length-prefixed shader-define names.
- 14 of 15 pass categories are common/shared dictionaries.
- `glt` is scene-specific and yields 336 distinct files.
- Observed GLT payload records are exactly 43 bytes.
- `menu` uses a separate shader-set.

## SDC structure
All 120 observed `.sdc` files fit this exact size relation:

`12 + 8*group_count + 12*entry_count + compressed_bulk_total`

This proves a 12-byte leading header plus group/entry tables and compressed bulk sizing. Semantic names for the first three u32 fields remain provisional until decode validation.

## Historical builds
- `beta2`: 2007 SP Demo.
- `beta`: 2007 MP Demo.
- 2006 lineage carries Meqon evidence.
- 2007 lineage carries Havok 4.6 evidence and a newer Saber3D branch.

## Negative evidence with bounded meaning
A raw D3D9-oriented scan did not recover useful shader payload signatures from the SDC bulk. Because the bulk is compressed, this result says nothing decisive about the final renderer API.
