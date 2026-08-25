# TimeShiftVR — Runtime Lineage 2026-08-25

Purpose: preserve the exact runtime branch history separately from the older COLD renderer archaeology.

## Evidence labels
- **AUTO PROVEN** — measured by runtime logs/counters/artifacts.
- **USER OBSERVED** — headset/monitor visual report from the human tester.
- **STATIC READY** — source/package audit passed, but no runtime visual verdict yet.
- **REJECT** — causal or visual result says not to reuse the strategy.
- **HOLD** — technically useful branch preserved but not the canonical next run.

## v4.7.2 — true OpenXR stereo MVP
Status: **KEEP / frozen transport baseline**.

### AUTO PROVEN
- 5858 completed same-frame stereo pairs.
- 41006 / 41006 LEFT/RIGHT uploads.
- 3197 OpenXR frames.
- Quest IPD around 63.63 mm.
- asymmetric physical per-eye FOV available.
- same-frame RIGHT re-entry works.

### USER OBSERVED
- real binocular stereo/depth exists.
- HMD yaw/roll convention was wrong/reversed.
- shadows absent in the duplicated eye path.

### Decision
Keep transport/scheduler. Fix orientation and rendering state around it. Do not redesign stereo from scratch.

---

## v4.9.x — corrected row-view + total D3D9/XR census
Status: **KEEP as diagnostic working line**.

### Added
- `ROW_VIEW_CORRECTED` HMD orientation logic.
- `BODY_PLUS_HMD` camera behavior.
- D3D9 RT/resource/texture/shader/state census.
- XR input/controller census.
- adaptive stack cleanup calibration.
- gameplay-view signal.
- automatic retail/CPU-fix restoration.

### Decision
Use this as the rollback base for later causal repairs.

---

## v5.0.0 — shadow resource asymmetry
Status: **AUTO PROVEN**.

### Evidence
Exact native shadow resource isolated:
- 1024×2048.
- D16 depth texture.
- native binds: 3817.
- LEFT stereo binds: 256.
- RIGHT stereo binds: 0.
- RIGHT shadow-consuming draws still occur.

### Decision
There is real LEFT/RIGHT state asymmetry. A targeted repair is justified, but causality still requires a controlled intervention.

---

## v5.1.0 — initial repair delivery
Status: **TOOL BUILD FAIL / NO VERDICT**.

### Failure
Compile-order problem around `write_phase_file` declaration.

### Decision
No VR inference. Hotfix only the build issue.

---

## v5.1.1 — high-level camera-source + learned shadow-state repair
Result:
`TIMESHIFTVR_XR_TRUE_STEREO_HMD_MVP_v5_1_1_RESULT_20260825_223246.zip`

SHA256:
`896952fa47de3489f4517d4bf49db9811c3ce344913c38ffa8be9188beffed44`

Status: **AUTO TRANSPORT PASS / USER VISUAL REJECT**.

### AUTO PROVEN
- 3317 same-frame pairs.
- 40242 gameplay view-source repair writes.
- 537488 RIGHT shadow-state repair draws.
- 183 learned shadow consumer shader pairs.
- 23219 LEFT eye uploads.
- 23219 RIGHT eye uploads.
- camera source latch armed.
- D16 shadow texture identified.
- retail baseline restored.

### USER OBSERVED
- camera/tilt became very wrong.
- black wedges appeared.
- eyes desynchronized.

### Postmortem
The branch combined two unsafe ideas:
1. mutate high-level gameplay `view+0x40` before engine ownership is fully separated;
2. learn one shadow texture tuple per shader pair and replay it into RIGHT.

Raw corpus disproved the second identity assumption: a sampled VS/PS pair used **six different stage-1 textures**.

### Decision
**REJECT** high-level camera-source freezing and per-shader last-texture replay.

---

## Exact-pair draw correspondence harvested from v5.1.1 corpus
Status: **AUTO PROVEN structural relation**.

First 256 stereo pairs:
- LEFT DIP count == RIGHT DIP count in 256/256 pairs.
- 26028/26028 sampled LEFT shadow-bound DIP draws had an exact RIGHT partner at the same DIP ordinal.
- matching fields: primitive data, geometry indices, VS, PS.

### Decision
If state replay is needed later, exact draw ordinal + signature is a valid candidate key and is much safer than per-shader learning.

---

## v5.2A — causal rollback + exact shadow-depth bind
Result:
`TIMESHIFTVR_CAUSAL_ROLLBACK_SHADOW_BIND_RESULT_20260825_221925.zip`

SHA256:
`f0936e113256b22a5b97114130ed1efb4583417fa1d39efb8f85a55ee4637f57`

Status: **INTERVENTION EXECUTED / VISUAL FIX FAIL**.

### Intervention
- rollback v5.1 camera-source surgery.
- rollback main-world-only owner split.
- rollback forced Z reflection.
- restore v4.9/v5.0 BODY_PLUS_HMD + ROW_VIEW_CORRECTED behavior.
- keep same-frame stereo.
- mirror only the exact 1024×2048 shadow-depth bind after LEFT proves the exact consumer pair.

