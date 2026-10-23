# MANIFEST-P2G2 — фаза 2, пакет P2-G2: промоушн дома верификаторов `computations/verification/chat_20261011/` → `circular_phase_controls/` и его обёртки `chat_research_20261011.py` → `circular_phase_controls.py`; запись без переезда для `cat_jet/` и `fractional_hamming/`

**Источник:** живой main после пакета P2-G1 (коммит `9230249`): claims.json blob `53c0069cc9317cb706afd1c69198256bd37b5035` сверен с живым main коннектором при сборке настоящего пакета. Удаления P2-G1 двух старых каталогов верификаторов шли браузером параллельно и поверхностей этого пакета не касаются.
**Состав: 11 файлов, 1 каталог + 1 корневая обёртка** — переименование на той же глубине (`computations/verification/<имя>/`), поэтому вся `parents[N]`-геометрия и внутридомовые относительные пути сохраняются дословно. 8 файлов перенесены байт-в-байт; 3 файла отредактированы только в строках путей/имён (см. ниже). Имя выбрано по содержанию: дом — «Bounded circular-phase controls» (заголовок его README): точные коэффициенты Jack, кумулянты CSE, плотности Пфаффиана, независимый C++ SSYT-контроль круговой фазы, alternating/Walsh clock-контроли; обёртка — курируемый раннер того же набора. Стиль согласуется с соседями по `computations/verification/` (`abel_gaussian_wick`, `fractional_hamming`, `charge_strengthening`).

## Переезжающие файлы

| Старый путь | Новый путь | SHA-256 исходного содержимого | Байты |
|---|---|---|---|
| `computations/verification/chat_20261011/README.md` | `computations/verification/circular_phase_controls/README.md` | `32ae22d9137a3ab8b646941e6585fc79dbd2ba67ee037c6440f0ed6c29bf57cf` | 504 |
| `computations/verification/chat_20261011/audit_tools/run_experiment.py` | `computations/verification/circular_phase_controls/audit_tools/run_experiment.py` | `13cd8da1be7da1f0742810e55c57a1f89bbee4c2a0342fc881892a124a04ee7d` | 20697 |
| `computations/verification/chat_20261011/audit_tools/validate_manifest.py` | `computations/verification/circular_phase_controls/audit_tools/validate_manifest.py` | `4f94cc4dea9689b0547ff7efa608d52cfd951e2db76c5d9227f4706fa2205c16` | 19898 |
| `computations/verification/chat_20261011/cumulant_contract.json` | `computations/verification/circular_phase_controls/cumulant_contract.json` | `c8dfb94e18a4887b99e5e1ee1788c0072f498ba472d439ffd6a0faecad2fe625` | 1349 |
| `computations/verification/chat_20261011/integration_contract.json` | `computations/verification/circular_phase_controls/integration_contract.json` | `16ace122d92c4ee69192812715a48b2e0b4c9614451d5dbf7d2b799d70d9bc95` | 2652 |
| `computations/verification/chat_20261011/pfaffian_contract.json` | `computations/verification/circular_phase_controls/pfaffian_contract.json` | `3456e3689818c0e7f9f55e165a274758cf45522b153101dc513dd6a0709a09d3` | 1617 |
| `computations/verification/chat_20261011/scripts/cumulant_formula_controls.py` | `computations/verification/circular_phase_controls/scripts/cumulant_formula_controls.py` | `a163ec21464d253104619ebe70d81958402c4d26871b9342348a15a7a48e6049` | 5851 |
| `computations/verification/chat_20261011/scripts/exact_checks.py` | `computations/verification/circular_phase_controls/scripts/exact_checks.py` | `264cdbaec0e853b85f877409b36891a746c385e46f2149a082777f033e41c8ac` | 8167 |
| `computations/verification/chat_20261011/scripts/pfaffian_controls.py` | `computations/verification/circular_phase_controls/scripts/pfaffian_controls.py` | `637d4d52145fd42670f0f416267e7f09708cf3cd068c0c40581fe9a1321cf17f` | 4985 |
| `computations/verification/chat_20261011/scripts/run_controls.py` | `computations/verification/circular_phase_controls/scripts/run_controls.py` | `e306fde176aeb6f70ed13c0af4e9938e34d9becf2d1822c56d8ef87c9f249a84` | 1226 |
| `computations/verification/chat_research_20261011.py` | `computations/verification/circular_phase_controls.py` | `4c0af7d970c4041343e8ea39f0de04ae3e32a097c7ff9423fdc3fe489a19fb1a` | 5466 |

## Отредактированные при переезде файлы (не байт-копии)

- `computations/verification/circular_phase_controls.py` (обёртка) — 2 строки: константа `SCRIPTS` (строка 22: префикс дома) и значение по умолчанию `--output` (строка 46: `build/chat-research-20261011` → `build/circular-phase-controls` — сессионная метка выходного каталога сборки, не путь к дому; раскрывается явно). git blob: `ef3ccdcc167fed21f951d606458a04ce90933b51` → `8fa1ea332962ff17e3ec5c0076adc0b9de4d6d5f`; SHA-256 нового содержимого `1817da0718da6f6afab33b037e14207787c5d47715113afe87c09fe5692c406c`, 5 477 Б. Проза докстринга («the scoped 11 October research checkpoint») — историческое описание, не имя пути; не тронута.
- `computations/verification/circular_phase_controls/README.md` — 1 строка командного пути (строка 5: имя обёртки в команде запуска). git blob: `08c4e5ca3b08ecbab5b74f8e2935ae5138dcf6ff` → `d9a21b2aabc2634f0f8d71c8691eb29cfa6815b3`; SHA-256 нового содержимого `5c94cfb8e6d5dfe2495ff214ce85876d35f38c3b7a3f5d93fdc4482953f6c9f2`, 505 Б.
- `computations/verification/circular_phase_controls/integration_contract.json` — только путевые строки: 14 вхождений префикса дома + 2 вхождения пути обёртки (списки `execution_artifacts` и `mathematics.inputs`); `claim_id` (`BGS-TRACE-067-070-071-bounded-controls-20261011`) — идентификатор депонированных прогонов, не путь; не тронут. git blob: `69f54b9c34eef6dbbc3a60561ac831e4225b9164` → `a76950dc43331b0b9f23b3bd3b531b24f59048bf`; SHA-256 нового содержимого `73852fa2f30f15abe2f4424a053ae3b125252a04cc8eafe940b1db83d5a464c2`, 2 794 Б.

