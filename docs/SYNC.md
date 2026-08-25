# TimeShiftVR — SYNC

Updated: 2026-08-25 22:54 +03

This repository is the persistent canonical state for TimeShiftVR research. Carry forward verified facts, bounded negatives, explicit visual verdicts, reproducible next gates and tool-lineage corrections. Do not store copyrighted game binaries here.

## Frozen corpus / target
- corpus: `C:\GOG Games\TimeShift1`
- shared tools: `C:\GOG Games\VR Research Tools`
- retail: GOG TimeShift 1.02 x86
- retail SHA256: `78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613`
- CPU-fixed donor SHA256: `49bcca23d3d7872fbb578183b77472b64ecd8e3f8d68bfcccb1af6f04d4d8ed6`

## Historical COLD lineage
### Corpus / shader decode
- v1.x: collector/path/Python fixes.
- v2.0: shader-cache analysis.
- v2.1: SDC decoder.
- v2.2: GLT 192-bit define-mask oracle.
- v2.3: sight-associated shader + frozen SM3 VP family.

### Passive D3D9 / gameplay authority
- v3.0.x: passive D3D9 proxy lineage and CPU-startup baseline work.
- v3.1.x: gameplay matrix captures establish c0-c4 semantics and stable runtime callsites.

### Static renderer / camera owner lineage
- v3.2.x: `0x007C3970` proven cache flusher; `0x007C3540` cached VS constant setter.
- v3.3.x: RTTI/vtable evidence; broad numeric ranking later bounded as too permissive.
- v3.4.x: cross-build class-aware lineage.
- v3.5.0: exact setter slot-load -> indirect CALL dataflow; unique startRegister=0,count=4 uploader in retail/SP/MP.
- v3.6.0: backend `d3dREND_DRIVER`, immediate c0-c4 sources and matrix producer family.
- v3.7.0: generic +0x34 ranking found many false positives.
- v3.8.0: exact camera-feed owner/dispatcher family.
- v3.9.0: Ghidra API tool failure, no verdict.
- v3.9.1: facade/backend vtable separation proven.
- v4.0.0: facade-slot13 COLD bridge analyzer.

The v4.0 COLD gate is now **historical evidence, not the active blocker**.

# Working runtime lineage

## v4.7.2 — TRUE OPENXR STEREO BASELINE
Status: **KEEP**.

Evidence:
- 5858 same-frame stereo pairs.
- 41006 / 41006 LEFT/RIGHT uploads.
- 3197 OpenXR frames.
- Quest IPD around 63.63 mm.
- asymmetric physical per-eye FOV available.

User visual:
- real stereo/depth present.
- HMD orientation convention still wrong.
- shadows absent in duplicated stereo path.

Known package SHA256 recorded from the working line:
`9F865393...EBF15` (historical abbreviated record; retain exact local artifact when available).

## v4.8 / v4.9 — instrumentation / row-view correction
Status: **KEEP as diagnostic working lineage**.

Added:
- corrected row-view orientation path;
- D3D9 pass/resource profiler;
- XR controller/input census;
- adaptive stack calibration;
- gameplay-view gate;
- exact restore policy.

External capture policy:
- internal D3D9 wrapper owns the game process;
- do not stack apitrace/RenderDoc D3D9 wrappers in the same process;
- RenderDoc may be used on the x64 D3D11 OpenXR host when specifically needed;
- PresentMon is safe supplemental telemetry.

## v5.0 — SHADOW OWNER EVIDENCE
Status: **PROVEN asymmetry**.

- native 1024×2048 D16 shadow texture isolated.
- native binds 3817.
- LEFT stereo binds 256.
- RIGHT stereo binds 0.
- RIGHT shadow-consuming draws still execute.

This narrowed the missing-shadow problem to state/resource ownership, but did not prove one copied bind was sufficient.

## v5.1.0 — BUILD FAIL
Status: **NO VERDICT**.

Initial package failed compile due `write_phase_file` declaration order.

## v5.1.1 — BROAD CAMERA + SHADOW REPAIR
Status: **STRUCTURAL TRANSPORT PASS / VISUAL REJECT**.

Result:
`TIMESHIFTVR_XR_TRUE_STEREO_HMD_MVP_v5_1_1_RESULT_20260825_223246.zip`
SHA256:
`896952fa47de3489f4517d4bf49db9811c3ce344913c38ffa8be9188beffed44`

Automatic:
- 3317 pairs.
- 40242 high-level camera source writes.
- 537488 RIGHT shadow repair draws.
- 183 learned shader pairs.
- 23219 / 23219 eye uploads.

