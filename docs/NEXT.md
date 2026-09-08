# TimeShiftVR — NEXT

Updated: 2026-09-08 +03

## Current serial gate — EYE_DONE / final-color transaction ownership

Active claim:
`TS-FX-PASS-OWNER`

State:
```text
COLD = CONTINUE
LIVE = DENIED
VALID_FRESH_LIVE_TICKET = NONE
```

The old `TIMESHIFTVR_OMNI_EXACT_CLOSURE_v6.1.0` instruction is superseded as the current gate. Its SDC ideas remain reusable, but the AS-IS analyzer is not an admissible canonical verdict source and must not be run merely because older docs said `awaiting RESULT`.

## Frozen baseline that must hold
- exact GOG TimeShift 1.02 x86 retail target;
- retail SHA256 `78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613`;
- v4.7.2 OLD-GOOD same-frame OpenXR stereo;
- current-best effect state = OLD-GOOD + DIP exact TEX0+TEX1;
- no R3 COLD step launches the game, injects, patches, stages a DLL or mutates the corpus.

## Current model to attack, not assume
The synthetic stereo wrapper executes the exact inner renderer `0x0067F4F0` for LEFT and RIGHT, then releases eye ownership at `RETURN_RIGHT` while Saber continues a natural late view/finalization region.

Preserved execution shows:
```text
RETURN_RIGHT
  -> native 0x00680EF0 view/update
  -> rain / overlays / late FX
  -> Saber SetRenderTarget(real backbuffer)
  -> 425BF981 / 6FDF4543 final
  -> drawing end
```

The final stage remains eye0-only in the preserved v6.13 line because `eye_phase` and `stereo_active` are already cleared before the late tail.

Treat this as a leading ownership model, not an executed repair verdict.

## Highest-value COLD targets

### 1. Exact EYE_DONE boundary
Close the physical instruction/control boundary after `0x0067F4F0` that owns the end of the natural late transaction.

Do not assume `RET 0x00680EF0` is after the final `6FDF`; prove its position relative to rain/overlay/final draws and the enclosing parent continuation.

Required output:
- exact containing function/basic-block boundary;
- exact return/continuation order;
- whether required RIGHT eye state survives to the final backbuffer request;
- no guessed interior jump target.

### 2. Per-view vs shared tail ownership
Use existing exact-retail vtable/CFG evidence:
```text
vtable base 0x00D8D810
+0x2C -> 0x0067F4F0
+0x78 cell 0x00D8D888
+0x9C cell 0x00D8D8AC
+0x7C -> 0x00680EF0
```

Close semantics/lifetime for:
- `+0x78`;
- `+0x9C(View)`;
- `+0x7C / 0x00680EF0`;
- `DAT_00FCACD8` FX queue/list/membership relationships.

The question is ownership, not another broad shader census.

### 3. Queue destructiveness before any tail duplication
Classify downstream `0x007C1780` and adjacent FX containers as:
- immutable/replayable;
- cursor-based but non-destructive;
- destructive drain/clear;
- frame-global/shared temporal owner.

This does **not** block a one-tail owner-transfer canary, but it does block any future `(INNER+TAIL)L -> (INNER+TAIL)R` implementation.

### 4. Keep the shadow-cache defect separate
Retain the exact one-shot `TS-LIVE-005-RIGHT-LIGHT-CACHE-REARM` result as structural evidence that a cache miss can restore the native RIGHT shadow transaction.

Do not use another sustained v6.14.x harness from R3 to answer the final-color ownership question.

## Unexecuted causal discriminator — handoff candidate only
If COLD closes the teardown boundary sufficiently and the incumbent implementation owner issues a fresh ticket, the smallest causal test is conceptually:
```text
KEEP:
  PRE x1
  LEFT inner x1
  RIGHT inner x1
  natural late tail x1
  final x1

CHANGE ONLY:
  keep RIGHT eye ownership alive through the existing natural late finalization
  instead of clearing it at RETURN_RIGHT
```

Mechanical discriminator:
- native real-backbuffer request occurs while RIGHT ownership is still active;
- existing SetRenderTarget hook routes it to private RIGHT RT;
- `425/6FDF` moves from eye0 toward eye2 without increasing tail execution count.

Visual discriminator, only if a valid LIVE is later authorized:
- RIGHT gains missing rain/fullscreen/final composition;
- OLD-GOOD stereo geometry and lighting baseline remain healthy.

This discriminator has **not been executed**. Do not label it PASS/FAIL.

## Explicitly not next
Do not:
- run v6.1 AS-IS;
- create a new OMNI/pass-ranking analyzer;
- repeat same-frame stereo proof;
- repeat broad DIP/DP/TEX/state replay;
- rediscover `0x006EB650 +0x470/+0x474`;
- blindly repeat `0x006E6220`;
- replay `6FDF` manually as the primary repair;
- duplicate `0x0067F100` wholesale;
- duplicate the late tail before queue/temporal ownership is classified;
- create another v6.14.x sustained cache harness from R3;
- start weapon/controller work while this renderer gate remains active.

## Branch-local research entrypoint
Read:
`cold/r3/latefx-ownership:docs/COLD/R3_EYE_DONE_TRANSACTION_SYNC_20260908.md`

Then continue the exact COLD edge already recovered. Do not restart from shader names or v6.1.

## Current STOP RULE
**No new missing-FX LIVE from R3.**

R3 is structural REDTEAM. It must close/falsify ownership assumptions and hand any future executable one-mutation ticket to the existing implementation owner. Before that future LIVE, the mandatory five causal lines must be filled honestly.