### AUTO PROVEN
- exact depth captures: 1.
- LEFT exact binds: 1398.
- RIGHT same-pair mirrored binds: 1398.
- mirror failures: 0.
- same-frame pairs: 2172.
- stack failures: 0.
- re-entry failures: 0.
- matrix-contract failures: 0.
- XR-published pairs: 2169.
- XR readback failures: 0.
- retail EXE preserved; temporary CPU-fix removed.

### USER OBSERVED
- fish-eye / crooked camera.
- strong tilt.
- shadows still absent.

### Decision
The exact resource asymmetry is real and the mirror definitely executed, but **this one bind is not the complete visible shadow fix**. Close that hypothesis.

---

## v5.2B — SAFE PAIR REPAIR sibling branch
Package:
`TIMESHIFTVR_SAFE_PAIR_REPAIR_v5_2_0.zip`

SHA256:
`aad92e5d76c6d1a5665398aacee36e13bf8061f218966f6610d0f5e8490311c1`

Status: **HOLD**.

### Design
- no high-level camera-source mutation.
- writer watch arms extant TimeShift threads to locate real mouse/body writes.
- LEFT state captured by actual DIP ordinal.
- RIGHT repair only on exact draw-signature match.
- exact LEFT stage0 + stage1 state can be replayed only for that matching draw.

### Why HOLD
This branch was generated from the v5.1.1 corpus and fixes its state-identity bug, but v5.2A exposed a larger projection/physical-eye problem. Shadow visuals cannot be judged cleanly until projection identity is corrected.

### Decision
Preserve the branch. Do not promote it over v5.3.

---

## Projection/physical-eye contract audit after v5.2A
Status: **STATIC DEFECT FOUND**.

Two concrete bugs:
1. host-side image payload swapping could pair game LEFT imagery with physical RIGHT pose/FOV and vice versa;
2. row-vector RH off-axis coefficient denominator signs were mirrored incorrectly.

Correct formulas for current convention:
- X offset: `(l+r)/(r-l)`.
- Y offset: `(u+d)/(u-d)`.

### Decision
Projection identity must be fixed before more lighting mutation.

---

## v5.3.0 — projection identity recovery
Package:
`TIMESHIFTVR_PROJECTION_IDENTITY_RECOVERY_v5.3.0_30S_ONECLICK.zip`

SHA256:
`d247be9b3b27b1477d3870b6bc2615c87051d1ab6078f55de6acc99c190f5769`

Status: **STATIC READY / CURRENT CANONICAL NEXT LIVE**.

### Static audit
31 checks PASS.

### Frozen behavior
- same-frame RIGHT re-entry/return retained.
- pair counter retained.
- ROW_VIEW_CORRECTED retained.
- BODY_PLUS_HMD retained.

### Removed
- host image-only eye swap.
- old off-axis sign formulas.
- main-world-only owner surgery.
- forced Z reflection.
- active RIGHT shadow texture mirror.
- Windows mouse injection path.
- F2/F3/F5 live toggles for this focused run.

### Added / retained passive evidence
- one-shot real final backbuffer capture before desktop SBS overwrite.
- passive D3D9 ranking after `RETURN_RIGHT`.
- projection/final-color analyzer.
- exact baseline/hash guards and restore path.
- 30-second focused capture.

### Run rule
Load gameplay. Let true stereo start. Do not press F2/F3/F5. F8 recenter is allowed.

### PASS
- physical LEFT/RIGHT identity remains correct end-to-end.
- no projection-induced fish-eye/crooked binocular geometry.
- HMD yaw/pitch/roll coherent enough for continued integration.
- live distinct same-frame stereo remains healthy.

Shadows are not required for this PASS.

### If PASS but shadows still absent
Next target:
`post-RETURN_RIGHT final-light/final-color composition owner`

Use v5.3 passive evidence first. Only then decide whether the exact-pair state mechanism from v5.2B is useful at that later boundary.

### If FAIL
Do not mutate shadows. Diagnose the remaining camera/projection convention with one smaller causal test.

---

# Canonical ordering

`COLD renderer facts`

`-> v4.7.2 true stereo KEEP`

`-> v4.9 instrumentation/orientation KEEP`

`-> v5.0 shadow asymmetry PROVEN`

`-> v5.1 broad repair REJECT`

`-> v5.2A exact shadow bind EXECUTED / visible fix FAIL`

`-> projection identity defect FOUND`

`-> v5.3 CURRENT NEXT LIVE`

Parallel:
`v5.2B safe-pair mechanism = HOLD candidate`

# Non-negotiable lesson
A healthy RESULT ZIP can prove that code executed perfectly while the headset image is still wrong. Structural telemetry and human visual verdict must remain separate fields in every future TimeShiftVR result.
