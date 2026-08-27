# TimeShiftVR — Canonical State

Updated: 2026-08-27 +03

## Status
**ACTIVE. True same-frame OpenXR stereo remains proven. The active gate is now exact COLD render-pass ownership, not projection archaeology or another broad texture-replay LIVE sweep.**

Canonical next experiment:
`TIMESHIFTVR_OMNI_EXACT_CLOSURE_v6.1.0`

Status of that package: **GENERATED / COLD ONLY / result not yet returned**.

Full 2026-08-27 evidence ledger:
`docs/EVIDENCE_LEDGER_20260827.md`

Historical runtime ledger through v5.3 remains in:
`docs/RUNTIME_LINEAGE_20260825.md`

## Frozen target
- Game: GOG TimeShift 1.02 x86.
- Retail SHA256: `78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613`.
- Corpus root: `C:\GOG Games\TimeShift1`.
- Shared tools: `C:\GOG Games\VR Research Tools`.
- CPU-fixed startup donor SHA256: `49bcca23d3d7872fbb578183b77472b64ecd8e3f8d68bfcccb1af6f04d4d8ed6`.

# Frozen working baseline

## v4.7.2 OLD-GOOD true-stereo core
This remains the transport baseline that no later branch may regress:
- 5858 completed same-frame LEFT/RIGHT pairs.
- 41006 / 41006 LEFT/RIGHT uploads.
- 3197 OpenXR frames.
- Quest IPD around 63.63 mm.
- asymmetric per-eye OpenXR FOV available.
- same-frame RIGHT re-entry proven.
- live binocular content reaches the headset.

The later OLD-GOOD effect line preserves this stereo/camera contract.

## Current best effect-state branch
The controlled v6.13 10-mode sweep preserved OLD-GOOD stereo while varying DIP/DP texture/state replay.

User visual verdict:
- mode 3 = DP exact TEX0+TEX1: breaks lighting.
- mode 4 = DP resync +8 TEX0+TEX1: breaks lighting.
- the other widened DIP+DP/resync/TEX0..3/shadow-state modes produced no material visible recovery.
- current-best state remains OLD-GOOD + DIP exact TEX0+TEX1 (old mode 6 / v6.13 mode 1).

Therefore the active problem is no longer “try more of the same texture replay.” The missing FX path needs a semantic pass owner.

# PROVEN COLD foundation — 2026-08-27 closure

## Renderer View stack / player-frame lane
- renderer View-stack header: `root+0x618`.
- slot0 View: `root+0x620`.
- `0x00956680` is the generic View-stack push/copy routine, stride `0x364`, using `0x004B0DE0`.
- dynamic mouse-look was observed writing slot0 inside the second `0x004B0DE0` copy with saved outer ESI = `root+0x618`.
- mirrorSys uses the same push later at secondary indices and is excluded from main slot0 ownership.
- `0x00681DD0/0x00681EC7` are whole-View write/reset operations before dynamic submit.
- `0x00681DD0` is called at `0x00409D37` inside `0x004098C0`; `0x004098C0` is reached by pointer/vtable lineage rather than a recovered ordinary direct caller.

Exact non-mirror gameplay/body producer identity is still not fully proven.

## Donor candidate families
Recovered donor shader families include rain, blood, death, distortion, low-health, bullet-time, blur/distortion, crosshair/bullet-tracers, and remove-time-filter. The crosshair/bullet-tracer donor family is specifically annotated as affecting lights.

Donor/source labels are candidate generation only; retail proof remains separate.

## Exact shader / GLT / pass evidence
ShaderDB/RTTI closure proved:
- 9180 PAIRS; 374 unique parsed SHA; 374/374 parse success.
- canonical GLT slot count: 192.
- 109 retail GLT descriptor assignments with 109 slot-index agreements.
- GLT metadata fields at `0x600..0x62C`, stride 4; 919 static xrefs.
- 28 RTTI pass-vtable instances in the first closure; later OMNI ranking expanded method evidence to 900 rows.
- 375 SDC files; 198 unique SHA.
- 120716 D3D9 blobs in the ShaderDB/RTTI closure; 203984 in the expanded OMNI closure.
- 134 exact donor CRC matches to compiled D3D9 shader blobs.

