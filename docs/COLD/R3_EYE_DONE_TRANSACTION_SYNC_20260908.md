# TimeShiftVR — R3 EYE_DONE / FINAL-COLOR TRANSACTION CONVERGENCE

PROJECT = TimeShiftVR
ROLE = R3
CLAIM_ID = TS-R3-FINAL-COLOR-TRANSACTION-OWNERSHIP
TARGET_ID = GOG TimeShift 1.02 x86 / SHA256 78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613
EVIDENCE_CLASS = TARGET_STATIC_EXACT
SCOPE = COLD_ONLY
LOCKED_BASELINE = v4.7.2 OLD-GOOD + DIP exact TEX0+TEX1 current-best effects baseline
CONFLICT_WITH_LOCKED = NONE

SYNC_EPOCH = 2026-09-08
ROLE_LOCK = R3 STRUCTURAL REDTEAM
LIVE = DENIED
VALID_FRESH_LIVE_TICKET = NONE

## Why this note exists
The branch-root `README.md`, canonical `docs/STATE.md` and `docs/NEXT.md` still describe `TIMESHIFTVR_OMNI_EXACT_CLOSURE_v6.1.0` as the current awaiting-RESULT gate. Later preserved exact-target analysis and executed RESULT lineage advanced far beyond that state.

Those canonical files are intentionally not rewritten from a COLD branch. This document is the branch-local convergence shadow required by the repository integrity policy.

## COLD_FACTS

### 1. v6.1 AS-IS is not an admissible next action
The preserved v6.1 source audit found material scientific/mechanical defects:
- `RESULT_STATUS=PASS` was unconditional;
- function slicing terminated on raw RET bytes rather than decoded instruction/CFG boundaries;
- direct `FF 90..97` COM-displacement matching could both miss Saber wrapper calls and misclassify unrelated objects;
- ranking was dominated by raw function size/counts rather than semantic runtime ownership;
- the 43-byte GLT record was not semantically recovered beyond the first 24-byte slot mask;
- shader/donor occurrence counts could be mistaken for unique objects;
- exact retail SHA selection was insufficiently guarded;
- output was written inside the source corpus while claiming no source mutation.

Therefore `RUN_V6_1_AS_IS = FALSIFIED`. Reuse its valid SDC parsing pieces only through later corrected decoded-function lineage; do not revive the old OMNI ranking as the current gate.

### 2. Frozen R2 substrate remains the control
Retain:
- v4.7.2 OLD-GOOD true same-frame OpenXR stereo;
- current-best effects state = OLD-GOOD + DIP exact TEX0+TEX1;
- exact synthetic per-eye inner renderer = `0x0067F4F0`;
- same-frame LEFT/RIGHT geometry/projection transport is not the current R3 missing fact.

Do not reopen the same-frame-stereo proof from this R3 lane.

### 3. Shadow/light activation defect is a real but local defect
Exact-retail ownership chain recovered:
```text
0x006E6220
  producer-side shadow/light preparation
  generation advance / builder guard / matrices
        ↓
0x006EB650
  current-generation vs lastApplied cache gate
  state+0x470 / state+0x474
  equality => early return
        ↓
0x006EBB40
  resource activation adjacency
        ↓
0x007C7000
  hardware-visible state application
        ↓
0x007C7470
  physical cleanup
```

The preserved one-shot `TS-LIVE-005-RIGHT-LIGHT-CACHE-REARM` RESULT established, at exact executed scope:
- 64 baseline pairs: LEFT native bind+cleanup, RIGHT no bind+cleanup;
- one forced cache miss on the selected RIGHT pair caused the native RIGHT bind path to execute;
- Saber consumed the miss and naturally restored `lastApplied == generation`;
- LEFT and RIGHT native transaction windows each contained bind -> 102 draws -> cleanup;
- the exact draw multiset matched between eyes.

This proves the cache miss can restore the native RIGHT shadow transaction mechanically. It does **not** prove a sustained visual fix.

The later v6.14.1/v6.14.2/v6.14.3 sustained A/B harnesses did not produce a valid visual A/B verdict because their B phase never armed; their failures were harness/gate defects, not evidence against the cache model.

### 4. `mode360` is not an ownership discriminator
Later exact-retail convergence established:
- `mode360` is an activation-transaction subtype;
- `mode=0` disables the transaction;
- `mode=2` changes the constant-side subtype without changing owner identity;
- `mode=3` belongs to the same observed activation family but its exact subtype semantics remain incomplete;
- `mode360 in {1,2}` as a universal validity/ownership discriminator is FALSIFIED.

