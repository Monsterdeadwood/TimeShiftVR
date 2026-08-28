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

## Claim / evidence graph discipline
`RESEARCH_CONTRACT.yaml` tells tools and TABs where canonical state lives, which GitHub Issue is CURRENT and which claim IDs are active. `CLAIM_GRAPH.json` is the machine-readable registry of research questions and evidence.

Before changing or creating experiment code:
1. Search `CLAIM_GRAPH.json` for the same question, aliases and fingerprints.
2. Reuse the existing `CLAIM_ID` when the question is materially the same.
3. If no claim fits, add one narrow claim before adding experiment code.
4. Put exactly one claim ID in `experiments/<name>/CLAIM_ID.txt`.
5. Put exactly one class in `experiments/<name>/EXPERIMENT_CLASS.txt`: `COLD`, `PASSIVE_LIVE`, `CAUSAL_LIVE`, or `BUILD_LIVE`.
6. Put exactly one primary fact in `experiments/<name>/PRIMARY_FACT.txt` as `PRIMARY_FACT: <one discriminating fact>`.
7. Every non-`COLD` class additionally requires the exact five-line `PREFLIGHT_5_LINES.txt`.

Do not infer LIVE/COLD from a folder name. `EXPERIMENT_CLASS.txt` is authoritative.

Claim states:
- `ACTIVE` / `PENDING` = current work may target it.
- `QUEUED` / `PARKED` = retained but not the current mutation lane.
- `PROVEN` / `FALSIFIED` / `SUPERSEDED` = closed for ordinary experiment reuse.

Do not silently revive a closed claim. Either create a genuinely different claim or add `REOPEN_RATIONALE.md` containing both:

```text
WHY_REOPEN: <why the previous closed verdict is no longer sufficient>
NEW_EVIDENCE: <the concrete new contradictory evidence>
```

For every added or modified `RESULT_DELTA` / `EVIDENCE_DELTA`, register a unique evidence ID in `CLAIM_GRAPH.json`, link it from the owning claim, then put both headers near the top:

```text
EVIDENCE_ID: <project evidence id>
CLAIM_ID: <owning claim id>
```

## CURRENT Issue synchronization
`RESEARCH_CONTRACT.yaml` declares `current_issue_number`. CI verifies that the configured Issue is open, starts with `CURRENT:`, names the canonical STATE/SYNC path, contains every active `CLAIM_ID`, and is the only open Issue claiming `CURRENT:`.

If CI reports duplicate-claim similarity, reconcile with the existing claim before inventing another experiment. One durable identity per research question, not one identity per package name.
