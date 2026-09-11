# TimeShiftVR — Standalone Recovery Entry Point

Updated: 2026-09-12 +03

This file exists for the failure mode where prior ChatGPT conversations, memories and local conversational context are unavailable.

## 0. Rule
Do not reconstruct the project from memory, commit messages or README chronology alone. Restore the canonical state and evidence graph first.

## 1. Read in this order
1. `LATEST_SYNC.md`
2. `docs/STATE.md`
3. `docs/NEXT.md`
4. `CLAIM_GRAPH.json`
5. `docs/ACTIVE_CLAIMS.md`
6. `docs/FALSIFIED.md`
7. `docs/PROVEN.md`
8. `docs/EVIDENCE_BOUNDARY.md`
9. `docs/RESULT_MANIFEST.md`
10. newest relevant `docs/PROMOTIONS/*`, evidence ledger and runtime lineage.

## 2. Frozen identity
- project: TimeShiftVR
- game: GOG TimeShift 1.02 x86
- retail SHA256: `78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613`
- protected runtime baseline: v4.7.2 OLD-GOOD same-frame OpenXR stereo
- current-best effect state: OLD-GOOD + DIP exact TEX0+TEX1

If the target hash differs, stop treating exact-retail offsets/results as directly proven on that target.

## 3. Current canonical frontier
The old `+0x9C = View/FX membership owner` theory is FALSIFIED.

Current R3 edge:
```text
semantic View* (0x0067F4F0 arg1)
  -> inner dispatch +0x48..+0x74 OR neighboring owner
  -> concrete View-dependent late-FX state/consumer
  -> rain / distortion / light / final composition lifetime
```

LIVE is denied until that owner/consumer/lifetime is independently closed.

## 4. Exact newest evidence to recover before acting
- `TIMESHIFTVR_VIEW_FX_OWNER_COLD_RESULT_20260910_032138.zip`
  - SHA256 `3f67af95e23d463084082d6636a82ffa3fa2871a56633ba48be973f4411f3203`
- `TIMESHIFTVR_VIEW_FX_OWNER_COLD_V631_RESULT_20260910_040445.zip`
  - SHA256 `a18c0d88604b261285a8cd04856149ebb0d98bdbd50701e0faf9b5515f56e553`
- source packages and older exact artifacts are listed in `docs/RESULT_MANIFEST.md`.

If exact bytes are unavailable, mark that evidence `IDENTITY_KNOWN / BYTES_MISSING`; do not pretend a prose summary is equivalent to raw evidence.

## 5. Reconstruct STATE before proposing work
Write down:
```text
PROVEN
SUPPORTED
FALSIFIED / DO_NOT_REPEAT
STILL UNKNOWN
LAST GOLDEN
ACTIVE CLAIM
FIRST_MISSING_EDGE
DEPENDENCIES / CONFLICTS
BYTE GAPS
```

Only then choose the next COLD edge.

## 6. Reuse law
```text
REUSE -> ADAPT -> FIX -> EXTEND -> NEW
```

The v6.3.1 result already contains inner-slot ABI/disassembly, callgraph, memory references, anchor xrefs, vtable comparison and decompiles. Saturate those before creating another analyzer.

## 7. LIVE/build gate
Generic continuation does not authorize LIVE/build/injection/capture. Before any such step the owning role must state exactly:
```text
MISSING FACT
WHY NOT COLD
PASS
FAIL
BASELINE MUST HOLD
```

One LIVE tests one PRIMARY FACT. Compatible passive secondary harvest is allowed only if it does not contaminate causality.

## 8. After every RESULT
Update in the same cycle:
- POSTFLIGHT;
- canonical STATE;
- evidence/RESULT manifest with exact filename + SHA256;
- HANDOFF / promotion packet;
- CLAIM_GRAPH status;
- STOP RULE;
- `LATEST_SYNC.md` when the current frontier changes.

A RESULT that exists only in chat is not disaster-recovery complete.

## 9. Hard do-not-repeat anchors
At minimum, do not reopen without contradictory exact-target evidence:
- `+0x9C` as View membership owner;
- broad main-View mutation;
- generic last-LEFT texture replay;
- DP-only or wider generic DIP/DP/TEX/state replay;
- D16 mirror as complete visible-shadow fix;
- whole `0x0067F100 x2`;
- manual `6FDF` as primary repair;
- treating `0x0067F4F0 RET` as EYE_DONE;
- treating ranking/collection volume as semantic proof.

## 10. Recovery completeness status
As of this sync:
- canonical knowledge: strong;
- newest frontier: synchronized through the 2026-09-10 v6.3.1 COLD RESULT;
- exact newest artifact identities: synchronized;
- exact newest artifact bytes: **not stored as normal Git blobs here; external durable backup still required**.

That byte gap is the main remaining obstacle to treating this repository as a completely self-sufficient black-box recorder.
