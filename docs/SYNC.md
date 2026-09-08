# TimeShiftVR — SYNC

Updated: 2026-09-08 +03

Repository: `Monsterdeadwood/TimeShiftVR`
Active claim: `TS-FX-PASS-OWNER`
Current R3 gate: `View* -> DAT_00FCACD8 +0x9C -> FX queue/list/membership -> consumer`

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

## Retained closures
Do not reopen without contradictory exact evidence:
- broad live main-View mutation rejected;
- generic last-LEFT texture replay rejected;
- exact D16 bind mirror visually insufficient as a complete fix;
- DP-only exact/resync damages lighting;
- wider generic DIP/DP/TEX/shadow-state replay gave no material recovery;
- literal native secondary/mirror semantics are not a valid XR RIGHT architecture;
- v6.1 AS-IS is not an admissible current verdict source.

## R3 exact structural model
`0x0067F4F0` is the proven inner renderer and accepts the high-level Saber `View*` as arg1. Synthetic RIGHT currently reuses LEFT/main `View*` while late backend matrices are made eye-specific.

`DAT_00FCACD8` is structurally tied to scene/render-list ownership:
```text
+0x8C object register/enter
+0x90 object unregister/leave
+0x28/+0x2C per-View path
MAIN mask = 1
secondary mask = 1 << ViewStackIndex
```

The same manager region owns objects carrying rain, distortion, shadow-map, mirror and light-related flags.

MAIN additionally performs:
```text
stage10
+0x78()
+0x9C(View)
+0x7C() = 0x00680EF0
```

Recovered vtable base: `0x00D8D810`.

## Current FIRST_MISSING_EDGE
```text
View*
  -> DAT_00FCACD8 +0x9C(View)
  -> FX queue/list/membership
  -> consumer
```

Required RIGHT semantic input: `rightView = 0x0067F4F0 arg1`.

UNKNOWN:
- exact `+0x78/+0x9C/+0x7C` semantics;
- concrete queue/list structures;
- whether membership is per-View/per-slot/shared;
- destructive-vs-reusable queue behavior;
- exact rain/distortion/light/final consumers.

## Borrowed sibling runtime evidence
The late EYE_DONE/final-color line remains valid evidence but is not the R3 primary owner.

Preserved facts include:
- native work continues after `0x0067F4F0`;
- current wrapper clears eye ownership before late rain/overlay/final work;
- final `425/6FDF` is eye0-only in preserved v6.13 lineage;
- older captures place strong final composition on the real backbuffer;
- `DELAY_RIGHT_TEARDOWN_ONLY` remains unexecuted.

Treat these as `BORROWED_EVIDENCE` under the cross-role law. They constrain where R3-owned queues are consumed but do not authorize an R3 runtime canary.

## Orthogonal shadow/cache line
Exact-retail shadow activation around `0x006EB650` has a generation/lastApplied cache gate. One-shot TS-LIVE-005 mechanically restored a native RIGHT bind -> 102 draws -> cleanup transaction. This stays structural evidence, not a universal missing-FX fix.

## Current status
```text
COLD = CONTINUE
LIVE = DENIED
VALID_FRESH_LIVE_TICKET = NONE
```

## STOP RULE
- no v6.1 AS-IS;
- no new generic OMNI/pass-ranking analyzer;
- no repeat of generic texture/state replay;
- no blind second `0x006E6220`;
- no native secondary bit for XR RIGHT;
- no whole `0x0067F100 x2` as first repair;
- no rightView LIVE before exact View convention + membership prep closure;
- no late-tail duplication before queue/temporal ownership closure;
- no promotion of sibling EYE_DONE/680EF0 runtime ownership into R3 without independent closure;
- no executable R3 LIVE without a fresh implementation-owner ticket and exactly five causal preflight lines.
