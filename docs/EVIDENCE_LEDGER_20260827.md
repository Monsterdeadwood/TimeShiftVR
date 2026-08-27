# TimeShiftVR — Evidence Ledger — 2026-08-27

This ledger advances the canonical repository from the 2026-08-25 v5.3 state through the verified 2026-08-27 runtime and COLD research line. Historical v4.7.2–v5.3 evidence remains valid unless explicitly superseded below.

## Frozen target / baseline
- Target: GOG TimeShift 1.02 x86.
- Retail `TimeShift.exe` SHA256: `78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613`.
- CPU-fixed startup donor SHA256: `49bcca23d3d7872fbb578183b77472b64ecd8e3f8d68bfcccb1af6f04d4d8ed6`.
- Frozen true-stereo transport baseline: v4.7.2 OLD-GOOD, 5858 same-frame pairs, 41006/41006 eye uploads, 3197 OpenXR frames.
- COLD analyses below did not launch the game, inject, patch, or mutate the source corpus.

# Runtime line after the old GitHub snapshot

## OLD-GOOD effect/state sweep — v6.10 → v6.14
The active visual line retained the OLD-GOOD v4.7.2 stereo/camera contract while probing missing lighting/effect state rather than rewriting stereo geometry.

`TIMESHIFTVR_OLDGOOD_EFFECT_RESYNC_10MODE_v6_13_1_RECOVERYFIX` defined the controlled modes as:
1. DIP exact TEX0+TEX1 — current best / old mode 6.
2. DIP resync +8 TEX0+TEX1.
3. DP exact TEX0+TEX1.
4. DP resync +8 TEX0+TEX1.
5. DIP+DP exact TEX0+TEX1.
6. DIP+DP resync +4 TEX0+TEX1.
7. DIP+DP resync +8 TEX0+TEX1.
8. DIP+DP resync +16 TEX0+TEX1.
9. DIP+DP resync +16 TEX0..TEX3.
0. MAX: DIP+DP resync +32 TEX0..TEX3 + shadow-state.

User-observed visual verdict from the completed manual sweep:
- modes 3 and 4 break lighting;
- the other tested widening/resync modes produced no material visible improvement;
- current-best OLD-GOOD + DIP exact TEX0+TEX1 remains the useful runtime baseline for effect work.

Disposition:
- DP-only replay/resync is a negative path for the current baseline;
- merely widening the same ordinal/resync texture replay does not recover the missing rain/explosion/smoke/shadow families;
- do not produce another cosmetic variant of this same replay strategy without a newly identified semantic pass/owner.

`TIMESHIFTVR_OLDGOOD_FX_PASS_BOUNDARY_v6_14_0.zip` was generated after this verdict, but is not recorded here as an executed proof.

# Camera / player-frame owner closure

## Stack-local / virtual camera owner evidence
`TIMESHIFTVR_VIRTUAL_CAMERA_OWNER_COLD_RESULT_20260827_044735.zip`
SHA256: `bc1ed62818092e46ea33df5b6e31ec440594358f328841d21f6f2c4d4b08120c`

Proven structural chain:
- `0x0069AFB0` performs an indirect virtual call through object vtable slot `+0x2C` and then submits the resulting `View` through `0x00956680`.
- `0x00956680` is the generic View-stack push: it increments the stack count, advances with stride `0x364`, and copies a source View using `0x004B0DE0`.
- passive evidence returned from the copy at `0x00956719`.
- candidate implementation family included `0x004B0C40`, `0x00699940`, `0x0069A340`, `0x007FEFE0`; none is promoted to exact gameplay owner solely because it calls the View copy helper.

## Owner/source/fire evidence
`TIMESHIFTVR_OWNER_SOURCE_FIRE_RESULT_20260827_034120.zip`
SHA256: `42a92b57ed6dc453f7ca9345bd27e9f9d2b90d098446154a8043206c71cf8c10`

Observed corpus:
- 258135 events.
- HEAD discover hits: 1.
- HEAD source hits: 99116.
- FIRE events: 159018.
- strongest non-copy HEAD source writer: `0x005A1CC9` with 10064 hits.
- FIRE positive-control `0x00956780`: 129045 hits.

This is ranking evidence, not authorization to mutate a generic trace/spawn site.

## True main player-frame closure
`TIMESHIFTVR_TRUE_MAIN_PLAYER_FRAME_COLD_RESULT_20260827_135326.zip`
SHA256: `559a19527693a59453ef747986fa7c5d1bbfd80bf30c22e526e12a60da4b3f22`

