# MANIFEST-P2H — фаза 2, пакет P2-H: промоушн аудит-слоя supplement: `supplement/fixed_map/report-audit-20260919/` → `report-audit/`, `supplement/fixed_map/fixed-map-audit/` → `classical-conventions/`

**Источник:** живой main после пакета P2-G2: claims.json blob `6caca2fef44fc046225ae66a025c55e6183aebca` сверен с живым main коннектором при сборке настоящего пакета. Удаления P2-G2 (11 оригиналов `chat_20261011`) шли браузером параллельно и поверхностей этого пакета не касаются.
**Состав: 25 файлов, 2 каталога** — переименование на месте, на той же глубине (`supplement/fixed_map/<имя>/`), родитель и глубина сохранены. Содержимое всех 25 файлов не меняется байт-в-байт: SHA-256 и размеры в таблице — одновременно исходные и целевые. 23 текстовых файла переносит коннектор; 2 бинарных файла (отмечены ⚠) — браузерная загрузка сессией владельца с последующей blob-сверкой.

## Имена

- `report-audit-20260919/` → **`report-audit/`**. Основа имени — собственный предметный стем каталога: датированный суффикс был единственной аномалией. Содержание: аудит двух внешних исследовательских сводок от 19 сентября 2026 и продолженные вычисления — эталонная реализация CUE (`verify.py`, `cue_reference.md`), кубическая дисперсия, контроль сложенного спектра, монодромия. Таблица чтения `supplement/fixed_map/README.md` называет строку «Uploaded report audit».
- `fixed-map-audit/` → **`classical-conventions/`**. Старое имя дублировало имя родительского слоя и не описывало содержимое. Содержание: `classical.py` (неподвижные точки и гессиан классического отображения, точный следовый полином периода 3) и `conventions.py` (коммутаторные и ковариантные конвенции квантового отображения) + `report.json`.

## Переезжающие файлы

