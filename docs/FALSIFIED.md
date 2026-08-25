# TimeShiftVR — FALSIFIED / STOP PATHS

Updated: 2026-08-25 22:54 +03

These paths were tested, structurally disproven, or visually rejected. Do not reopen them without contradictory evidence.

## Startup / baseline
- Affinity-only CPU8 mitigation is not sufficient for stable startup.
- The CPU-fixed donor is not an independent renderer lineage source; relevant renderer neighborhoods are byte-identical to retail.

## Shader/cache
- Raw compressed SDC string/payload scanning is not a renderer verdict.
- Low-entropy GLT correlation is obsolete after the exact 192-bit define-mask mapping.
- Menu-only shader activity is not a valid gameplay camera laboratory.
- More broad shader/cache archaeology is not the current blocker while a narrower runtime gate exists.

## Runtime gameplay probes
- Any target-shader creation is not a gameplay signal; shader creation can occur during loading/menu contexts.
- Sight-associated raw CRC `0x8D672642` is not ADS-exclusive.
- Tool auto-close after a fixed timer is not evidence of an engine crash.
- Repeating “does a VP-family shader appear?” adds no useful information now.

## Constant path
- `0x007C3970` is not the ViewProjection producer; it is the dirty constant-cache flusher.
- Generic c0-c3 mutation at `0x007C3970` is unsafe.
- `0x007C3540` is the cached VS constant setter, not the semantic gameplay-camera owner.
- A numeric `+0xA8` or `+0x34` near an indirect CALL is not sufficient class/vtable identity.

## Camera facade identity
- The anonymous camera facade is not backend `d3dREND_DRIVER`.
- camera-feed `CALL [this->vtable+0x34]` is facade slot13, not automatically backend `d3dREND_DRIVER::slot13`.
- Generic slot13 sweeps are not an authorized camera-search strategy.

These remain valid historical corrections, but they are no longer the active blocker.

# Rejected runtime repairs

## v5.1 high-level gameplay view mutation — REJECT
The executed v5.1.1 result performed **40242** writes to the high-level gameplay view source around `view+0x40` before `0x00956780`.

Automatic stereo transport survived, but the user observed:
- badly wrong camera/tilt;
- black wedges;
- eye desynchronization.

The mutation sits upstream of wider rendering/culling/lighting ownership and is too invasive.

**STOP:** do not restore this high-level camera/source freezing strategy as the final owner solution.

## v5.1 per-shader shadow texture replay — REJECT
The v5.1.1 run performed **537488** RIGHT-eye shadow-state overrides using **183** learned shader pairs.

Raw evidence showed sampled shadow-consuming VS/PS pairs can use multiple distinct stage-1 textures; one pair used **six different stage-1 textures**.

Therefore “remember the last LEFT texture for this shader pair and replay it in RIGHT” aliases unrelated cascade/lookup state.

**STOP:** never use per-shader last-texture learning as shadow-state identity.

## Forced Z reflection — REJECT
The v5.1-era camera/Z reflection surgery worsened the visual result and is not required by the frozen working stereo core.

**STOP:** do not force OpenXR Z reflection or reflected inverse orientation without a new causal proof.

## Main-world-only owner split — REJECT
The attempted main-world-only owner surgery did not produce a stable visual result and was rolled back before the v5.2 causal test.

**STOP:** do not reintroduce this split merely to chase the current projection/shadow symptoms.

## Host-side image-only LEFT/RIGHT swap — SUPERSEDED / REJECT
A host-side payload swap was introduced to compensate for crossed-eye appearance, but later source review showed it breaks the physical eye identity contract by pairing a game-eye image with the opposite native `XrView` pose/FOV.

v5.3 restores:
- LEFT image -> LEFT pose/FOV;
- RIGHT image -> RIGHT pose/FOV.

**STOP:** do not fix crossed-eye symptoms by swapping only image payloads.

## Old off-axis denominator signs — REJECT
For the row-vector RH convention used by the current runtime, the previous mirrored-sign formulas were wrong.

Correct coefficients are:
- horizontal: `(l+r)/(r-l)`;
- vertical: `(u+d)/(u-d)`.

**STOP:** do not restore the old denominator signs.

## v5.2 simple exact shadow-depth bind as complete fix — CLOSED
The v5.2 causal rollback/shadow-bind run proved the intervention executed exactly:
- 1398 exact LEFT binds;
- 1398 same-pair RIGHT mirrored binds;
- 0 failures.

The user still saw **no shadows**.

Therefore:
- the missing exact 1024×2048 D16 bind is real state asymmetry;
- but copying that one bind is not sufficient to restore visible shadows.

**STOP:** do not repeat the same simple bind mirror as if its visible effect were still unknown.

## Visual PASS must not be inferred from counters
High pair counts, zero stack failures, successful texture overrides or successful XR publication prove that machinery executed. They do **not** prove that the headset image is correct.

The v5.1 and v5.2 runs are the canonical examples:
- structural machinery executed;
- visual result remained wrong.

## Current stop condition
Until v5.3 projection identity is judged:
- no new shadow mutation;
- no new broad camera mutation;
- no controller/hand integration;
- no return to generic reverse-engineering sweeps.

Current convergence path:

`v5.3 physical eye/projection identity -> freeze sane stereo geometry -> locate post-RETURN_RIGHT final-light/final-color owner -> only then apply the smallest causal lighting repair`
