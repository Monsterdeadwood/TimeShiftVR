# META Promotion — Research Integrity Gate V2

CLAIM_ID: META-RESEARCH-INTEGRITY-GATE-V2
ROLE: META
TARGET: repository control plane
EVIDENCE_CLASS: TARGET_STATIC_EXACT
PRIOR_SCOPE: control-plane gate v1
NEW_SCOPE: control-plane gate v2

## Accepted delta
- require `promote/*` PRs to be based on the exact current `main` base SHA;
- reject merge commits after that base;
- require exactly one promotion record per promotion PR;
- audit every `main` push for association with a merged `promote/* -> main` PR;
- preserve the COLD/LIVE canonical-file write barrier.

No research claim, baseline, STATE, NEXT, runtime result, LIVE authorization, or COLD conclusion is promoted by this record.