Strongest facts:
- renderer View-stack header: `root+0x618`; slot0 View: `root+0x620`.
- `0x00956680` pushes/copies View state with stride `0x364` using `0x004B0DE0`.
- passive hardware evidence caught the dynamic mouse-look write to slot0 inside the second `0x004B0DE0` copy; saved outer ESI was `root+0x618`.
- mirrorSys also uses `0x00956680`, but at secondary indices after main and is excluded as the slot0 owner.
- `0x00681DD0/0x00681EC7` perform whole-View write/reset to slot0 before dynamic submit and are separately classified.
- `0x00681DD0` has a direct callsite at `0x00409D37` inside `0x004098C0`; `0x006595A0` follows at `0x00409D46`.
- `0x004098C0` has no ordinary direct caller in the recovered graph, indicating a pointer/vtable identity path.

Still unknown: exact non-mirror gameplay/body producer identity feeding the slot0 source through `0x00956680`.

# Donor / shader / pass closure

## Donor closure
`TIMESHIFTVR_DONOR_CLOSURE_RESULT_20260827_052826.zip`
SHA256: `9a4386322664b0c8dcb1693211447e8305bb22ec8fdbe1aaf5b5f43223d6cd04`

Recovered ShaderToggler candidate families:
- HUD PS `759149124`.
- rain screen FX VS `3008662745`, `1294141040`.
- blood PS `1730621601`.
- death PS `1208193290`.
- distortion PS `3000606172`.
- low-health PS `2319713783`.
- bullet-time VS `2236193038`.
- blur/distortion PS `751228937`.
- crosshair/bullet-tracer VS `1922619837`, PS `162489781`; donor metadata says this family affects lights.
- remove-time-filter VS `2751074104`.

Exact retail time AOB anchor: file/RVA `0x3EB3F`, VA `0x0043EB3F`.
Donor/source material is candidate generation only; retail proof remains separate.

## Maximum COLD harvest
`TIMESHIFTVR_MAX_COLD_HARVEST_RESULT_20260827_053816.zip`
SHA256: `c8d0bf4565a3c1d3971953047e417824b0eec7b0f667d785df41a648132ddf02`

Totals:
- TimeShift-like EXEs: 9.
- PE modules: 41.
- SDC files: 375.
- ShaderToggler hash assignments: 35.
- Cheat-table records: 7; AOBs: 12.
- TimeShift saves/TSS: 146.

The tested whole-file/blob hash families and raw embedding did not directly map known donor hashes to local SDC data. This was a bounded negative, not proof that the shaders are absent.

## PAIR / SDC / compilation database closure
`TIMESHIFTVR_PAIR_SDC_COMPDB_CLOSURE_RESULT_20260827_135123.zip`
SHA256: `25f24b8b1fedf4b7f3079ec6d14e2c65fe26f94c46b96508545bfea525bf392b`

- workers: 32/32.
- known donor CRCs: 23.
- PAIRS: 9180.
- pass/Compilation DB xrefs: 55.
- candidate owner functions: 10.
- cheat-table structure fields: 5280.
- TimeSuit closure rows: 6.
- direct donor CRC in PAIRS: 0.
- SDC blob CRC in PAIRS: 0.

The v3 SDC bytecode extractor reported zero D3D9 blobs; this parser limitation was superseded by the later corrected SDC work below.
`Player+0x280` remains a hypothesis, not a proven retail owner.

## ShaderDB + RTTI closure
`TIMESHIFTVR_SHADERDB_RTTI_CLOSURE_RESULT_20260827_141602.zip`
SHA256: `fcd4d88528558d7b37d27689b5de8e447d5b95ea83796ce9b8ea15e1a1d486b1`

- workers: 32/32.
- PAIRS: 9180; unique SHA: 374; parse success: 374/374.
- canonical GLT slot count: 192; one slot-name schema.
- retail GLT descriptor assignments: 109; slot-index agreements: 109.
- GLT metadata fields: `0x600..0x62C`, stride 4; static xrefs: 919.
- RTTI pass vtable instances: 28; method rows: 700.
- SDC files: 375; unique SHA: 198.
- extracted D3D9 blobs: 120716.
- exact donor CRC matches: 134.
- legacy `shaders.cache` blobs: 16623; exact donor CRC matches: 0.

Dynamic-light descriptors include:
- slot 33 / descriptor `0x108`: `SDR_GLT_PARALLAX_SHADOW`.
- slots 41–44: `DYN_LIGHT0..3_DIFFUSE`.
- slots 45–48: `DYN_LIGHT0..3_SPECULAR`.
- slot 49: `DYN_LIGHT0_CUBEMAP_SHADOW`.
- slot 72: `DYN_LIGHT_BRANCH`.

Exact compiled D3D9 CRC matches are stronger evidence than donor labels or raw PAIR proximity.

## OMNI COLD closure v5
`TIMESHIFTVR_OMNI_COLD_CLOSURE_RESULT_20260827_144128.zip`
SHA256: `f85cf6e1ce83abbb811b30d8f69085dccaa73822c390b4e2a84032231262d18d`