User visual:
- very wrong camera/tilt.
- black wedges.
- eye desync.

Postmortem:
- high-level view source mutation too invasive.
- per-shader shadow learning aliases multiple stage-1 textures; sampled pair uses six distinct stage1 textures.

Disposition:
**REJECT broad repair strategy.**

## v5.2A — CAUSAL ROLLBACK + EXACT SHADOW BIND
Status: **INTERVENTION EXECUTED / VISUAL SHADOW FIX FAIL**.

Result:
`TIMESHIFTVR_CAUSAL_ROLLBACK_SHADOW_BIND_RESULT_20260825_221925.zip`
SHA256:
`f0936e113256b22a5b97114130ed1efb4583417fa1d39efb8f85a55ee4637f57`

Automatic:
- exact depth captures 1.
- 1398 LEFT exact binds.
- 1398 RIGHT mirrored binds.
- 0 mirror failures.
- 2172 same-frame pairs.
- 0 stack failures.
- 0 re-entry failures.
- 0 matrix-contract failures.
- 2169 XR-published pairs.
- 0 XR readback failures.

User visual:
- fish-eye/crooked image.
- strong tilt.
- shadows still absent.

Disposition:
**simple exact shadow-depth bind is CLOSED as the complete visible fix.**

## v5.2B — SAFE PAIR REPAIR
Status: **GENERATED / HOLD / NOT CANONICAL NEXT**.

Package:
`TIMESHIFTVR_SAFE_PAIR_REPAIR_v5_2_0.zip`
SHA256:
`aad92e5d76c6d1a5665398aacee36e13bf8061f218966f6610d0f5e8490311c1`

This is a sibling branch built from the v5.1.1 corpus, not a replacement for the executed v5.2A causal result.

Design correction:
- no per-shader last-texture learning;
- capture LEFT state by exact DIP ordinal;
- repair RIGHT only on exact draw-signature match.

Corpus support:
- 256/256 analyzed pairs have equal LEFT/RIGHT DIP count.
- 26028/26028 sampled LEFT shadow-bound DIP draws have an exact RIGHT partner at the same ordinal with matching primitive/geometry/VS/PS identity.

Hold reason:
projection/physical-eye identity must be corrected first, otherwise visual shadow verdicts remain contaminated.

## v5.3.0 — PROJECTION IDENTITY RECOVERY
Status: **STATIC READY / CURRENT CANONICAL NEXT LIVE**.

Package:
`TIMESHIFTVR_PROJECTION_IDENTITY_RECOVERY_v5.3.0_30S_ONECLICK.zip`
SHA256:
`d247be9b3b27b1477d3870b6bc2615c87051d1ab6078f55de6acc99c190f5769`

Static audit:
- 31 checks PASS.

Fixes:
- physical LEFT image/pose/FOV identity restored end-to-end.
- physical RIGHT image/pose/FOV identity restored end-to-end.
- host image-only swap removed.
- row-vector RH off-axis denominators corrected to `(r-l)` / `(u-d)` form.
- main-world-only surgery absent.
- forced Z reflection absent.
- active shadow mutation absent.
- Windows mouse injection absent.
- final backbuffer captured before SBS overwrite.
- passive post-`RETURN_RIGHT` draw ranking enabled.

Run policy:
- 30-second focused capture after true stereo starts.
- do not use F2/F3/F5.
- F8 recenter allowed if needed.

# Canonical architecture now

`TimeShift D3D9 gameplay render`

`-> same-frame LEFT render`

`-> same-frame RIGHT re-entry`

`-> per-eye CPU readback / transport`

`-> x64 D3D11 OpenXR host`

`-> physical LEFT/RIGHT XrView submission`

Camera/pose baseline:
`BODY_PLUS_HMD + ROW_VIEW_CORRECTED`

Current required correction:
`physical eye identity + correct row-vector RH off-axis projection`

Shadow work is downstream of this gate.

# Evidence hygiene
- Automatic counters prove execution, not visual correctness.
- User headset observation is the arbiter for visual fusion/camera/shadow quality.
- Do not call a RESULT ZIP “PASS” merely because it contains healthy telemetry.
- Preserve exact hashes and version lineage.
- Donor/source candidates do not replace retail runtime proof.
- Do not stack conflicting intrusive D3D9 wrappers.
- One primary missing fact per LIVE run; harvest secondary evidence only when it does not compromise causality.

# Current global gate

`v5.3 projection identity recovery`

then, only after projection PASS:

`post-RETURN_RIGHT final-light/final-color owner -> smallest causal shadow repair`

The safe-pair v5.2B branch remains a candidate mechanism, not the current visual baseline.
