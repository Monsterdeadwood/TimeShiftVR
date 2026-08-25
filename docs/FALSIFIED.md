# TimeShiftVR — FALSIFIED / STOP PATHS

Updated: 2026-08-25 08:19 +03

These paths were tested or structurally disproven. Do not reopen them without contradictory evidence.

## Startup / baseline
- Affinity-only CPU8 mitigation is not sufficient for stable startup.
- The CPU-fixed donor is not an independent renderer lineage source; renderer target neighborhoods used by the current camera work are byte-identical to retail.

## Shader/cache
- Raw compressed SDC string/payload scanning is not a renderer verdict.
- Low-entropy GLT correlation is obsolete after the exact 192-bit define-mask mapping.
- Menu-only shader activity is not a valid gameplay camera laboratory.

## Runtime gameplay probes
- Any target-shader creation is not a gameplay signal; shader creation can occur during loading/pre-game/menu contexts.
- The sight-associated raw CRC `0x8D672642` is not ADS-exclusive.
- Tool auto-close after a fixed timer is not evidence of an engine crash.
- More repeats of “does a frozen VP-family target appear?” no longer add information.

## Constant path
- Retail `0x007C3970` is not the ViewProjection producer. It is the dirty constant-cache flusher.
- Generic c0-c3 mutation at `0x007C3970` is unsafe.
- `0x007C3540` is the cached VS constant setter, not the semantic gameplay-camera owner.
- A generic numeric `+0xA8` or `+0x34` near an indirect CALL is not enough to identify the intended vtable/class.

## Generic ranking heuristics
- The old broad v3.3.1 ranking overpromoted unrelated functions because ordinary offsets such as `0xA8`, `0xBC`, and `0xC8` were counted near CALLs rather than as exact call dataflow.
- Generic slot13 / `+0x34` sweeps produce many unrelated virtual methods and are no longer authorized as a camera-search strategy.

## Camera facade identity
- The anonymous camera facade vtable is not the backend `d3dREND_DRIVER` vtable.
- v3.9.1 does not support a derived-vtable relation from the facade to `d3dREND_DRIVER`; slot-by-slot identity is 0 and RTTI does not establish that inheritance.
- Therefore camera-feed `CALL [this->vtable+0x34]` is facade slot13, not a direct backend `d3dREND_DRIVER::slot13` call.

## Historical-build caution
- Do not transfer retail RVAs into SP/MP/2006 builds by address.
- Match homologs by behavior, class/vtable position, normalized instruction structure, D3D9 slot usage, object offsets, and callgraph context.
- The old Atari/2006 image is currently lower-value for this gate; late Sierra SP/MP provide much stronger homolog evidence.

## Mutation stop condition
No stereo/HMD matrix mutation is authorized until the gameplay/world camera context is separated from menu, scope, shadow and other renderer cameras.

Current convergence path remains:

`camera facade slot13 -> backend renderer bridge -> dispatcher upstream context -> one passive LIVE authority test -> mutation`
