# TimeShiftVR — NEXT

Updated: 2026-09-12 +03

## Current serial gate — R3 real View-dependent late-FX owner
Active claim: `TS-FX-PASS-OWNER`

```text
COLD = CONTINUE
LIVE = DENIED
VALID_FRESH_LIVE_TICKET = NONE
```

The old `TIMESHIFTVR_OMNI_EXACT_CLOSURE_v6.1.0` instruction is superseded. The former `View* -> DAT_00FCACD8 +0x9C -> membership` edge is also superseded and FALSIFIED by exact-retail v6.3.0 evidence.

## Frozen baseline that must hold
- exact GOG TimeShift 1.02 x86 retail target;
- retail SHA256 `78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613`;
- v4.7.2 OLD-GOOD same-frame OpenXR stereo;
- current-best effect state = OLD-GOOD + DIP exact TEX0+TEX1;
- no R3 COLD step launches, injects, patches, stages a DLL or mutates the corpus.

## Corrected exact facts from 2026-09-10
### v6.3.0 RESULT
`TIMESHIFTVR_VIEW_FX_OWNER_COLD_RESULT_20260910_032138.zip`

SHA256:
`3f67af95e23d463084082d6636a82ffa3fa2871a56633ba48be973f4411f3203`

Exact correction:
- `+0x9C = 0x00681500`;
- `0x00681500` reads global RGBA `0x01096544` and display dimensions and emits a four-vertex fullscreen submission;
- no recovered View-derived read exists in the captured `0x00681500` direct dataflow;
- therefore `+0x9C` is **not** the missing View-to-FX queue/list/membership owner.

### v6.3.1 RESULT
`TIMESHIFTVR_VIEW_FX_OWNER_COLD_V631_RESULT_20260910_040445.zip`

SHA256:
`a18c0d88604b261285a8cd04856149ebb0d98bdbd50701e0faf9b5515f56e553`

Result status:
`COLD_V631_COLLECTION_COMPLETE__REAL_VIEW_LATE_FX_OWNER_PENDING_REVIEW`

The run recovered exact ABI/disassembly for the inner dispatch and widened the static evidence surface, but it did not semantically close the owner. `manager-anchored slot-call candidates = 0`; ranking rows remain candidate generation only.

## PRIMARY R3 FIRST_MISSING_EDGE
```text
semantic View* (0x0067F4F0 arg1)
  -> inner dispatch +0x48..+0x74 OR neighboring owner
  -> concrete View-dependent late-FX state/consumer
  -> rain / distortion / light / final composition lifetime
```

Primary binary/structural question:
**Which exact inner-dispatch target or neighboring owner consumes the semantic View and owns the late FX/final work missing from synthetic RIGHT, and what concrete consumer/lifetime makes that work eye-specific or shared?**

## Highest-value COLD work — reuse the existing v6.3.1 corpus first

### 1. Saturate the already-collected inner dispatch
Review together, not one candidate at a time:
```text
+0x48  0x0067FBB0
+0x4C  0x0067FC30
+0x50  0x0067FCB0
+0x54  0x0067FD30
+0x58  0x0067FDB0
+0x5C  0x0067FE60
+0x60  0x00680100
+0x64  0x00680110
+0x68  0x00680230
+0x6C  0x006803F0
+0x70  0x006805D0
+0x74  0x006806B0
```

Use the existing decompiles, raw ABI disassembly, callgraph, memory refs, anchor xrefs and caller windows. A new analyzer is not justified until this material is exhausted.

### 2. Trace semantic View dataflow, not address proximity
Start from the real semantic input at `0x0067F4F0 arg1` and prove one of:
- direct propagation into an inner pass;
- conversion into a View-local owner/record;
- publication into a neighboring manager/global that a late consumer reads.

PASS requires at least two independent static paths converging on the same owner plus a concrete downstream consumer/lifetime. Otherwise remain UNKNOWN.

### 3. Classify `+0x98 = 0x00681310` and overlay state separately
Map writers/readers/lifetime of `0x01096544`. Do not conflate global fullscreen overlay state with the missing per-View owner unless exact dataflow proves the bridge.

### 4. Use paired-vtable evidence as a negative constraint
Primary `0x00D8D810` and sibling `0x00DAA7C8` share the compared inner targets across `+0x28..+0xA0` after early identity entries. Therefore simple primary-vs-sibling slot difference is not the expected owner discriminator in that range.

### 5. Connect the result to concrete late consumers
Search for convergent evidence around rain/distortion/light/final work, including writers/readers, render-service calls, destructive drains/clears and pair-shared publication. Do not promote strings or ranking score alone.

### 6. Keep rightView semantics bounded
Current synthetic RIGHT passes the same high-level `View*` as LEFT. A future correct RIGHT may require a native clone/rebuild, but R3 must first prove the exact owner/consumer lifetime that needs distinct semantic View identity. Do not jump directly to a rightClone LIVE.

### 7. Treat EYE_DONE as BORROWED constraint
Preserved sibling evidence that late rain/overlay/final work occurs after current RIGHT teardown remains important, but it is not the R3 PRIMARY gate. Use it only to constrain the lifetime model.

## Orthogonal shadow-cache line
Retain the one-shot TS-LIVE-005 structural proof. Do not create another sustained cache harness from R3 while the main View/late-FX owner remains open.

## Explicitly not next
Do not:
- revive `+0x9C = membership owner`;
- run v6.1 AS-IS;
- create a new OMNI/pass-ranking analyzer before v6.3.1 static saturation;
- repeat same-frame stereo proof;
- repeat broad DIP/DP/TEX/state replay;
- rediscover `0x006EB650 +0x470/+0x474`;
- blindly repeat `0x006E6220`;
- set native secondary bit for XR RIGHT;
- treat unique View mask as a complete owner;
- duplicate `0x0067F100` wholesale;
- duplicate late tail before ownership/lifetime closure;
- promote sibling `EYE_DONE/680EF0` canary to R3 runtime ownership;
- start weapon/controller work while this renderer gate is active.

## Current STOP RULE
**No new missing-FX LIVE from R3.**

Reuse and saturate `TIMESHIFTVR_VIEW_FX_OWNER_COLD_V631_RESULT_20260910_040445.zip`; close the real `View -> owner -> consumer -> lifetime` edge, falsify competing ownership models, and only then hand an executable one-mutation ticket to the incumbent implementation owner with the mandatory five-line causal gate.