## Миграции тем же коммитом

- `record/claims.json` — ровно 4 значения `verifiers[]` у 4 claims (BGS-TRACE-069, BGS-TRACE-070, BGS-TRACE-071, BGS-TRACE-072): `computations/verification/chat_research_20261011.py` → `computations/verification/circular_phase_controls.py`. Путей реестра внутрь трёх каталогов (`chat_20261011/`, `cat_jet/`, `fractional_hamming/`) — 0 (перепроверено полным поиском). Эпохальная регистрация не требуется — по измерению: ни один из 4 claims не входит в запечатанный снимок wave2 (96 строк), все четверо — follow-on `after_wave3`; поправок `historical_claim_amendments` нет, множество `approved` не расширяется (остаётся 67).
- `.gitattributes` — 5 строк: путевые ключи атрибута `whitespace=-blank-at-eof` для пяти файлов дома переведены на новый префикс (иначе атрибуты молча перестали бы применяться). Потребитель, отсутствующий в переписи дизайна §5; класс правки тот же.
- `REPRODUCE_unified.md` — 13 путевых вхождений префикса дома + 3 вхождения пути обёртки в двух исполняемых блоках воспроизведения (интеграционный контракт и контракт Schur). Ярлыки свежих выходных каталогов в примерах (`build/chat-research-reproduction`) — не указатели, оставлены.
- Контракты прогонов, использующие общие `audit_tools` дома как исполнительные артефакты, — только путевые строки префикса дома (26 вхождений): `computations/verification/clock_reference_contract.json` (4), `haar_feedback_contract.json` (4), `schur_censoring_contract.json` (4), `spectrum_coherence_contract.json` (2), `two_step_drift_contract.json` (4), `unitary_two_step_contract.json` (4), `feedback_concentration/row_contract.json` (2), `feedback_concentration/stopped_contract.json` (2). Класс потребителя, отсутствующий в переписи дизайна §5: `run_experiment.py` требует, чтобы `execution_artifacts` контракта дословно совпадали с существующими `--input`-файлами, поэтому без миграции весь этот слой воспроизведения ломался бы. `claim_id`, утверждения и границы контрактов не тронуты; депонированные манифесты прогонов в `archive/evidence/` не тронуты и продолжают описывать прогоны как исполненные.

## Запись без переезда: `cat_jet/` и `fractional_hamming/`

- `computations/verification/cat_jet/` (10 файлов) — имя признано предметным (линия CAT/jet-контролей), переезд не требуется. Единственная связность: `cat_jet_certificates.py` (строка ~37) грузит шаговые модули importlib-конструкцией `parent/'cat_jet'/step['module']`; имена модулей — из замороженного `archive/evidence/cat_jet_20261006/input_map.json` (имена файлов, не пути). Переименование каталога или модулей настоящим пакетом запрещено дизайном и не выполняется.
- `computations/verification/fractional_hamming/` (7 файлов) — имя признано предметным, переезд не требуется. Связность: CI-тест `computations/maintenance/tests/test_fractional_routing.py` исполняет `fractional_hamming/check_routing.py` подпроцессом; путевые поля рабочего слоя `record/` (~15 полей в 6 файлах, включая sha256-пины по содержимому) переименованием не затрагиваются и не правятся.

## Сознательно НЕ мигрированные носители (разрешаются настоящим манифестом)

- Замороженные пакеты `archive/evidence/executions/2026101{1,2,3,4}/**` и `evidence/executions/20261022/repository-recheck/manifest.json` — депонированные манифесты прогонов с исходными путями; исторические записи как исполнено.
- `record/audits/era_baseline_attestation_20261023/{inventory_abel,inventory_wick}.json`, `record/audits/repository_recheck_20261022/*` — замороженные инвентаризации/аудиты своих дат.
- `archive/MANIFEST-P2G1.md` — манифест предыдущего пакета (упоминает дом как оставшееся сессионное имя очереди G2).
- `record/errata.json` и генерируемая из него `ERRATA.md` (ERR-043) — прозаическое упоминание имени обёртки в тексте датированной errata-записи; не указатель пути, исторический текст не правится.
- `manuscript/unified_sections/chat_research_20261011.tex` и `\input` в `manuscript/BGS_unified.tex`, а также 27 полей `manuscript[]` реестра — секция рукописи со своим датированным именем; поверхность фазы 4, настоящим пакетом не трогается.
- Датированные Wolfram-источники `computations/wolfram/{circular_phase,fourth_delay,reversal_censoring,schur_censoring,walsh_clock}_20261011.wl` — отдельный поддерживаемый слой (README дома: «maintained separately»), вне объёма G2.
- Сиды `20261011` в `schur_censoring_and_clock.py` и `unitary_two_step_obstruction.py` — числовые значения генераторов, не пути.

## Удаления (следующим шагом, браузером)

- `computations/verification/chat_20261011/` — все 10 файлов каталога.
- `computations/verification/chat_research_20261011.py`.