COLD clean PASS:
- workers: 32.
- corpus files: 22102.
- donor CRCs: 23.
- CT fields: 5280.
- PAIR files: 9180; unique SHA: 374.
- GLT registry rows: 436.
- RTTI method rows: 900.
- EXEs: 9; AOB rows: 18.
- compilation DB xrefs: 55.
- SDC files: 375; unique SHA: 198.
- SDC D3D9 blobs: 203984.
- exact donor CRC matches: 134.
- owner-ranking rows: 485.
- cross-version homology rows: 122.
- S3D files: 17.
- TimeSuit rows: 6.

Strong static owner candidates:
- retail `0x003A9652`: STRONG 736 from GLT registry + PAIR-slot agreement + string xrefs across dynamic lights/final-combiner families.
- retail `0x003A6DEC`: STRONG 642 from GLT registry + PAIR-slot agreements over common/shadowmapped families.
- RTTI virtual-method candidate family includes `0x003A5F10`, `0x003A5F20`, `0x003A74A0`, `0x003A7FB0` across `d3dPASS_BASE`, `d3dPASS_DISTORT`, `d3dPASS_FORD`, `d3dPASS_GLT`, `d3dPASS_IMAGE_FILTER`, `d3dPASS_PARTICLES`, `d3dPASS_PROJ_SHD`, `d3dPASS_RAIN`, `d3dPASS_WATER`.

These rankings are strong structural candidates, not yet proof of runtime render semantics. Registry/init code must be separated from methods that actually touch the D3D9 device.

# Current exact COLD gate — v6.1
Generated package:
`TIMESHIFTVR_OMNI_EXACT_CLOSURE_v6.1.0.zip`
SHA256: `7bfdb72c5dc71719d7b1cf487be3df35c120798ab1dc345381800fac80aa83dc`

Status: **GENERATED / NOT YET RESULT-PROVEN**.

v6.1 corrects the multi-group SDC model discovered from v5 evidence. For multi-group SDCs the group metadata is interleaved:
1. `u32 group_count`, `u32 total_record_count`, `u32 total_compressed_bytes`;
2. for each group: `compressed_size`, `record_count`, followed by that group's per-record `keyA`, `keyB`, `raw_record_size` triplets;
3. zlib payloads follow in group order.

The gate is designed to:
- map every compiled D3D9 shader to exact SDC record + `keyA/keyB`;
- detect donor VS/PS co-residence in one compiled record;
- validate GLT tails as 43-byte permutation records;
- count lighting/shadow/dynamic-light pass permutations;
- recover `d3dPASS_*` RTTI virtual methods;
- scan those methods for direct `IDirect3DDevice9` COM activity;
- rank likely runtime render methods above registry/initialization methods.

Exact preflight contract:
- MISSING FACT: exact SDC group/record map, donor shader co-residence and keys, GLT 43-byte option records, actual `d3dPASS` runtime methods touching D3D9.
- WHY NOT COLD: N/A; v5 exposed the required invariants and the evidence is local.
- PASS: SDC boundaries/decompression/raw splits validate; donor CRCs map to exact records; GLT validates; pass virtual methods separate by real D3D9 COM activity.
- FAIL: invariants fail broadly or runtime ownership remains indistinguishable.
- BASELINE MUST HOLD: no game launch, injection, patch, DLL install, or source mutation.

# Canonical state after this ledger

## PROVEN
- true same-frame OpenXR stereo transport exists and v4.7.2 remains the frozen transport baseline.
- simple v5.1/v5.2 broad camera/last-texture/one-shadow-bind repairs are closed.
- OLD-GOOD effect work does not benefit from simply widening DP/DIP/resync texture replay; DP-only modes can actively damage lighting.
- renderer View-stack mechanics, main slot0 behavior, donor shader families, 192-slot GLT registry, exact compiled SDC shader identity, d3dPASS RTTI families, and strong retail pass candidates are now substantially mapped.

## FALSIFIED / bounded negatives
- per-shader last-texture replay.
- simple exact shadow-depth bind as complete visible fix.
- host-side image-only eye swap / old projection-sign compensation.
- broad high-level gameplay View mutation.
- DP-only effect replay/resync on the OLD-GOOD baseline.
- another wider texture-resync sweep without a new semantic pass owner.

## STILL UNKNOWN
- exact non-mirror gameplay/body producer feeding renderer slot0.
- exact runtime `d3dPASS_*` virtual method(s) responsible for the missing lighting/effect composition boundary.
- exact SDC record/key pairing and GLT 43-byte permutation semantics across the target pass families, pending v6.1 result.
- smallest safe retail mutation point that can restore missing FX while preserving OLD-GOOD stereo/light baseline.

## STOP RULE
Do not create a new LIVE/build/injection/capture for missing FX until v6.1 COLD exact closure either identifies a bounded runtime pass owner or demonstrably fails to separate one. After COLD saturation, authorize only one PRIMARY FACT mutation at the exact pass boundary, with the frozen OLD-GOOD stereo/light state as baseline and broad passive secondary harvest around that owner.
