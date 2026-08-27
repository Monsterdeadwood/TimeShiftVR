# TimeShiftVR — NEXT

Updated: 2026-08-27 +03

## Current serial gate — OMNI EXACT CLOSURE v6.1

Canonical package:
`TIMESHIFTVR_OMNI_EXACT_CLOSURE_v6.1.0.zip`

Status: **GENERATED / COLD ONLY / awaiting RESULT**.

The 2026-08-25 v5.3 projection-identity gate is historical. The project has since returned to the OLD-GOOD working stereo line and exhausted the useful simple texture-replay variants. The immediate missing fact is now semantic: **which exact compiled SDC/GLT/d3dPASS runtime lane owns the missing lighting/effect boundary?**

See:
- `docs/STATE.md` for current canonical state.
- `docs/EVIDENCE_LEDGER_20260827.md` for the full 2026-08-27 evidence closure.

# Frozen baseline that must hold
- GOG TimeShift 1.02 x86 target identity remains exact.
- v4.7.2 OLD-GOOD same-frame stereo transport remains the frozen transport baseline.
- current-best effect-state behavior is OLD-GOOD + DIP exact TEX0+TEX1.
- no COLD experiment may launch the game, inject, patch, stage a DLL, or mutate the corpus.

# Why v6.1 exists
The v5 OMNI result corrected a material parser assumption: multi-group SDC metadata is interleaved by group before all zlib payloads.

Correct structural model:
1. `u32 group_count`.
2. `u32 total_record_count`.
3. `u32 total_compressed_bytes`.
4. For every group: `compressed_size`, `record_count`, then that group's per-record `keyA`, `keyB`, `raw_record_size` triplets.
5. All zlib payloads follow in group order.

v6.1 must use that structure to close four linked unknowns without LIVE execution:
- exact compiled D3D9 shader -> SDC record -> `keyA/keyB` identity;
- donor VS/PS co-residence and record identity;
- 43-byte GLT permutation-tail validation and lighting/shadow option census;
- exact `d3dPASS_*` virtual methods with direct `IDirect3DDevice9` COM activity, separated from registry/init methods.

# Exact experiment contract

MISSING FACT: exact SDC group/record map, donor shader co-residence and keys, GLT 43-byte option records, actual `d3dPASS` runtime methods touching D3D9.

WHY NOT COLD: N/A; v5 exposed the required invariants and all required files are local.

PASS: SDC boundaries/decompression/raw splits validate; donor CRCs resolve to exact records; GLT tails validate; pass virtual methods are separated by real D3D9 COM activity.

FAIL: invariants fail broadly or ownership remains indistinguishable.

BASELINE MUST HOLD: no game launch, injection, patch, DLL install, or source mutation.

# What to inspect in the RESULT
Rank the result by **independent evidence intersection**, not by one score alone:
1. exact donor CRC -> compiled shader -> SDC record/key evidence;
2. GLT slot/descriptor/permutation agreement;
3. RTTI class + vtable method identity;
4. direct D3D9 COM call activity from that method;
5. callgraph/xref neighborhood linking runtime pass execution rather than registration only;
6. cross-version homology as supporting evidence, never retail proof by itself.

A candidate is not promoted merely because it has many strings or registry references.

# PASS routing
If v6.1 produces one or a small bounded set of runtime pass owners with independent support:
- freeze all v6.1 exact maps into `PROVEN`;
- choose **one PRIMARY FACT** for the next LIVE test;
- mutate only one exact semantic pass boundary;
- preserve OLD-GOOD stereo/camera and stable lighting;
- collect broad compatible passive secondary harvest: draw ordinal, RT/DS, textures, VS/PS, constants, state transitions, callsite and pass identity.

Before that LIVE, write exactly:
- MISSING FACT
- WHY NOT COLD
- PASS
- FAIL
- BASELINE MUST HOLD

If those five lines cannot be filled honestly, do not build the experiment.

# FAIL routing
If v6.1 cannot validate the corrected SDC layout or cannot distinguish runtime pass methods:
- do not launch a new LIVE sweep;
- inspect the failing invariant and extend the same COLD lineage;
- preserve the v5 OMNI corpus and ranking tables;
- REUSE -> ADAPT -> FIX -> EXTEND the v6.1 analyzer rather than create an unrelated oracle.

# Explicitly not next
Do not:
- repeat v5.1 broad camera/source mutation;
- repeat per-shader last-texture replay;
- repeat the v5.2 one-shadow-bind mirror as the complete fix;
- revive host image-only eye swapping or old projection-sign compensation;
- run DP-only exact/resync effect replay again; it damaged lighting in the visual sweep;
- generate another wider DIP/DP/resync/TEX0..3 texture-state sweep without a newly identified semantic owner;
- start controller/weapon integration while the render-pass missing-FX boundary is unresolved;
- treat donor names, RTTI names, PAIRS proximity, or registry functions as final retail runtime proof without independent intersection.

# Current STOP RULE
**No new missing-FX LIVE until the v6.1 COLD exact closure is judged.**
