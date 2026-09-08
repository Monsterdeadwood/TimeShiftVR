# TimeShiftVR — Canonical State

Updated: 2026-09-08 +03

## Status
**ACTIVE. True same-frame OpenXR stereo remains proven. The current missing-FX gate is native late-transaction ownership, not another texture replay or the old OMNI v6.1 ranking pass.**

Canonical active claim:
`TS-FX-PASS-OWNER`

## Frozen target
- Game: GOG TimeShift 1.02 x86.
- Retail SHA256: `78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613`.
- Corpus root: `C:\GOG Games\TimeShift1`.
- CPU-fixed startup donor SHA256: `49bcca23d3d7872fbb578183b77472b64ecd8e3f8d68bfcccb1af6f04d4d8ed6`.

## Protected working baseline
### v4.7.2 OLD-GOOD true stereo
Retain without reopening absent contradictory exact evidence:
- 5858 completed same-frame LEFT/RIGHT pairs;
- 41006 / 41006 eye uploads;
- 3197 OpenXR frames;
- physical Quest IPD / asymmetric per-eye FOV;
- real binocular content reaches the headset.

Current-best effect-state behavior remains:
`OLD-GOOD + DIP exact TEX0+TEX1`.

The controlled v6.13 sweep retained this conclusion:
- DP exact and DP resync modes damage lighting;
- wider DIP/DP/resync/TEX0..3/shadow-state modes did not materially recover the missing FX.

Therefore generic replay widening remains saturated.

## Historical COLD foundation retained
The 2026-08-27 corpus closure remains useful for shader/GLT/RTTI candidate generation:
- PAIRS 9180 / 374 unique parsed SHA;
- canonical GLT 192-slot schema;
- 109 retail descriptor assignments / 109 slot-index agreements;
- 375 SDC files / 198 unique SHA;
- 203984 compiled D3D9 shader blobs in the v5 OMNI closure;
- 134 exact donor CRC matches;
- 900 RTTI method rows / 485 owner-ranking rows.

Those maps are candidate infrastructure. They are no longer the project serial gate.

## v6.1 OMNI disposition
`TIMESHIFTVR_OMNI_EXACT_CLOSURE_v6.1.0` is **not the next executable/analyzer gate**.

Later source audit found the AS-IS implementation scientifically unsafe as a canonical verdict source, including unconditional PASS reporting, raw-byte RET function slicing, weak direct-COM displacement heuristics, incomplete GLT-tail semantics and insufficient exact-target/result discipline.

Disposition:
- preserve valid SDC parsing ideas;
- reuse later decoded-function/Ghidra lineage where needed;
- **do not run or promote v6.1 AS-IS**;
- do not invent another generic OMNI analyzer to replace it.

## Exact render-transaction convergence
### `0x0067F4F0` is INNER_DONE, not EYE_DONE
Preserved exact-target runtime/static convergence establishes:
- synthetic stereo executes the exact inner renderer `0x0067F4F0` for LEFT and RIGHT;
- native parent `0x0067F100` contains work after the inner renderer;
- its natural post-inner region includes stage10, vcall `+0x78`, vcall `+0x9C(View)`, and vcall `+0x7C = 0x00680EF0` before later frame completion;
- `0x006E6220` sits on producer-side shadow/light preparation and must not be blindly duplicated.

Recovered vtable anchors:
- base `0x00D8D810`;
- `+0x2C -> 0x0067F4F0`;
- `+0x78` cell `0x00D8D888`;
- `+0x9C` cell `0x00D8D8AC`;
- `+0x7C -> 0x00680EF0`.

### Native late tail after RIGHT return
Preserved v6.13 execution lineage:
- `RIGHT_RETURNS = 10455`;
- `10455 / 10455` RIGHT returns are followed in the same frame by native `0x00680EF0` view/update activity and then `425BF981 / 6FDF4543` final fullscreen work;
- in `10454 / 10455` stereo-return frames that final draw is the last D3D9 draw of the frame; the formal exception is multi-pair accounting;
- representative post-RIGHT tail: `2 rain + 14 overlay/HUD + 1 final fullscreen` draws.

The earlier model `0x0067F4F0 RET = EYE_DONE` is therefore rejected.

### Final color is a later transaction stage
Stereo counters in the preserved execution line:
```text
425 / 09AF:
  eye0 = 64
  eye1 = 10455
  eye2 = 10455

425 / 6FDF:
  eye0 = 10519
  eye1 = 0
  eye2 = 0

10519 = 64 baseline + 10455 stereo pairs
```

`09AF` and `6FDF` are not alternative eye shaders at one semantic branch. Native ordering is instead:
```text
inner/intermediate 425/09AF
  -> late rain/overlay/distortion/effect work
  -> final 425/6FDF
  -> output
```

Canonical ledger term:
`FINAL_COLOR_TRANSACTION_OWNERSHIP_DIVERGENCE`.

