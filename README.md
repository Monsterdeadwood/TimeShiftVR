# TimeShiftVR

Native VR integration research for **TimeShift / Saber3D**.

## Current status
**ACTIVE — TRUE SAME-FRAME OPENXR STEREO IS PROVEN; PROJECTION IDENTITY RECOVERY v5.3 IS THE NEXT CANONICAL LIVE GATE.**

The project is no longer blocked on generic shader/cache or camera-facade archaeology. Those layers remain valuable proven evidence, but the working line has advanced into a real D3D9 -> x64 OpenXR stereo path with same-frame LEFT/RIGHT re-entry, HMD pose, per-eye FOV and live headset submission.

Frozen local corpus:
`C:\GOG Games\TimeShift1`

Shared research tools:
`C:\GOG Games\VR Research Tools`

## Frozen retail target
- GOG TimeShift 1.02 x86.
- Retail SHA256: `78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613`.
- CPU-fixed startup donor SHA256: `49bcca23d3d7872fbb578183b77472b64ecd8e3f8d68bfcccb1af6f04d4d8ed6`.
- The runner temporarily stages the exact CPU-fixed donor when required and restores the retail EXE automatically.

## Proven foundation
The older COLD work is retained and still authoritative:
- 120 `.sdc`, 5040 `*_pairs` = 8 profiles × 42 scenes × 15 passes.
- Full SDC structure/decompression and GLT 192-bit define-mask mapping.
- COLD shader bytecode identity matches LIVE D3D9 shader creation.
- Retail VS constant path: `0x007C3540 cached setter -> 0x007C3970 flusher -> D3D9`.
- c0-c3 are combined ViewProjection/world-to-clip; c4 is camera world position.
- Backend `d3dREND_DRIVER` and its matrix/upload lane are mapped.
- The anonymous camera facade is separate from backend `d3dREND_DRIVER`.

These are no longer the active serial gate.

## Runtime breakthrough
### v4.7.2 — frozen true-stereo core
The true OpenXR MVP established a stable same-frame transport:
- **5858** completed same-frame LEFT/RIGHT pairs.
- **41006 / 41006** LEFT/RIGHT eye uploads.
- **3197** OpenXR frames.
- Quest IPD observed around **63.63 mm** with asymmetric per-eye FOV.
- Stack/re-entry/matrix transport remained stable.

The user confirmed that real binocular stereo existed, but HMD orientation still had convention problems and shadows were absent in the duplicated eye path.

### v5.0 — shadow asymmetry isolated
Live D3D9 evidence identified the native **1024×2048 D16 shadow texture**. In the measured lane it was bound in native/LEFT execution but not rebound for RIGHT even though shadow-consuming draws existed in both eyes. This converted “missing RIGHT-eye shadows” from a vague rendering symptom into a finite state-ownership problem.

### v5.1.1 — transport PASS, repair strategy REJECT
The v5.1 camera/source + broad per-shader shadow repair completed **3317** same-frame pairs with transport intact, but its repair layer was too invasive:
- **40,242** high-level gameplay view-source writes.
- **537,488** RIGHT-eye shadow-state overrides.
- **183** learned shadow consumer shader pairs.

The user visually rejected the result: camera/tilt became badly wrong, black wedges appeared and the eyes desynchronized. Raw evidence also showed one VS/PS pair can use multiple different stage-1 textures, so replaying the last LEFT texture per shader pair is invalid.

### v5.2 causal rollback — exact shadow bind executed, visual hypothesis failed
The bad v5.1 camera/Z surgery was rolled back. A much narrower intervention mirrored only the exact proven 1024×2048 shadow-depth bind for the exact consumer pair:
- **1398 LEFT exact binds -> 1398 RIGHT mirrored binds**.
- **0** mirror failures.
- **2172** same-frame pairs.
- **0** stack, re-entry or matrix-contract failures.
- **2169** XR-published pairs.

The user still saw a fish-eye/crooked camera with strong tilt and **no restored shadows**. Therefore the simple missing-shadow-texture-bind hypothesis is closed as a visible fix.

## Current canonical gate — v5.3 projection identity recovery
`TIMESHIFTVR_PROJECTION_IDENTITY_RECOVERY_v5.3.0_30S_ONECLICK`

Static preflight passes 31 checks. This build removes two concrete eye/projection contract errors found after v5.2:
- no host-side LEFT/RIGHT image payload swap; physical image + XrView pose + XrFovf stay together end-to-end;
- row-vector RH off-axis coefficients use `(l+r)/(r-l)` and `(u+d)/(u-d)`.

It also keeps the failed mutations out:
- no main-world-only owner split;
- no forced Z reflection;
- no active shadow/resource mutation;
- no HMD-to-Windows-mouse injection.

The focused capture lasts 30 seconds after true stereo begins and passively captures the real final backbuffer before the desktop SBS overwrite. Draws after `RETURN_RIGHT` are ranked to locate the later final-light/final-color boundary if shadows remain missing.

## Parallel branch on hold
`TIMESHIFTVR_SAFE_PAIR_REPAIR_v5_2_0` is a later generated repair branch derived from the v5.1.1 corpus. It correctly replaces unsafe per-shader texture learning with exact LEFT/RIGHT **DIP ordinal + draw-signature matching**. It is useful evidence and should be preserved, but it is **not the canonical next visual test until v5.3 projection identity is judged**, because projection errors can poison any shadow visual verdict.

## Working discipline
`WORKING BUILD FIRST`

`REVERSE ONLY BLOCKERS`

`ONE MISSING FACT -> ONE TEST -> ONE VERDICT`

`PARALLELIZE EVIDENCE -> SERIALIZE MUTATION`

`VISUAL HEADSET VERDICT != AUTOMATIC STRUCTURAL PASS`

Do not reopen broad reverse engineering while a narrower runtime causal gate exists.

## Start here
1. `docs/STATE.md` — active canonical state.
2. `docs/PROVEN.md` — facts that must not be rediscovered.
3. `docs/FALSIFIED.md` — closed wrong paths and rejected repairs.
4. `docs/NEXT.md` — current serial gate and pass/fail routing.
5. `docs/SYNC.md` — synchronization and tool lineage.
6. `docs/RUNTIME_LINEAGE_20260825.md` — v4.7.2 -> v5.3 runtime evidence ledger.
