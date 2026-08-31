# META Promotion — Research Integrity Gate V2.1

CLAIM_ID: META-RESEARCH-INTEGRITY-GATE-V2-1
ROLE: META
TARGET: repository control plane
EVIDENCE_CLASS: TARGET_STATIC_EXACT
PRIOR_SCOPE: control-plane gate v2
NEW_SCOPE: control-plane gate v2.1

## Accepted delta
Close the time-of-check/time-of-merge drift window.

On every `main` push produced by a promotion merge, the gate now requires:
- the associated PR is merged `promote/* -> main`;
- the PR base SHA equals `github.event.before`, the immediate previous `main`;
- that immediate previous `main` is also the merge-base of the promotion head.

Therefore a promotion that was green before `main` advanced cannot silently become canonical without being reconstructed/rebased and rechecked.

No research claim, baseline, STATE/SYNC/NEXT, runtime result, LIVE authorization, or COLD conclusion is promoted by this record.
