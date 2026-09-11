# PROMOTION — Recovery + View/FX v6.3.x synchronization

DATE = 2026-09-12
ROLE = META / R3 evidence reconciliation
CLAIM_ID = `TS-FX-PASS-OWNER`
EVIDENCE_CLASS = EXACT_RETAIL_COLD_RESULT + GOVERNANCE_RECOVERY
TARGET = GOG TimeShift 1.02 x86
TARGET_SHA256 = `78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613`

## Prior scope
Canonical main previously treated
```text
View* -> DAT_00FCACD8 +0x9C(View) -> FX queue/list/membership -> consumer
```
as the active R3 missing edge.

That state predated two returned exact-retail COLD artifacts from 2026-09-10.

## Exact evidence promoted
1. `TIMESHIFTVR_VIEW_FX_OWNER_COLD_RESULT_20260910_032138.zip`
   - SHA256 `3f67af95e23d463084082d6636a82ffa3fa2871a56633ba48be973f4411f3203`
   - exact retail identity PASS
   - COLD only; corpus/baseline unchanged
   - `+0x9C = 0x00681500`
   - recovered direct dataflow reads global RGBA `0x01096544` and display dimensions and emits a four-vertex fullscreen submission
   - no recovered View-derived read in the captured direct dataflow

2. `TIMESHIFTVR_VIEW_FX_OWNER_COLD_V631_RESULT_20260910_040445.zip`
   - SHA256 `a18c0d88604b261285a8cd04856149ebb0d98bdbd50701e0faf9b5515f56e553`
   - exact retail identity retained
   - status `COLD_V631_COLLECTION_COMPLETE__REAL_VIEW_LATE_FX_OWNER_PENDING_REVIEW`
   - recovers ABI/disassembly and broad static harvest for inner dispatch `+0x48..+0x74`, `+0x98`, paired vtables, callgraph, memory references and anchor xrefs
   - ranking is candidate generation only; semantic owner remains unresolved

## PASS / FAIL
PASS:
- exact static evidence falsifies only the `+0x9C = View/FX membership owner` step;
- current claim remains ACTIVE but narrows to the real semantic View-dependent late-FX owner/consumer/lifetime;
- v4.7.2 OLD-GOOD and all executed runtime verdicts remain unchanged.

FAIL / not promoted:
- no claim that any `+0x48..+0x74` candidate is already the owner;
- no rightView clone authorization;
- no EYE_DONE ownership promotion;
- no LIVE authorization;
- no visual/cadence causal verdict derived from static ranking.

## New canonical scope
```text
semantic View* (0x0067F4F0 arg1)
  -> inner dispatch +0x48..+0x74 OR neighboring owner
  -> concrete View-dependent late-FX state/consumer
  -> rain / distortion / light / final composition lifetime
```

`TS-FX-9C-MEMBERSHIP-OWNER` = FALSIFIED / DO_NOT REVIVE without contradictory exact-retail evidence.

## Baseline status
BASELINE = PRESERVED
- v4.7.2 OLD-GOOD true same-frame OpenXR stereo unchanged
- current-best effect state OLD-GOOD + DIP exact TEX0+TEX1 unchanged
- no game execution, injection, DLL staging or corpus mutation was used for this promotion

## Artifact / recovery synchronization
The repository now records exact newest RESULT/source identities and distinguishes `IDENTITY_KNOWN` from actual byte availability. `RECOVERY.md` is the standalone entry point and `docs/RESULT_MANIFEST.md` records byte gaps explicitly.

Exact newest bytes were available in the user artifact library at synchronization time but are not ordinary Git blobs; they remain `EXTERNAL_REQUIRED` until independently backed up by immutable bytes.

## Contradictions resolved
- stale `+0x9C membership owner` canonical direction vs newer exact-retail v6.3.0 evidence: resolved in favor of the newer exact-target RESULT at its exact static scope.
- candidate rankings vs semantic proof: rankings remain noncanonical candidates.
- borrowed late-tail evidence vs R3 ownership: remains BORROWED_EVIDENCE only.

## Canonical files represented by this promotion
The accepted state is reflected in:
- `docs/STATE.md`
- `docs/NEXT.md`
- `CLAIM_GRAPH.json`
- `LATEST_SYNC.md`
- `docs/RESULT_MANIFEST.md`
- `RECOVERY.md`

## Process correction
Several synchronization files reached `main` directly before this promotion record was created. The integrity gate correctly rejected that provenance. This fresh `promote/*` branch is based on the current `main`, fixes the machine claim anchor, records the promotion explicitly, and restores the required promotion path for the current head without rewriting historical evidence.

## STOP RULE
- no `+0x9C = membership owner` revival absent contradictory exact-retail evidence;
- no new generic pass-ranking/OMNI analyzer while v6.3.1 remains unsaturated;
- no LIVE/build/injection/capture follows from this promotion;
- next work is COLD review of the existing v6.3.1 corpus to close `View -> owner -> consumer -> lifetime`.
