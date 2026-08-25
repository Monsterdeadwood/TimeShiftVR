# TimeShiftVR — NEXT

Updated: 2026-08-25 08:19 +03

## Current serial gate — facade slot13 -> backend renderer

The shader/cache and generic renderer-authority phases are no longer the active blocker.

Current missing fact:

`camera facade slot13 -> ? -> d3dREND_DRIVER matrix producer`

Frozen late-build addresses:

| Build | Facade slot13 | Camera feed | Camera dispatch | Backend matrix producer |
|---|---:|---:|---:|---:|
| Retail | `0x007FB740` | `0x007FB790` | `0x007FBF50` | `0x0079E100` |
| Sierra SP | `0x007F2830` | `0x007F2880` | `0x007F3040` | `0x00789E40` |
| Sierra MP | `0x007FA190` | `0x007FA1E0` | `0x007FA9A0` | `0x0079E830` |

Active analyzer:

`TIMESHIFTVR_CAMERA_FACADE_BRIDGE_COLD_v4_0_0`

### PASS
Retail + SP + MP independently show the same facade-slot13 forwarding path into the proven backend renderer/matrix-producer lane.

### PARTIAL
One late build exposes a direct bridge and the homologs require one additional static hop.

### FAIL / ADAPT
Facade slot13 is unrelated to the proven backend lane. Do not return to generic `+0x34` scans; inspect only the tiny facade slot13 stubs/direct targets and revise the architecture.

## Next gate after PASS — facade dispatcher upstream context

Target the exact camera-dispatch methods:
- retail `0x007FBF50`.
- SP `0x007F3040`.
- MP `0x007FA9A0`.

Recover:
1. the exact virtual/interface slot used to invoke dispatcher;
2. the upstream gameplay/render-view descriptor provenance;
3. which field(s) distinguish gameplay/world camera from menu/scope/shadow/other render cameras;
4. whether the same object/context is stable across an entire LEFT+RIGHT pair.

Acceptance: one exact, reversible context gate that can authorize camera matrix intervention only for the intended world view.

## First authorized LIVE after static convergence

Only after the dispatcher/context gate is finite:
- instrument, do not mutate;
- record object pointer / caller / camera context / c0-c4 source identity;
- gate on the strongest gameplay-world signal, currently raw VS CRC `0x416CFC1B` where useful;
- one run should resolve all remaining candidate contexts.

LIVE PASS should answer one causal question: which exact facade/renderer context owns gameplay ViewProjection.

## Mutation remains blocked
Do not yet:
- replace c0-c3 generically at `0x007C3540` or `0x007C3970`;
- apply HMD pose to every renderer camera;
- treat sight CRC `0x8D672642` as an ADS-only gate;
- start hand/controller integration;
- build stereo transport around an unclassified camera context.

## Future intervention objective
Once gameplay camera authority is exact:

`gameplay camera descriptor -> facade -> backend ViewProjection source -> per-eye view/projection -> existing D3D9 draw path`

Keep `c4` coherent with the per-eye camera world position when c0-c3 are changed.
