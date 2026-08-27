# TimeShiftVR — FALSIFIED / STOP PATHS

Updated: 2026-08-27 +03

These paths were tested, structurally disproven, visually rejected, or bounded strongly enough that repeating them without new evidence would be duplicate research.

# Startup / baseline
- Affinity-only CPU8 mitigation is not sufficient for stable startup.
- The CPU-fixed donor is not an independent renderer lineage source; relevant renderer neighborhoods are byte-identical to retail.

# Shader/cache / owner inference
- Raw compressed SDC string/payload scanning is not a renderer verdict.
- Low-entropy GLT correlation is obsolete after exact 192-bit GLT mapping.
- Menu-only shader activity is not a valid gameplay camera laboratory.
- A donor shader name/hash is not retail runtime ownership proof.
- PAIRS proximity or a registry string xref is not enough to promote a function to runtime pass owner.
- RTTI class membership alone is not virtual-method semantics.
- `Player+0x280` remains a hypothesis; do not treat it as proven because it appears in adjacent TimeSuit material.

# Runtime gameplay probes / constant path
- Any target-shader creation is not automatically gameplay-exclusive.
- Sight-associated raw CRC `0x8D672642` is not ADS-exclusive.
- Tool auto-close after a timer is not evidence of an engine crash.
- `0x007C3970` is not the ViewProjection producer; it is the dirty constant-cache flusher.
- Generic c0-c3 mutation at `0x007C3970` is unsafe.
- `0x007C3540` is a cached VS constant setter, not the semantic gameplay-camera owner.
- A numeric `+0xA8`, `+0x34`, or similar indirect-call displacement is not class/vtable identity.

# Camera facade identity
- the anonymous camera facade is not backend `d3dREND_DRIVER`.
- camera-feed `CALL [this->vtable+0x34]` is facade slot13, not automatically backend slot13.
- generic slot sweeps are not an authorized camera-search strategy.
- a View copy helper is not automatically the semantic gameplay/body View producer.

# Rejected runtime repairs

## v5.1 high-level gameplay View mutation — REJECT
The v5.1.1 result performed 40242 writes around the high-level gameplay View source while structural stereo survived.

User visual result:
- badly wrong camera/tilt;
- black wedges;
- eye desynchronization.

**STOP:** do not restore broad high-level `view+0x40` freezing as the final owner strategy.

## v5.1 per-shader last-texture replay — REJECT
The run performed 537488 RIGHT-eye shadow-state overrides across 183 learned shader pairs.

Raw evidence proved one sampled shader pair used six distinct stage-1 textures.

**STOP:** per-shader “remember last LEFT texture and replay in RIGHT” aliases unrelated resource state and must not be reused.

## Forced Z reflection — REJECT
The v5.1-era Z/reflection surgery worsened the visual result and is not required by the frozen OLD-GOOD transport.

**STOP:** do not force reflected OpenXR Z/orientation without new causal proof.

## Main-world-only owner split — REJECT
The attempted main-world-only split failed to produce a stable visual result.

**STOP:** do not revive this branch merely to chase current missing FX.

## Host-side image-only LEFT/RIGHT swap — REJECT
Swapping only image payloads separates the game-eye image from its physical `XrView` pose/FOV identity.

**STOP:** do not fix crossed-eye symptoms by swapping image payloads alone.

## Old off-axis denominator signs — REJECT
For the row-vector RH convention reviewed in the v5.3 line, the old mirrored denominator signs were wrong.

Correct coefficients:
- X `(l+r)/(r-l)`.
- Y `(u+d)/(u-d)`.

**STOP:** do not restore the old sign compensation.

## v5.2 simple exact shadow-depth bind as complete fix — CLOSED
The intervention executed exactly:
- 1398 exact LEFT binds.
- 1398 same-pair RIGHT mirrored binds.
- 0 failures.

Visible shadows did not return.

**STOP:** the missing 1024×2048 D16 asymmetry is real, but repeating the same one-bind mirror is not a new experiment.

# 2026-08-27 OLD-GOOD effect sweep negatives

## DP-only texture replay — REJECT for current baseline
Controlled v6.13 visual sweep:
- mode 3: DP exact TEX0+TEX1 -> breaks lighting.
- mode 4: DP resync +8 TEX0+TEX1 -> breaks lighting.

**STOP:** do not repeat DP-only exact/resync variants on the same OLD-GOOD baseline unless a new semantic owner explains why the behavior should differ.

## Wider DIP+DP/resync texture replay — SATURATED / NO MATERIAL RECOVERY
The other tested v6.13 widening variants, up to:
- DIP+DP resync windows;
- TEX0..TEX3 replay;
- additional shadow-state replay;
produced no material visible recovery of the missing effect families.

This is not proof that every resource/state combination is irrelevant. It is proof that **another cosmetic widening of the same correspondence/replay algorithm is low-information duplicate research**.

**STOP:** no v6.15/v6.16-style broader replay variant without a new pass/owner fact.

# COLD parser / interpretation corrections

## v3 SDC “0 extracted D3D9 blobs” — SUPERSEDED
The PAIR/SDC/COMPDB v3 closure reported zero extracted D3D9 blobs because its SDC parser model was incomplete.

Later ShaderDB/RTTI and OMNI closures recovered 120716 then 203984 compiled D3D9 blobs and 134 exact donor CRC matches.

**STOP:** do not use the v3 zero-blob count as evidence that local SDC bytecode is absent.

## Whole-file/blob donor hash mismatch — BOUNDED NEGATIVE ONLY
The MAX COLD harvest found no direct donor match under the tested whole-file/blob/raw-embedding hash families.

Later exact compiled D3D9 CRC matching recovered 134 donor matches.

**STOP:** do not infer shader absence from whole-file hash mismatch.

# Visual PASS must not be inferred from counters
High pair counts, zero stack failures, successful resource overrides, or successful XR publication prove execution, not headset correctness.

Canonical examples:
- v5.1 machinery executed but visual result was rejected.
- v5.2 exact bind executed but visible shadows remained absent.

# Current STOP RULE
Until `TIMESHIFTVR_OMNI_EXACT_CLOSURE_v6.1.0` is judged:
- no new missing-FX LIVE;
- no new broad texture-state replay sweep;
- no new camera rewrite;
- no controller/weapon integration as a distraction from the render-pass owner;
- no promotion of registry/init functions to runtime owners without direct D3D9 method evidence.

Current convergence path:

`v6.1 exact SDC/GLT/d3dPASS COLD closure -> bounded runtime pass owner -> one PRIMARY FACT LIVE mutation -> preserve OLD-GOOD baseline`
