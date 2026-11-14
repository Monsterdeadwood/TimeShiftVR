# TimeShift VR — project status

[← Project page](../README.md) · [Flat2VR testing & discussion](https://discord.gg/P4q9zt7ek)

Reviewed **14 November 2026**. Documented branch: **R65a community package / R66 precision candidate**.

## What has been checked

- Native-game/XR Sim checks cover posture, recenter, selected video transitions and nine-weapon firing in the recorded revisions.

## Current limits

- Physical-headset comfort and full-campaign Roomscale coverage remain open; low ceilings, ladders and platforms need broader playtesting.
- Compatibility is tied to the package’s supported EXE identities; support for every Steam/retail executable is not established.

## Separate experimental work

- R66 tests tracked primary-fire precision while retaining the shotgun pellet cone. It is a distinct experimental candidate; precision_aim=false restores the original accuracy model.

## Build access

Ask for the current complete test package in the game’s Flat2VR thread. A local build record does not by itself mean a file has been uploaded to this repository’s Releases.

## Documentation basis

This overview was reconciled against the project’s recorded package notes and validation records. The following names identify the records reviewed; they are not download links:

- `TimeShiftVR_R65a_OpenXR_LauncherFix_20261112`
- `TimeShiftVR_R66_NativePrecision_20261112/README_EN.txt`
- `R66 TEST_RECEIPT.json / KNOWN_ISSUES.txt`

Game execution, simulator validation and physical-headset feedback are reported separately above. Features from a separate experimental branch are identified explicitly.

## Кратко по-русски

TimeShift в VR: оружие от контроллеров, управление временем, поддержка второй рукой и меню VR-настроек. Можно играть сидя или включить Roomscale для приседания движением шлема через родную систему поз.

- Комфорт в физическом шлеме и Roomscale во всей кампании ещё проверяются; низкие потолки, лестницы и платформы требуют более широких тестов.
- Совместимость привязана к поддерживаемым EXE сборки; работа со всеми Steam/retail-версиями не установлена.
