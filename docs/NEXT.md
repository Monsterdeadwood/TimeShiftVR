# TimeShiftVR — NEXT

Updated: 2026-09-08 +03

## Current serial gate — R3 scene/FX ownership
Active claim: `TS-FX-PASS-OWNER`

```text
COLD = CONTINUE
LIVE = DENIED
VALID_FRESH_LIVE_TICKET = NONE
```

The old `TIMESHIFTVR_OMNI_EXACT_CLOSURE_v6.1.0` instruction is superseded. Generic replay and pass-ranking are not next.

## Frozen baseline that must hold
- exact GOG TimeShift 1.02 x86 retail target;
- retail SHA256 `78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613`;
- v4.7.2 OLD-GOOD same-frame OpenXR stereo;
- current-best effect state = OLD-GOOD + DIP exact TEX0+TEX1;
- no R3 COLD step launches, injects, patches, stages a DLL or mutates the corpus.

## PRIMARY R3 FIRST_MISSING_EDGE
```text
View*
  -> DAT_00FCACD8 +0x9C(View)
  -> FX queue / list / membership
  -> consumer
```

Required semantic RIGHT input remains:
```text
rightView = 0x0067F4F0 arg1
```

This edge has precedence over sibling EYE_DONE runtime hypotheses for R3 because the later portfolio/master state explicitly separates renderer-graph ownership from R2 runtime/fanout canaries.

## Highest-value COLD targets

### 1. Resolve `DAT_00FCACD8 +0x9C(View)` exactly
Recover the exact function pointer/implementation behind vtable cell `0x00D8D8AC` and map:
- arguments / ABI;
- direct reads/writes;
- called helpers;
- queue/list heads or membership masks touched;
- xrefs to rain/distortion/light/shadow/mirror object classes;
- downstream consumers.

Do not stop at a symbolic name or one candidate xref.

### 2. Classify the enclosing MAIN-only bracket
Exact native sequence:
```text
stage10
+0x78()
+0x9C(View)
+0x7C() = 0x00680EF0
```

Determine which parts are:
- per-View preparation;
- queue build/commit;
- shared frame work;
- destructive drain/clear;
- temporal/history ownership.

### 3. Connect register/unregister ownership to the consumer
Use already-known manager evidence:
```text
+0x8C = object register/enter
+0x90 = object unregister/leave
+0x28/+0x2C = per-View path
```

Trace the same object sets into `+0x9C` and then to concrete render consumers. Rank candidates by independent evidence, not one string or flag.

### 4. Keep rightView semantics bounded
Current synthetic RIGHT passes the same high-level `View*` as LEFT. A future correct RIGHT may require a native clone and rebuild, but R3 must first prove the minimal queue/membership prep that consumes that View. Do not jump directly to a rightClone LIVE.

### 5. Treat EYE_DONE as BORROWED constraint
Preserved sibling evidence that late rain/overlay/final work occurs after current RIGHT teardown is important, but it is not the R3 PRIMARY gate.

Use it to ask:
- does the `+0x9C`-owned state survive until those late consumers?
- is that state built once, per View, or drained once?
- would a rightView/member set be consumed before or during the borrowed late tail?

Do not execute `DELAY_RIGHT_TEARDOWN_ONLY` from R3.

## Orthogonal shadow-cache line
Retain the one-shot TS-LIVE-005 structural proof. Do not create another sustained v6.14.x cache harness from R3.

## Explicitly not next
Do not:
- run v6.1 AS-IS;
- create a new OMNI/pass-ranking analyzer;
- repeat same-frame stereo proof;
- repeat broad DIP/DP/TEX/state replay;
- rediscover `0x006EB650 +0x470/+0x474`;
- blindly repeat `0x006E6220`;
- set native secondary bit for XR RIGHT;
- treat unique View mask as a complete owner;
- duplicate `0x0067F100` wholesale;
- duplicate late tail before queue/temporal ownership closure;
- promote sibling `EYE_DONE/680EF0` canary to R3 runtime ownership;
- start weapon/controller work while this renderer gate is active.

## Current STOP RULE
**No new missing-FX LIVE from R3.**

R3 is structural REDTEAM. Close `View* -> +0x9C -> queue/list/membership -> consumer`, falsify competing ownership models, and hand any executable one-mutation ticket to the incumbent implementation owner only after COLD saturation and the mandatory five-line causal gate.
