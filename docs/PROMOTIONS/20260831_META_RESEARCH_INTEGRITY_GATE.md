# META PROMOTION — RESEARCH INTEGRITY GATE — 2026-08-31

CLAIM_ID: `META-RESEARCH-INTEGRITY-GATE`
ROLE: `META`
EVIDENCE_CLASS: `CONTROL_PLANE`
PRIOR_SCOPE: documented process only
NEW_SCOPE: automated advisory CI gate
RUNTIME_CLAIM_CHANGE: NONE
BASELINE_CHANGE: NONE

Adds an advisory CI gate because private-repository rulesets/branch protection are unavailable through the current account/integration path.

- PR into `main` must originate from `promote/*`.
- PR must include `docs/PROMOTIONS/*.md`.
- promotion PR must not wholesale-import `docs/COLD/`.
- pushes to `cold/**` and `live/**` are checked for canonical truth/control-file writes.

Limit: without required branch protection this check is advisory and cannot stop an owner bypass. No runtime/renderer/evidence claim changes.