### Current wrapper drops eye ownership before native finalization
Current sequence:
```text
RIGHT 0x0067F4F0
  -> RETURN_RIGHT
  -> eye_phase = 0
  -> stereo_active = 0
  -> real backbuffer
  -> native late view / FX
  -> final 425/6FDF
```

Immediately before the final fullscreen draw, Saber requests the real backbuffer at caller RVA `0x0039C4F6`.

The existing SetRenderTarget hook already supports:
```text
stereo_active && requested == real_backbuffer:
  eye1 -> private LEFT RT
  eye2 -> private RIGHT RT
```

For the preserved run, the actual private surfaces were:
- LEFT `0x01502FC0`;
- RIGHT `0x01502A20`;
- BACK `0x01502480`.

Older `0x0FC861A0 / 0x0FC86620` observations are Saber-internal surfaces, not private VR eye RT identity. Do not use them as proof that final `6FDF` consumes the LEFT VR eye.

## Independent older RESULT support
`TIMESHIFTVR_PROJECTION_IDENTITY_RECOVERY_RESULT_20260826_002808.zip` independently records the same boundary:
- 3234 completed RIGHT returns;
- exactly 3234 post-RIGHT `425BF981 / 6FDF4543` fullscreen draws;
- final fullscreen targets the real backbuffer rather than the private eye targets;
- `FINAL_BACKBUFFER_BEFORE_SBS.bmp` visibly contains strong rain/final-lighting/fullscreen composition absent from `LEFT_EYE.bmp` and `RIGHT_EYE.bmp`.

This supports a transaction-boundary problem rather than an XR readback problem.

## Orthogonal shadow/light cache defect
Do not collapse this with late final-color ownership.

The exact-retail shadow activation chain around `0x006E6220 -> 0x006EB650 -> 0x006EBB40 -> 0x007C7000 -> 0x007C7470` includes a generation/lastApplied cache gate at state `+0x470/+0x474`.

A preserved one-shot `TS-LIVE-005-RIGHT-LIGHT-CACHE-REARM` causal result mechanically restored the native RIGHT bind -> 102 draws -> cleanup transaction for one selected pair. That is structural proof of a local cache defect, **not** a sustained visual fix and not a universal explanation for missing rain/final composition.

## FALSIFIED / do not repeat
- broad v5.1 `view+0x40` camera mutation;
- per-shader last-LEFT-texture replay;
- simple D16 mirror as complete visible shadow fix;
- DP-only exact/resync FX replay;
- wider generic DIP/DP/TEX/state replay without a new owner;
- `09AF vs 6FDF` as a simple shader-choice branch;
- `0x003C7975` as established semantic owner merely because both stages pass through it;
- `0x0067F4F0 RET = EYE_DONE`;
- blind repeat of producer-side `0x006E6220`;
- whole `0x0067F100 x2` as the first repair;
- manual `6FDF` replay as the primary repair;
- old internal-surface pointer equality as private VR-eye identity.

# Current gate — EYE_DONE / final-color transaction ownership
`TS-FX-PASS-OWNER` remains ACTIVE; no new duplicate claim is created.

Current leading model:
> the stereo wrapper duplicates the inner render correctly but releases RIGHT eye ownership before Saber's natural late finalization completes.

R3 branch-local convergence shadow:
`cold/r3/latefx-ownership:docs/COLD/R3_EYE_DONE_TRANSACTION_SYNC_20260908.md`.

## STILL UNKNOWN
1. Exact physical/native EYE_DONE boundary after `0x0067F4F0`, especially whether `0x00680EF0` return is still earlier than the final rain/overlay/6FDF tail.
2. Exact semantics/ownership of `+0x78`, `+0x9C(View)`, and their FX queue/list/membership dependencies.
3. Whether `0x007C1780` replays an immutable list or destructively drains a queue; this matters before any future design duplicates late-tail execution.
4. Whether keeping RIGHT ownership alive through the one already-existing natural tail is sufficient to route final output into the private RIGHT RT without destroying required state.
5. If that causal discriminator later passes, which minimum tail subset must eventually become per-eye so LEFT and RIGHT both receive complete late composition.
6. Sustained visual consequence of the separately proven one-shot shadow-cache rearm.

## Current execution status
`LIVE = DENIED`
`VALID_FRESH_LIVE_TICKET = NONE`

No new BAT/DLL/build is authorized by this state convergence. Continue COLD boundary/queue ownership and hand any future one-mutation execution to the incumbent implementation owner.

## STOP RULE
- do not run v6.1 AS-IS;
- do not create another generic pass-ranking analyzer;
- do not repeat generic texture/state replay;
- do not duplicate producer-side shadow preparation;
- do not duplicate the late tail until queue/temporal ownership is classified;
- do not treat the unexecuted `DELAY_RIGHT_TEARDOWN_ONLY` discriminator as PASS or FAIL;
- do not create a LIVE from R3 without a fresh sibling implementation ticket and the mandatory five-line causal gate.
