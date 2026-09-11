# TimeShiftVR — RESULT / PACKAGE MANIFEST

Updated: 2026-09-12 +03

Purpose: make exact evidence identity recoverable without relying on ChatGPT conversation memory. A row being listed here does **not** mean the binary bytes are stored in GitHub. `BYTE_STATUS` is authoritative for that distinction.

## Current frontier artifacts

| Artifact | Class | SHA256 | Bytes | Evidence status | BYTE_STATUS |
| --- | --- | --- | ---: | --- | --- |
| `TIMESHIFTVR_VIEW_FX_OWNER_COLD_RESULT_20260910_032138.zip` | exact-retail RESULT | `3f67af95e23d463084082d6636a82ffa3fa2871a56633ba48be973f4411f3203` | 179830 | executed COLD, baseline preserved; falsifies `+0x9C = membership owner` | EXTERNAL_REQUIRED |
| `TIMESHIFTVR_VIEW_FX_OWNER_COLD_V631_RESULT_20260910_040445.zip` | exact-retail RESULT | `a18c0d88604b261285a8cd04856149ebb0d98bdbd50701e0faf9b5515f56e553` | 792700 | executed COLD; expanded ABI/inner-dispatch/anchor harvest; semantic owner unresolved | EXTERNAL_REQUIRED |
| `TIMESHIFTVR_VIEW_FX_OWNER_COLD_v6_3_0_20260909.zip` | source package | `af2082450b4b1cfd8055b27bf9a77bef035c81d645fc61820f2dfb3c272fc982` | 22486 | collector source lineage for v6.3.0 | EXTERNAL_REQUIRED |
| `TIMESHIFTVR_VIEW_FX_OWNER_COLD_v6_3_1_20260910.zip` | source package | `f33e07e98e1fee12c93a3b0f3e89920c73216ee279e981e750e6153d79f91803` | 28150 | corrected collector source with forced entries/ABI/inner-pass harvest | EXTERNAL_REQUIRED |

`EXTERNAL_REQUIRED` means the exact bytes were available in the preserved user artifact library at sync time but are not represented by a normal Git blob in this repository. Recovery is incomplete until those bytes are copied to an independent durable evidence store or otherwise made retrievable by immutable identifier.

## Older canonical artifact identities already preserved by the evidence vault

| Artifact | SHA256 | Bytes | Role |
| --- | --- | ---: | --- |
| `TIMESHIFTVR_XR_TRUE_STEREO_HMD_MVP_v5_1_1_RESULT_20260825_223246.zip` | `896952fa47de3489f4517d4bf49db9811c3ce344913c38ffa8be9188beffed44` | 37375828 | historical true-stereo runtime evidence |
| `TIMESHIFTVR_CAUSAL_ROLLBACK_SHADOW_BIND_RESULT_20260825_221925.zip` | `f0936e113256b22a5b97114130ed1efb4583417fa1d39efb8f85a55ee4637f57` | 20317457 | causal shadow-bind evidence |
| `TIMESHIFTVR_SAFE_PAIR_REPAIR_v5_2_0.zip` | `aad92e5d76c6d1a5665398aacee36e13bf8061f218966f6610d0f5e8490311c1` | 68711 | source/package lineage |
| `TIMESHIFTVR_PROJECTION_IDENTITY_RECOVERY_v5.3.0_30S_ONECLICK.zip` | `d247be9b3b27b1477d3870b6bc2615c87051d1ab6078f55de6acc99c190f5769` | 51435 | projection/physical-eye package lineage |

See `docs/EVIDENCE_LEDGER_20260827.md` and `docs/RUNTIME_LINEAGE_20260825.md` for historical interpretation. Those documents remain subordinate to newer exact-target RESULT/STATE/HANDOFF evidence.

## Frozen target identity

- GOG TimeShift 1.02 x86 retail SHA256: `78ac1602411b39ab31f22203eb45df0236c35e8b1c59e33fabc969b617953613`.
- CPU-fixed startup donor SHA256: `49bcca23d3d7872fbb578183b77472b64ecd8e3f8d68bfcccb1af6f04d4d8ed6`.

## Evidence precedence

```text
newer exact-target RESULT + exact source identity
> validated HANDOFF / STATE promotion
> older canonical project documents
> donor/beta/source inference
> generic memory/chat recollection
```

## Disaster-recovery requirement

A future recovery is considered byte-complete only when every `PROVEN_EXACT_TARGET` claim can be traced to:
1. exact artifact filename;
2. SHA256;
3. target identity;
4. source/package identity when applicable;
5. accessible immutable bytes or an independently backed-up location;
6. promotion document explaining what was and was not proven.

Do not silently convert `EXTERNAL_REQUIRED` into `IN_GIT` or `AVAILABLE` without verifying the exact SHA256 bytes.
