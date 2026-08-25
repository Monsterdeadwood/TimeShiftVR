# TimeShiftVR — NEXT

Updated: 2026-08-25

## Serial gate 1 — SDC decode closure
1. Validate the first three u32 header fields against every `.sdc` as structural counts/sizes.
2. Recover or identify the compression codec without modifying source corpora.
3. Decompress bulk into a generated work area only.
4. Map entry records to payload ranges and classify compiled shader objects.
5. Cross-check decoded payload counts against the 8 × 42 × 15 cache topology.

Acceptance: deterministic decode on the full 120-file corpus with bounds checks and no unexplained trailing regions.

## Serial gate 2 — renderer/camera authority
Perform narrow static PE/import/string/xref comparison across retail, 2007 SP Demo, 2007 MP Demo, and useful 2006 lineage binaries.

Recover exact evidence for:
- render API creation/present path;
- view/projection construction;
- camera update ownership;
- scene render entry/re-entry points;
- historical debug/reflection/symbol residue.

Acceptance: one or more exact callsites/data structures are strong enough to support a reversible runtime probe.

## Serial gate 3 — first LIVE experiment
Choose one hypothesis only. The first runtime experiment must answer a binary causal question about render/camera authority. No broad injector, no hand/controller work, no comfort layer yet.

## Stop conditions
If an experiment does not discriminate between two hypotheses, redesign it before adding more runtime machinery.