Do not build another harness whose scientific gate assumes `{1,2}` is the complete valid owner set.

### 5. `0x0067F4F0 RET` is not native EYE_DONE
BORROWED_EVIDENCE from the exact-retail R2/TAB_B execution lineage, consumed here only as R3 ownership evidence:

Across the preserved v6.13 runtime trace:
- `RIGHT_RETURNS = 10455`;
- `10455 / 10455` RIGHT returns are followed in the same frame by native `0x00680EF0` Menu/view update and later `425BF981 / 6FDF4543` fullscreen final draw;
- in `10454 / 10455` stereo-return frames that final draw is literally the final D3D9 draw of the frame; the formal exception is multi-pair accounting in one frame;
- a representative post-RIGHT tail is exactly `2 rain + 14 overlay/HUD + 1 final fullscreen` draws;
- the native `0x00680EF0` update occurs before those tail draws.

Therefore:
```text
0x0067F4F0 RET = INNER_DONE
not
0x0067F4F0 RET = EYE_DONE
```

### 6. Exact native parent structure places late work after the inner renderer
Exact-retail static reconstruction of `0x0067F100`:
```text
SHARED_PREP
  includes producer-side 0x006E6220
        ↓
INNER_RENDER
  vcall +0x2C = 0x0067F4F0
        ↓
NATURAL POST-INNER REGION
  stage10
  vcall +0x78
  vcall +0x9C(View)
  vcall +0x7C = 0x00680EF0
        ↓
SHARED_POST / FINALIZATION
```

Recovered vtable relations:
- vtable base = `0x00D8D810`;
- `+0x2C` cell `0x00D8D83C -> 0x0067F4F0`;
- `+0x78` cell = `0x00D8D888`;
- `+0x9C` cell = `0x00D8D8AC`;
- `+0x7C` cell `0x00D8D88C -> 0x00680EF0`.

The logical tail block is separated from shared-post by CFG. Exact semantic classification of every tail slot remains incomplete.

### 7. Final-color problem is transaction ownership, not a simple shader branch
The earlier model `09AF vs 6FDF = alternative eye shader branch` is FALSIFIED.

Observed native ordering instead is:
```text
425 / 09AF
  ↓
late work: rain / overlays / distortion / final effects
  ↓
425 / 6FDF
  ↓
final output
```

Stereo v6.13 observes:
- `09AF`: baseline 64 plus LEFT 10455 plus RIGHT 10455;
- `6FDF`: eye0 10519, eye1 0, eye2 0;
- `10519 = 64 + 10455`.

Use ledger term:
`FINAL_COLOR_TRANSACTION_OWNERSHIP_DIVERGENCE`.

Do not return to `003C7975 shader predicate` as primary owner without new contradictory evidence.

### 8. Current wrapper tears RIGHT ownership down before native finalization
Exact current sequence:
```text
RIGHT 0x0067F4F0
  ↓
RETURN_RIGHT
  ↓
wrapper sets:
  eye_phase = 0
  stereo_active = 0
  RT = real backbuffer
  ↓
native 0x00680EF0 / late FX
  ↓
Saber SetRenderTarget(real backbuffer)
  ↓
425 / 6FDF final
```

Immediately before final `6FDF`, the native renderer requests the real backbuffer at caller RVA `0x0039C4F6`.

The existing v6.13 SetRenderTarget hook already implements:
```text
if stereo_active && requested == real_backbuffer:
    eye1 -> private LEFT RT
    eye2 -> private RIGHT RT
```

The private runtime surfaces for that execution are:
- LEFT `0x01502FC0`;
- RIGHT `0x01502A20`;
- BACK `0x01502480`.

Older `0x0FC861A0 / 0x0FC86620` observations are Saber internal surfaces, not the private VR eye surfaces. Consequently `6FDF input is proven LEFT VR eye` is FALSIFIED.

### 9. Old v5.3 RESULT independently records the same missing boundary
Preserved exact runtime artifact:
`TIMESHIFTVR_PROJECTION_IDENTITY_RECOVERY_RESULT_20260826_002808.zip`.

It recorded:
- completed RIGHT returns = 3234;
- exactly 3234 post-RIGHT `425BF981 / 6FDF4543` fullscreen draws;
- those final draws target the real backbuffer rather than the private LEFT/RIGHT RTs;
- `FINAL_BACKBUFFER_BEFORE_SBS.bmp` contains strong rain/final-lighting/fullscreen composition that is absent from `LEFT_EYE.bmp` and `RIGHT_EYE.bmp`.

