# Research Workflow

## Canonical loop
`SYNC -> THINK -> KEEP/ADAPT/STOP -> BATCH HARVEST -> CONVERGE -> PROVEN/FALSIFIED -> NEXT GATE -> SYNC`

## Cross-branch state sync
Before any expensive LIVE / capture / TTD / causal experiment, synchronize:
- LATEST RESULT
- PROVEN
- FALSIFIED
- CURRENT FINALISTS
- CONCRETE TARGETS
- CURRENT GATE
- NEXT
- METHOD ALREADY USED

Do not repeat an experiment another branch already closed. Import proven/falsified findings and merge independently convergent evidence.

## Evidence lanes
- **A — COLD/STATIC:** source, PDB, RTTI, disassembly, lineage mapping.
- **B — PASSIVE LIVE/GPU:** API capture, resource/draw/CB observation, logging.
- **C — CAUSAL/PROVENANCE:** TTD, ReClass, one-field mutation, debugger nudge.

Parallelize A/B/alternative hypotheses. Serialize intrusive mutation.

## Mandatory 5-line LIVE preflight
Every new LIVE/build/DLL/patch/probe/capture/injector must state exactly:
1. `MISSING FACT:`
2. `WHY NOT COLD:`
3. `PASS:`
4. `FAIL:`
5. `BASELINE MUST HOLD:`

If these cannot be filled concretely, do not create the experiment.

## Decision rule after every result
- **KEEP PATH:** measurable distance to the current gate decreased.
- **ADAPT PATH:** stronger evidence or a faster/more precise method appeared.
- **STOP PATH:** candidate falsified, question already closed elsewhere, or no longer blocks the build.

## Source-first hard gate
When source/SDK/debug/beta/PDB/RTTI/donor corpus exists:
`CORPUS -> EXHAUSTIVE STATIC HARVEST -> CROSS-VERSION MAP -> RUNTIME CANDIDATES -> TARGETED LIVE`

## Repository truth
- canonical STATE/SYNC path is declared in `RESEARCH_CONTRACT.yaml`;
- evidence-backed facts stay separate from falsified/dead paths;
- prepared package is never a RESULT;
- GitHub is the persistent project truth after convergence.

Chat branches may explore. Repository truth must converge before the next intrusive mutation.