| Старый путь | Новый путь | SHA-256 содержимого | Байты |
|---|---|---|---|
| `supplement/fixed_map/report-audit-20260919/audit.md` | `supplement/fixed_map/report-audit/audit.md` | `8fd21059bd23fbab382e78c930a931fc6a88716418f1d22ba74f5f77eb4eb3b0` | 13409 |
| `supplement/fixed_map/report-audit-20260919/checkpoint.json` | `supplement/fixed_map/report-audit/checkpoint.json` | `24ae5f534b488799ad27db7dc9efd50c7aedf919080ad2c0f9061a0384a4d560` | 5355 |
| `supplement/fixed_map/report-audit-20260919/cubic_variance.json` | `supplement/fixed_map/report-audit/cubic_variance.json` | `6941499f8acfbd1065b8e562705dacaf8ca453cc6850d10c7f3f3824558cc47f` | 11640 |
| `supplement/fixed_map/report-audit-20260919/cubic_variance.md` | `supplement/fixed_map/report-audit/cubic_variance.md` | `57eb5bf2056b860d56d1ae6b540f60887346eeae9c53afc3ee9046c8b95ea5e9` | 8018 |
| `supplement/fixed_map/report-audit-20260919/cubic_variance.py` | `supplement/fixed_map/report-audit/cubic_variance.py` | `00184f15a2c5fcb6d9383869e5925b271efb12b55b88f464054f718a0bbeac6d` | 5940 |
| `supplement/fixed_map/report-audit-20260919/cue_reference.md` | `supplement/fixed_map/report-audit/cue_reference.md` | `0d2d142f4b1e85489125f2c4d45569f47e4c9a779e6f9047d6a371b2a18b6c03` | 7145 |
| `supplement/fixed_map/report-audit-20260919/cue_reference.png` | `supplement/fixed_map/report-audit/cue_reference.png` | `c61a155193a823d8e1544b0f157ecbe409f4400a699653c31ec2bd5857bf4708` | 135355 ⚠ бинарный — браузерная загрузка |
| `supplement/fixed_map/report-audit-20260919/cue_reference.svg` | `supplement/fixed_map/report-audit/cue_reference.svg` | `31d0e0b26cae6ab5f47924774529ec429ab6cf8abcf74fd5b192c3ff52181bbf` | 71356 |
| `supplement/fixed_map/report-audit-20260919/exact_symbol_check.wl` | `supplement/fixed_map/report-audit/exact_symbol_check.wl` | `0786c85bb8d2d537139ac2ee4e69b21c203c07f35a0be8a1cc60a9fccf58fbc4` | 791 |
| `supplement/fixed_map/report-audit-20260919/folded_spectrum_control.json` | `supplement/fixed_map/report-audit/folded_spectrum_control.json` | `025236997b1a9e9351e7be6e8be87d78f7bf47d9cb52117de39442d7c2c7cea4` | 2901 |
| `supplement/fixed_map/report-audit-20260919/folded_spectrum_control.md` | `supplement/fixed_map/report-audit/folded_spectrum_control.md` | `c8474014a2eedad9b1b3d71163c5516dde5f4b03ce86cf6188ace644c3962c6e` | 5770 |
| `supplement/fixed_map/report-audit-20260919/folded_spectrum_control.py` | `supplement/fixed_map/report-audit/folded_spectrum_control.py` | `6db1a30b58fa6305d547f744adfe99038069175271657d899ed3834a89c7149d` | 2139 |
| `supplement/fixed_map/report-audit-20260919/independent_variance_review.json` | `supplement/fixed_map/report-audit/independent_variance_review.json` | `9fadaaede5e157b908fc6c5022b4da82fc2f68dfd8ad2a2476db0b9809806424` | 2115 |
| `supplement/fixed_map/report-audit-20260919/independent_variance_review.py` | `supplement/fixed_map/report-audit/independent_variance_review.py` | `6f4df515f36c8e69e34b174bcaf23905a4300a416aea79b48c4a4d5486ed44b3` | 7409 |
| `supplement/fixed_map/report-audit-20260919/monodromy_eigenangles.npz` | `supplement/fixed_map/report-audit/monodromy_eigenangles.npz` | `11f18c06908ebd9d2849c8db7339507be93a0fe3394c436344034dbb55cd6773` | 27340 ⚠ бинарный — браузерная загрузка |
| `supplement/fixed_map/report-audit-20260919/monodromy_experiment.json` | `supplement/fixed_map/report-audit/monodromy_experiment.json` | `426c97b72dae6c73178709d9af545595ed493151edfe5e7de8879e551c01d1a2` | 3984 |
| `supplement/fixed_map/report-audit-20260919/monodromy_experiment.py` | `supplement/fixed_map/report-audit/monodromy_experiment.py` | `f175a6cc14118b9bd8ba635ad281035a9493d0a22921522e57c30051446b80ed` | 5416 |
| `supplement/fixed_map/report-audit-20260919/plot_reference.py` | `supplement/fixed_map/report-audit/plot_reference.py` | `d22728c24135431002fc31bd8551a87f96b1c970ef3e041dc37455f65cee02b4` | 1842 |
| `supplement/fixed_map/report-audit-20260919/resonant_normalization.md` | `supplement/fixed_map/report-audit/resonant_normalization.md` | `cffe68c1dc6b0cb8fb9d144704d638933efadd500584fdb0205e9b8d4d5b5748` | 6128 |
| `supplement/fixed_map/report-audit-20260919/symbol_and_symmetry.md` | `supplement/fixed_map/report-audit/symbol_and_symmetry.md` | `91a755b36e6828742a430f34695733c1b1ae950f05ccb40ea63b9ee1e67a9e2d` | 10302 |
| `supplement/fixed_map/report-audit-20260919/verify.json` | `supplement/fixed_map/report-audit/verify.json` | `96d4f339cd530fc71d74e536a01c85e9f0243ee854f89ed36348c8e4c4c544b6` | 8846 |
| `supplement/fixed_map/report-audit-20260919/verify.py` | `supplement/fixed_map/report-audit/verify.py` | `a1ec10124f85fc2345ec7fb4f46302195209c128b2dd421a653d219e75b0ef95` | 10726 |
| `supplement/fixed_map/fixed-map-audit/classical.py` | `supplement/fixed_map/classical-conventions/classical.py` | `fdac48da96adbaa3511a611c8a5d9a8494d7b9a5789974947fa83ee07bb64de2` | 928 |
| `supplement/fixed_map/fixed-map-audit/conventions.py` | `supplement/fixed_map/classical-conventions/conventions.py` | `aca499c7e8f4548a01f8c52d9973776872278a7f7e2027a3944253346a25916e` | 877 |
| `supplement/fixed_map/fixed-map-audit/report.json` | `supplement/fixed_map/classical-conventions/report.json` | `9e7c511facbe1857bbba5643f2fccc6fc6daa074817f0dcc0d3f03f8fd2d14e0` | 2035 |

## Отредактированные тем же коммитом файлы (миграция потребителей)