Thus the late-composition boundary predates the later model and is independently visible in a preserved RESULT.

## INFERENCES

### Leading model
The most economical current R3 model is:
```text
synthetic stereo duplicates the INNER renderer,
but the wrapper drops eye ownership before Saber's native late finalization.
```

This explains simultaneously:
- correct same-frame stereo geometry;
- OLD-GOOD transport stability;
- late `6FDF` remaining eye0-only;
- missing rain/fullscreen composition in private eye images;
- why broad texture/state replay did not repair the image.

### Two orthogonal defects may coexist
Do not collapse them:
```text
DEFECT A: shadow/light activation cache
  -> exact one-shot TS-LIVE-005 structural proof

DEFECT B: eye transaction closes before late finalization
  -> EYE_DONE / final-color transaction ownership
```

A fix for one is not proof for the other.

## CANDIDATES

### C1 — strongest next causal discriminator, NOT YET EXECUTED
`DELAY_RIGHT_TEARDOWN_ONLY`

Keep all execution counts unchanged:
```text
PRE          x1
LEFT INNER   x1
RIGHT INNER  x1
LATE TAIL    x1
MENU         x1
RAIN         x1 transaction
FINAL        x1
POST         x1
```

Change only:
```text
BEFORE: natural late-tail owner = eye0/backbuffer
TEST:   natural late-tail owner = RIGHT
```

Mechanically expected if the model is correct:
- native `SetRenderTarget(real backbuffer)` is intercepted by the existing hook while `eye_phase=RIGHT` and `stereo_active=1`;
- effective target becomes private RIGHT RT;
- `425/6FDF`: eye0 count decreases and eye2 becomes non-zero;
- no duplicate tail, no extra producer work, no extra Present.

This canary has **no preserved executed RESULT**. Do not call it PASS or FAIL.

### C2 — downstream per-eye ownership classification
After a successful C1 only, determine the minimum eye-owned subset among:
- `+0x78`;
- `+0x9C(View)`;
- `+0x7C / 0x00680EF0`;
- associated FX queue/list/membership state.

Do not duplicate the whole tail before proving queue/lifetime semantics. `0x007C1780` remains a specific destructive-vs-reusable queue concern if a future design tries to execute the late tail twice.

## STILL_UNKNOWN
1. Whether keeping RIGHT ownership alive through the natural existing late tail is sufficient to route `6FDF` to the private RIGHT RT without invalidating required state.
2. Exact physical EYE_DONE/teardown point if `0x00680EF0` return precedes the final rain/overlay/6FDF draws.
3. Exact semantics/owners of vtable `+0x78`, `+0x9C(View)`, and their relation to FX queue/list/membership.
4. Whether `0x007C1780` replays an immutable list or destructively drains a queue; this matters only if a future architecture duplicates tail execution.
5. Exact `mode=3` subtype semantics. This no longer blocks the EYE_DONE discriminator.
6. Sustained visual consequence of the proven one-shot shadow cache rearm.
7. LEFT-eye late-tail ownership strategy if a RIGHT-only owner transfer proves the scheduling root.

## PROMOTION_TEST
No R3 COLD fact in this note authorizes a build automatically.

For the EYE_DONE model to move from leading COLD model to an executed causal result, a fresh implementation-owner ticket would have to preserve the existing v6.13/OLD-GOOD lineage and mutate only RIGHT teardown timing. The execution must distinguish mechanical routing from visual recovery and keep all native tail counts unchanged.

R3 itself is REDTEAM: it supplies the exact ownership model and falsification conditions; it does not become a second implementation branch.

## STOP_RULE
- Do not run v6.1 AS-IS.
- Do not create another generic OMNI/pass ranking sweep.
- Do not repeat same-frame stereo proof.
- Do not rediscover `0x006EB650 +0x470/+0x474`.
- Do not blind-call `0x006E6220` twice.
- Do not revive fake native-secondary XR RIGHT.
- Do not build more v6.14.x sustained harness variants from this R3 tab.
- Do not duplicate `0x0067F100` wholesale.
- Do not manually replay `6FDF` as the primary repair.
- Do not duplicate the late tail until queue/temporal ownership is classified.
- Do not create a new LIVE from R3 without a fresh sibling implementation-owner ticket and the mandatory five-line causal gate.

CURRENT_FIRST_MISSING_EDGE = `EYE_DONE ownership: can natural existing late finalization remain owned by RIGHT without changing execution counts?`
NEXT_R3_COLD = attack the exact teardown boundary and per-view/queue ownership assumptions; hand any executable mutation to the incumbent implementation owner.
