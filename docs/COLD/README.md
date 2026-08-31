# TimeShiftVR COLD workspace

Everything under this directory is research-in-progress unless a later promotion record explicitly moves a claim into canonical locked evidence.

Every COLD document must begin with:

```text
PROJECT = TimeShiftVR
ROLE = R1|R2|R3|R4|RESEARCH
CLAIM_ID = <stable id>
TARGET_ID = <exact build/hash/runtime identity>
EVIDENCE_CLASS = TARGET_STATIC_EXACT|PRESERVED_TARGET_SOURCE|DONOR_BETA_HINT|PLAN_SUMMARY_PREPARED
SCOPE = COLD_ONLY
LOCKED_BASELINE = <artifact/commit/result>
CONFLICT_WITH_LOCKED = NONE|<exact conflict>
```

Then keep separate sections:
- `COLD_FACTS` — exact observations only;
- `INFERENCES` — interpretations derived from those observations;
- `CANDIDATES` — ranked but unproven targets;
- `STILL_UNKNOWN`;
- `PROMOTION_TEST` — what exact evidence would permit promotion;
- `STOP_RULE`.

Rules:
- never write `GLOBAL PROVEN` for a COLD-only claim;
- never change OLD-GOOD or another protected runtime baseline from here;
- never erase a conflicting locked fact;
- donor/analogous evidence remains candidate-only until exact retail proof;
- cross-role evidence must be labeled `BORROWED_EVIDENCE`;
- a prepared DLL/BAT/package is not a RESULT;
- promotion into canonical PROVEN/STATE/EVIDENCE happens in a separate explicit promotion commit after the required evidence exists.

See `../EVIDENCE_BOUNDARY.md`.