Dynamic-light GLT anchors:
- slot 33: `SDR_GLT_PARALLAX_SHADOW`.
- slots 41–44: `DYN_LIGHT0..3_DIFFUSE`.
- slots 45–48: `DYN_LIGHT0..3_SPECULAR`.
- slot 49: `DYN_LIGHT0_CUBEMAP_SHADOW`.
- slot 72: `DYN_LIGHT_BRANCH`.

## OMNI COLD closure v5
`TIMESHIFTVR_OMNI_COLD_CLOSURE_RESULT_20260827_144128.zip` completed COLD-clean with 32 workers.

Key totals:
- corpus files 22102.
- PAIRS 9180 / unique SHA 374.
- GLT registry rows 436.
- RTTI method rows 900.
- SDC files 375 / unique SHA 198.
- SDC D3D9 blobs 203984.
- exact donor CRC matches 134.
- owner-ranking rows 485.
- cross-version homology rows 122.

Strong retail static candidates:
- `0x003A9652` — STRONG 736: GLT registry + PAIR-slot agreement + string xrefs across dynamic-light/final-combiner families.
- `0x003A6DEC` — STRONG 642: GLT registry + PAIR-slot agreement across common/shadowmapped families.
- RTTI virtual-method family includes `0x003A5F10`, `0x003A5F20`, `0x003A74A0`, `0x003A7FB0` across `d3dPASS_BASE`, `DISTORT`, `FORD`, `GLT`, `IMAGE_FILTER`, `PARTICLES`, `PROJ_SHD`, `RAIN`, `WATER`.

These are **strong candidates, not final runtime semantics**. Registry/initialization paths must be separated from virtual methods that actually touch the D3D9 device.

# FALSIFIED / do not repeat
- v5.1 high-level `view+0x40` camera mutation.
- v5.1 per-shader last-LEFT-texture replay.
- forced Z reflection / main-world-only owner split.
- host-side image-only eye swap and old projection denominator signs.
- v5.2 simple exact 1024×2048 D16 bind mirror as the complete visible shadow fix.
- DP-only exact/resync effect replay on the OLD-GOOD baseline: modes 3/4 damage lighting.
- another wider DIP/DP/resync/TEX0..3/shadow-state sweep without a new semantic owner: tested widening produced no material visual recovery.

# STILL UNKNOWN
1. Exact SDC multi-group record/key map for all target compiled shaders under the corrected group layout.
2. Whether donor VS/PS pairs co-reside in the same exact compiled SDC record and with which `keyA/keyB`.
3. Exact semantics of GLT 43-byte permutation tails around the lighting/shadow families.
4. Which exact `d3dPASS_*` runtime virtual method(s) touch D3D9 at the missing final-light/effect boundary.
5. Exact non-mirror gameplay/body producer feeding renderer slot0.
6. The smallest retail mutation point that restores missing FX while preserving OLD-GOOD stereo and stable lighting.

# Current gate — OMNI EXACT CLOSURE v6.1
The corrected v6.1 parser/closure uses the multi-group SDC layout recovered from v5 evidence and must stay COLD-only.

MISSING FACT: exact SDC group/record map, donor shader co-residence and keys, GLT 43-byte option records, and actual `d3dPASS` runtime methods touching D3D9.

WHY NOT COLD: N/A; v5 exposed the required invariants and all required evidence is local.

PASS: SDC boundaries/decompression/raw splits validate; donor CRCs map to exact records; GLT tails validate; pass virtual methods separate by real D3D9 COM activity.

FAIL: invariants fail broadly or runtime ownership remains indistinguishable.

BASELINE MUST HOLD: no game launch, injection, patch, DLL install, or source mutation.

# STOP RULE
Do **not** create another LIVE missing-FX experiment until v6.1 has either:
- produced a bounded exact pass owner suitable for one-primary-fact causal mutation; or
- failed in a way that identifies the next specific COLD missing fact.

After COLD saturation, any LIVE test must preserve OLD-GOOD stereo/light baseline and mutate one exact semantic pass boundary only, with broad compatible passive harvest around it.
