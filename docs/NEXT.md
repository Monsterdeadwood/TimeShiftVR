# TimeShiftVR — NEXT

Updated: 2026-08-25 22:54 +03

## Current serial gate — v5.3 projection identity recovery

Canonical package:
`TIMESHIFTVR_PROJECTION_IDENTITY_RECOVERY_v5.3.0_30S_ONECLICK.zip`

The old facade-slot13 COLD bridge is no longer the active project gate. True same-frame OpenXR stereo already exists. The immediate missing fact is whether the remaining fish-eye/crooked/tilted binocular image is caused by the two now-identified projection/eye-identity errors.

## Frozen baseline that must hold
From v4.7.2 and later stable transport runs:
- same-frame LEFT/RIGHT re-entry works.
- distinct live eye images reach OpenXR.
- OpenXR host publishes real stereo frames.
- no continuing stack/re-entry/matrix/readback failures are acceptable.

v5.3 must not regress this transport while fixing eye identity/projection.

## v5.3 exact changes
Only the projection/identity contract is being corrected:
1. remove host-side LEFT/RIGHT image payload swap;
2. keep each game eye bound to its own physical `XrView` pose and FOV;
3. use row-vector RH off-axis coefficients:
   - X: `(l+r)/(r-l)`;
   - Y: `(u+d)/(u-d)`;
4. retain ROW_VIEW_CORRECTED orientation and BODY_PLUS_HMD camera lock;
5. remove active shadow mutation;
6. remove main-world-only/Z-reflection surgery;
7. capture the real final game backbuffer once before desktop SBS overwrite;
8. rank D3D9 draws after `RETURN_RIGHT` passively.

Static audit: **31 / 31 checks PASS**.

## Run contract
Focused runtime window: **30 seconds after true stereo starts**.

During this run:
- do not press F2/F3/F5;
- F8 recenter is allowed if needed;
- do not add a second intrusive capture DLL;
- let the built-in passive D3D9/XR evidence collector finish and restore the baseline automatically.

## v5.3 visual PASS
All of the following should hold:
- LEFT/RIGHT remain live and distinct;
- binocular geometry no longer has the v5.2 fish-eye/crooked character attributable to eye identity/sign errors;
- head yaw/pitch/roll is coherent enough to continue owner work;
- no catastrophic black wedges / eye desync regression;
- same-frame stereo transport stays intact.

Shadows are **not required** for projection PASS. Shadow repair is a separate downstream gate.

## v5.3 structural PASS
Automatic result should show:
- true stereo starts;
- same-frame pair counter grows;
- zero or bounded/understood stack/re-entry/matrix failures;
- XR publication/readback remains healthy;
- LEFT image remains LEFT through submission and RIGHT remains RIGHT;
- final backbuffer capture is present;
- passive post-`RETURN_RIGHT` draw ranking is populated.

## If v5.3 VISUAL + STRUCTURAL PASS
Freeze projection identity as the new baseline.

Then the next missing fact becomes:

`where does the final lighting/shadow/color contribution get consumed or composed after RETURN_RIGHT?`

Use the passive v5.3 evidence first:
- final pre-SBS backbuffer;
- ranked draws after `RETURN_RIGHT`;
- render-target/texture/state history;
- exact shader context.

Do **not** immediately repeat the old one-texture mirror.

A later shadow repair may reuse the **safe exact-pair** idea from `TIMESHIFTVR_SAFE_PAIR_REPAIR_v5_2_0`, but only after the final-light/final-color owner is identified.

## If v5.3 STRUCTURAL PASS but VISUAL FAIL
Projection/camera convention remains the blocker.

Next experiment must be one smaller causal probe against the remaining convention, not a new shadow or hand/controller feature.

Candidates should be chosen only from evidence produced by v5.3. Do not resurrect broad camera rewrites.

## If v5.3 STRUCTURAL FAIL
Stop and repair the transport/build/runtime failure while preserving the v4.7.2 baseline contract. Do not interpret headset appearance from a structurally invalid run.

## Parallel branch — preserve, do not promote yet
`TIMESHIFTVR_SAFE_PAIR_REPAIR_v5_2_0`

Useful proven design facts:
- 256/256 analyzed pairs had equal LEFT/RIGHT DIP counts.
- 26028/26028 sampled LEFT shadow-bound draws had an exact RIGHT draw at the same DIP ordinal with matching draw signature.
- repair is draw-ordinal/signature based, not per-shader last-texture based.

Status: **HOLD pending v5.3 projection verdict.**

## Explicitly not next
Do not:
- restore v5.1 high-level `view+0x40` mutation;
- restore v5.1 per-shader texture replay;
- repeat the v5.2 simple exact shadow-depth mirror as the whole shadow solution;
- force Z reflection;
- swap only image payloads at the XR host;
- reopen broad SDC/Ghidra archaeology;
- start controller/hand integration before projection and final-light ownership are stable.