- `supplement/fixed_map/inventory.json` — у 25 строк выше обновлено только поле `path`; `original_path` (исторический `build/...` провенанс), `previous_editions` и запись издания 2026-10-06 не тронуты. В `edition_updates` добавлена запись по собственной конвенции файла (дата, `previous_commit`, причина, список новых путей): переименование фазы 2, хэши содержимого сохранены. Верификатор supplement утверждает sha256 каждой из 116 строк по новому пути.
- `computations/maintenance/verify_fixed_map_supplement.py` — 6 путей списка `CHECKS`: `report-audit/{verify,cubic_variance,independent_variance_review,folded_spectrum_control}.py`, `classical-conventions/{classical,conventions}.py`.
- Три аудита линии Heisenberg, загружающие `verify.py` по корневому пути (загрузка + список источников `sources`, по 2 строки в каждом): `computations/verification/signed_heisenberg_audit.py` (строки 265, 269), `resonant_density_audit.py` (строки 58, 315), `heisenberg_note_audit.py` (строки 179, 294) — путь заменён на `supplement/fixed_map/report-audit/verify.py`. Ожидаемая дельта провенанса свежих выходов аудитов: список `sources` несёт новый путь; собственный `source_sha256` каждого аудита меняется, потому что редактируется сам файл аудита; хэш содержимого `verify.py` не меняется. Депонированные исторические выходы не переписываются.
- `supplement/fixed_map/README.md` — 2 ссылки строки «Uploaded report audit» (`audit.md`, `cue_reference.md`) и имя каталога в прозе заключительного абзаца (`fixed-map-audit` → `classical-conventions`).
- Ссылки в поддерживаемых заметках: `mathematics/folded_quadratic_resonance_control.md`, `mathematics/heisenberg_trace_support.md`, `mathematics/signed_heisenberg_comparison.md` (по 1 ссылке), `literature/folded_quadratic_sources.md` (1), `literature/signed_heisenberg_sources.md` (2).
- `record/claims.json` не тронут: ссылок реестра на оба каталога — 0 (перепроверено полным поиском при сборке).

## Сознательно НЕ мигрированные носители (разрешаются настоящим манифестом)

- Внутри переезжающих файлов: исторические команды запуска с путями исходной раскладки `build/report-audit-20260919/...` (`audit.md`, `checkpoint.json`, докстринги `verify.py` и `independent_variance_review.py`) и идентификатор чекпойнта `report-audit-20260919-cue-variance-folded-control` — датированное содержимое замороженных байтов; раскладка `build/` — та самая историческая, что записана в `original_path` инвентаря. Байты не правятся.
- `supplement/fixed_map/algebraic-return/checkpoint.json` — замороженный чекпойнт: поле `parent_checkpoint` — идентификатор родительского чекпойнта, ключи `input_sha256` — пути исходной раскладки `build/`; не указатели живого дерева.
- `supplement/fixed_map/algebraic-return/exact_return_theorem.md` (заголовок, строка 4) и `supplement/fixed_map/design-return/research_checkpoint.md` (§§7–8) — упоминания пути в кодовых спанах внутри файлов восстановленного издания, запиненных инвентарём по содержимому; это датированные провенанс-цитаты («19 September 2026»), а не ссылки. Байты восстановленного издания настоящим пакетом не правятся нигде; упоминания разрешаются таблицей переезда выше.
- `record/audits/era_baseline_attestation_20261023/inventory_abel.json`, `inventory_wick.json` — замороженные инвентаризации аттестации эпох своих дат.
- Замороженные носители `evidence/` (38 файлов) и `archive/` (43 файла) с упоминаниями старых путей — депонированные записи прогонов и манифесты своих дат, как исполнено.

## Бинарные файлы и честная оговорка

`cue_reference.png` (135 355 Б) и `monodromy_eigenangles.npz` (27 340 Б) коннектор (push-files, только UTF-8 текст) перенести не может. Механика: загрузка сессией владельца через веб-интерфейс GitHub в новый каталог с последующей сверкой git blob SHA каждого файла с таблицей выше; оригиналы удаляются браузером только после подтверждённой сверки. Если браузерная загрузка окажется недоступна, бинарные файлы остаются в старом каталоге как именованный остаток, а пакет не считается закрытым до отдельного решения.

## Удаления (следующим шагом, браузером, по каталогам)

- `supplement/fixed_map/report-audit-20260919/` — все 22 файла (после blob-сверки бинарных загрузок).
- `supplement/fixed_map/fixed-map-audit/` — все 3 файла.
