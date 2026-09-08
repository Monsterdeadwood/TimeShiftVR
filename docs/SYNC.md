# TimeShiftVR — SYNC

Updated: 2026-09-08 +03

Repository: `Monsterdeadwood/TimeShiftVR`
Active claim: `TS-FX-PASS-OWNER`
Current gate: `EYE_DONE / final-color transaction ownership`

## Frozen target
- GOG TimeShift 1.02 x86.
- Retail SHA256 `78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613`.
- CPU-fixed donor SHA256 `49bcca23d3d7872fbb578183b77472b64ecd8e3f8d68bfcccb1af6f04d4d8ed6`.

## Protected runtime baseline
`v4.7.2 OLD-GOOD` remains authoritative for working same-frame OpenXR stereo:
- 5858 completed LEFT/RIGHT pairs;
- 41006 / 41006 uploads;
- 3197 XR frames;
- physical per-eye pose/FOV behavior;
- real binocular headset content.

Current-best effect state remains `OLD-GOOD + DIP exact TEX0+TEX1`.

## Retained historical closures
Do not reopen without contradictory exact evidence:
- broad high-level View mutation rejected;
- per-shader last-LEFT-texture replay rejected;
- v5.2 exact D16 bind mirror executed but was visually insufficient;
- DP-only exact/resync modes damage lighting;
- wider generic DIP/DP/TEX/shadow-state replay produced no material recovery;
- host image-only eye swap / old projection-sign compensation rejected;
- View-stack foundation around `root+0x618`, slot0 `root+0x620`, and generic View copy `0x00956680` retained.

## 2026-09-08 convergence correction
The former canonical serial gate `TIMESHIFTVR_OMNI_EXACT_CLOSURE_v6.1.0` is stale.

Later preserved source audit established that v6.1 AS-IS is not an admissible scientific verdict source due unconditional PASS reporting, raw-byte function slicing, weak direct-COM owner heuristics and incomplete exact-tail semantics. Preserve useful SDC ideas only through corrected decoded-function lineage. Do not run v6.1 merely because an older document says `awaiting RESULT`.

## Current exact render-transaction model
Synthetic stereo duplicates the exact inner renderer `0x0067F4F0`.

Exact-retail parent/CFG evidence places additional native work after that inner call in `0x0067F100`, including:
```text
stage10
+0x78
+0x9C(View)
+0x7C = 0x00680EF0
```

Recovered vtable anchors:
```text
base 0x00D8D810
+0x2C -> 0x0067F4F0
+0x78 cell 0x00D8D888
+0x9C cell 0x00D8D8AC
+0x7C -> 0x00680EF0
```

Preserved v6.13 runtime lineage shows:
- 10455 / 10455 RIGHT returns are followed by native `0x00680EF0` and later `425BF981 / 6FDF4543` in the same frame;
- in 10454 / 10455 stereo-return frames that final draw is the last D3D9 draw, modulo one multi-pair accounting case;
- representative post-RIGHT tail = 2 rain + 14 overlay/HUD + 1 final fullscreen draw.

Therefore `0x0067F4F0 RET` is `INNER_DONE`, not established `EYE_DONE`.

## Final-color ownership correction
Preserved stereo counters:
```text
425 / 09AF:
  eye0 64
  eye1 10455
  eye2 10455

425 / 6FDF:
  eye0 10519
  eye1 0
  eye2 0
```

Native order places `09AF` before late FX and `6FDF` after them. The older `simple shader branch divergence` model is rejected.

Use:
`FINAL_COLOR_TRANSACTION_OWNERSHIP_DIVERGENCE`.

## Current premature-teardown fact pattern
At current RIGHT return, the stereo wrapper clears:
```text
eye_phase = 0
stereo_active = 0
RT = real backbuffer
```

Saber then continues native late work. Immediately before final `6FDF`, it requests the real backbuffer at caller RVA `0x0039C4F6`.

Existing SetRenderTarget routing already knows:
```text
stereo_active && requested == backbuffer:
  eye1 -> private LEFT RT
  eye2 -> private RIGHT RT
```

Actual private surfaces on the preserved run:
- LEFT `0x01502FC0`;
- RIGHT `0x01502A20`;
- BACK `0x01502480`.

Older `0x0FC861A0 / 0x0FC86620` values are Saber internal surfaces and are not private VR-eye identity.

## Independent older RESULT support
`TIMESHIFTVR_PROJECTION_IDENTITY_RECOVERY_RESULT_20260826_002808.zip` records 3234 completed RIGHT returns and exactly 3234 post-RIGHT final `425/6FDF` fullscreen draws to the real backbuffer. Its pre-SBS final backbuffer image contains strong rain/final composition missing from saved private eye images.

This independently supports a late transaction-boundary defect rather than XR readback failure.

## Orthogonal shadow/cache line
Exact-retail shadow/light producer/cache ownership around `0x006E6220 -> 0x006EB650 -> 0x006EBB40 -> 0x007C7000 -> 0x007C7470` remains a separate defect.

A preserved one-shot TS-LIVE-005 result mechanically restored a native RIGHT bind -> 102 draws -> cleanup transaction for one selected pair after one cache miss. That is not a sustained visual verdict and does not replace the EYE_DONE gate.

## Active R3 line
Branch: `cold/r3/latefx-ownership`
Shadow note: `docs/COLD/R3_EYE_DONE_TRANSACTION_SYNC_20260908.md`
Role: R3 structural red-team.

R3 owns:
- exact EYE_DONE boundary after `0x0067F4F0`;
- `+0x78 / +0x9C(View) / +0x7C` ownership;
- FX queue/list/membership lifetime;
- destructive-vs-reusable queue behavior before any future tail duplication.

R3 does not own a competing implementation build.

## Active R4 line
Branch: `cold/r4/sidecar-ownership`.
R4 remains separate and unbound. Do not collapse sidecar/replacement ownership into the current native Saber transaction question.

## Unexecuted causal candidate
`DELAY_RIGHT_TEARDOWN_ONLY` is a narrow future discriminator, not an accepted RESULT.

Its conceptual isolation is to preserve all native execution counts and change only whether the single already-existing natural late tail remains owned by RIGHT long enough for native backbuffer routing to reach the private RIGHT RT.

No accepted execution result exists for that canary.

## Current status
```text
COLD = CONTINUE
LIVE = DENIED
VALID_FRESH_LIVE_TICKET = NONE
```

## STOP RULE
- no v6.1 AS-IS;
- no new generic OMNI/pass-ranking analyzer;
- no repeat of same-frame stereo proof;
- no generic DIP/DP/TEX/state replay;
- no blind second `0x006E6220`;
- no whole `0x0067F100 x2` as first repair;
- no manual `6FDF` replay as primary repair;
- no late-tail duplication before queue/temporal ownership closure;
- no executable R3 LIVE without a fresh implementation-owner ticket and exactly five causal preflight lines.
