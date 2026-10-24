# MANIFEST-P2SPECTRAL — фаза 2, пакет P2-SPECTRAL: документы спектральной линии → `record/spectral_research/`

**База (пересверена для финальной сборки):** живой main `3a836e7`
(закрытие волны 7; последний коммит — удаление
`mathematics/weighted_wiener_resonance.md`). Локальная база:
`p2_spectral_work/base_tree` — байт-идентична `p2_math7_work/post_tree`
(`diff -rq` пуст, по 6739 файлов). Сверка с живым main коннектором:
листинг корня `record/` — 62 записи — совпал с локальной базой запись в запись
(призраков нет); git-blob SHA совпали с живыми для `record/claims.json`
(`eebf6feb…`, 197 claims), трёх перемещаемых файлов (`aed0852c…`, `284660de…`,
`4a5afabf…`), `literature/external_dependencies.json` (`e12df5bc…`),
`literature/metadata_audit.json` (`d5fb8c49…`),
`computations/verification/check_spectral_edition.py` (`a88015f3…`),
`computations/maintenance/render_spectral_research.py` (`f2c38113…`),
`record/spectral_research/review_matrix.md` (`dd560c50…`),
`evidence/source_metadata/registry_metadata_20261023_refresh.json`
(`c4d63fc2…`), `record/claim_ledger.md` (`86e373c3…`).
Финальный пост: `p2_spectral_work/post_final` (приор-пост + succession-чекер +
cache refresh + обновлённый манифест). В живой репозиторий при сборке ничего
не писалось; пуш — шаг координатора.

## 1. Карта переезда (переименование = только снятие даты)

| Старый путь | Новый путь | SHA-256 содержимого на базе | SHA-256 содержимого на посте | git-blob нового файла |
|---|---|---|---|---|
| `record/spectral_final_integration_20261021.md` | `record/spectral_research/spectral_final_integration.md` | `7e5c6290f170f9f0…` | `1e59cde1227cccb3…` | `f4fd7ee88575ce825f4d9868a083160c658110dc` |
| `record/spectral_master_audit_20261021.md` | `record/spectral_research/spectral_master_audit.md` | `ee094d76a462d13e…` | `8095599c7e47cfa2…` | `4d0c5487cde43c4fbdf3924dc50c138576ffd65c` |
| `record/trace_closure_20261022.md` | `record/spectral_research/trace_closure.md` | `354ea4fe3e23a145…` | `9fa0a44921d8254b…` | `ec16326e547f841db0d252a5e798f05486e0edcb` |

Переименование одобрено дизайном §9 и не ломает чекер сверх одного оператора:
`check_spectral_edition.py:58` — единственное место, где имена несёт код, и оно
правится тем же коммитом (см. §2). Коллизий в целевом каталоге нет
(`record/spectral_research/` — 237 файлов; имён без дат там не было).

Переехавшие файлы — НЕ байт-копии, а перевод ссылок по геометрии (файлы уходят
на уровень глубже: `record/` → `record/spectral_research/`). Дельта каждого файла
— только цели markdown-ссылок, математическое содержимое не менялось:
- `../mathematics/…`, `../computations/…`, `../evidence/…`, `../archive/…`,
  `../literature/…` → `../../…` (один уровень `../` добавлен);
- `spectral_research/catalog.json`, `spectral_research/sections/README.md`,
  `spectral_research/review_matrix.md` → `catalog.json`, `sections/README.md`,
  `review_matrix.md` (префикс снят — цель уже в том же каталоге);
- `remaining_breakthrough_task_20261021.md` (остаётся в корне `record/`) →
  `../remaining_breakthrough_task_20261021.md`;
- взаимная ссылка `spectral_final_integration → trace_closure` (один каталог) →
  новое имя `trace_closure.md`.
Репозитарно-относительные код-спаны (`record/spectral_research/sources/…` и т.п.)
не менялись: как пути репозитория они остаются верными. Полный построчный дифф
трёх файлов — только строки ссылок (проверено при сборке).

## 2. Правки потребителей тем же коммитом (19 файлов + перегенерированная матрица)

- `literature/external_dependencies.json` — EXT-BR-1975 `project_sources[2]`:
  `record/trace_closure_20261022.md` → `record/spectral_research/trace_closure.md`.
  Это потребительская миграция, не эпохальная: EXT-BR-1975 входит в 18 явно
  допущенных позже входов (`external_dependency_extension.added_ids`), а не в 39
  исторических контрактов (см. §3).
- `computations/verification/check_spectral_edition.py:58` — список markdown-входов
  издания: два переехавших файла получили полные новые пути, третий вход
  (`remaining_breakthrough_task_20261021.md`, не двигается) остался в корне `record/`.
  `spectral_master_audit` в этом списке не было и нет: чекер его не читает
  (дизайн §9 неточен в этом пункте — измерено по коду, а не по дизайну).
  Финальная сборка: чекер стал succession-aware (§5.1, таблица §7) — единственное
  изменение кода пакета сверх списка путей; все остальные проверки чекера
  байт-идентичны прежним.
- `computations/maintenance/render_spectral_research.py:32` — строка генератора
  матрицы: `../spectral_final_integration_20261021.md` →
  `spectral_final_integration.md` (матрица лежит в том же каталоге, что и файл);
  `record/spectral_research/review_matrix.md` перегенерирована скриптом, а не
  правлена вручную (дифф матрицы — ровно эта одна строка; остальные
  генерируемые виды — темы и секции — байт-идентичны базе).
- Навигация (по одной ссылке на файл, если не указано иное):
  `CHANGELOG.md` (final, trace), `RESEARCH.md` (все 3),
  `REPRODUCE_unified.md` (final), `manuscript/README.md` (final, trace),
  `mathematics/README.md` (все 3), `mathematics/results.md` (все 3),
  `mathematics/open_questions.md` (trace),
  `mathematics/spectral_research/README.md` (final),
  `mathematics/topics/fixed-map/README.md` (trace),
  `mathematics/physical_kick_trace_decay.md` (master),
  `mathematics/physical_trace_polynomial_approximation.md` (master),
  `record/README.md` (все 3, same-dir → `spectral_research/…`),
  `record/claim_ledger.md` (все 3, same-dir → `spectral_research/…`),
  `literature/spectral_final_source_scope_20261021.md` (trace; живая датированная
  заметка с позднейшим scoped update — мигрирована как живая, по прецеденту
  волны 7; при несогласии откатить только этот файл до пуша),
  `manuscript/unified_sections/physical_kick_20261021.tex` (`\path` master),
  `manuscript/unified_sections/spectral_trace_closure_20261022.tex` (`\path` trace).
- Cache refresh (финальная сборка, §5.2): новый снимок
  `evidence/source_metadata/registry_metadata_20261024_refresh.json` + его
  `.sha256`, отчёт `record/audits/metadata_cache_refresh_20261024/report.md`,
  перевыбор указателя `literature/metadata_audit.json` (ровно 3 строки).
  Итоговый состав пакета: 28 файлов в пуш-списке — 24 пути приор-сборки
  (3 переезда + манифест + 20 правок; из них чекер и манифест несут финальные
  версии содержимого) + 4 новых пути: снимок, его digest, отчёт refresh и
  указатель metadata_audit.json. Итого 24 + 4 = 28.
- Проверено поименно, что корневые три файла НЕ читаются конструируемыми путями:
  `replay_spectral_corpus.py` и `rebuild_spectral_corpus.py` читают только
  `record/spectral_research/catalog.json`; `render_spectral_research.py` — только
  строку §2 выше; `trace_closure_checks.py` путей к этим файлам не содержит.

## 3. Эпохальная часть: измеренно нулевая

- `record/claims.json`: точный поиск по полям всех 197 claims — 0 ссылок на три
  файла (4 совпадения подстроки `trace_closure_20261022` — это секция рукописи
  `manuscript/unified_sections/spectral_trace_closure_20261022.tex`, другой файл,
  не двигается). Поправок, расширения `approved` и изменений статусов нет.
- `wave2_integration_audit.run()`: JSON базы и поста байт-идентичны
  (SHA `5b53fba85020f16d…` в обоих случаях, `status: passed`).
- Внешняя эпоха (гейт пакета, разрешён родителем; факты сверены на базе):
  исторический снимок `archive/evidence/executions/20261011/chat-research/
  baselines/external_dependencies_20261007.json` содержит ровно 39 контрактов;
  EXT-BR-1975 в нём отсутствует, а входит в `added_ids` (18) расширения от
  2026-10-22; `test_external_epoch_preservation` (6 тестов) пинит только 39
  исторических контрактов и проходит на базе и на посте (6/6).
  Диспозиция H-EXT для `trace_closure` не требуется.
- `record/claim_integration_epochs.json`, `wave2_integration_audit.py`,
  `record/claims.json` в пакет НЕ входят.

## 4. Остаточный скан: старые пути остались только в замороженных носителях

Полный поиск трёх старых стемов по пост-дереву (29 файлов):
- **Замороженные, не правятся:** `archive/MANIFEST-F1.md` (манифест пакета фазы 1);
  `evidence/executions/20261021/spectral-final/` (README, receipt,
  `fresh/math_collector_source.py.txt`); `evidence/executions/20261021/
  spectral-master-audit/README.md`; `evidence/executions/20261022/trace-closure/`
  (README, receipt, math_parse, manuscript_build);
  `evidence/executions/20261022/repository-recheck/manuscript_build.json`;
  `evidence/source_metadata/registry_metadata_20261022*.json` (исторические
  снимки; текущий выбранный кэш 20261023_refresh — см. §5);
  `record/audits/era_baseline_attestation_20261023/*.json` (инвентари старых
  деревьев); `record/audits/repository_recheck_20261022/*.json` (снимки).
- **Ложные срабатывания стем-поиска (не старые пути, не трогаются):**
  все остальные совпадения `trace_closure_20261022` — это секция рукописи
  `manuscript/unified_sections/spectral_trace_closure_20261022.tex`
  (`manuscript/BGS_unified.tex`, `manuscript/README.md`, `record/claims.json`,
  аудиты recheck, era_files_wick).
- Живых указателей на старые пути вне этих классов — 0.

## 5. Решённые пункты — решения родителя, исполненные финальной сборкой

### 5.1. `check_spectral_edition`: succession-aware через MANIFEST-P2SPECTRAL (решение 2)

На базе — PASS (535 source units, 429 markdown-файлов, 1278 ссылок, 197 claims).
На приор-посте (без succession) — FAIL, и только с этими двумя отказами:
- `evidence/executions/20261021/spectral-final/README.md` →
  `../../../../record/spectral_final_integration_20261021.md`;
- `evidence/executions/20261022/trace-closure/README.md` →
  `../../../../record/trace_closure_20261022.md`.
Чекер проверяет ссылки и внутри этих двух замороженных README (они входят в его
явный список markdown-входов). Правило пакета запрещает править
`evidence/executions/**` (вариант А отклонён — заморозка неприкосновенна);
вариант Б «ослабить чекер» отклонён стоящим правилом. Исполнено решение 2:
чекер стал succession-aware через таблицу §7 этого манифеста. Правило строгое:
ссылка проходит iff цель существует по записанному пути ИЛИ по записанной в
таблице преемственности при существующей новой цели; всё остальное — отказ.
Механика fail-closed: таблица читается только из секции §7; любая malformed
строка обнуляет всю таблицу и даёт отказ; отсутствие манифеста даёт пустую
таблицу (поведение на деревьях до манифеста — ровно прежнее). Все остальные
проверки чекера (проекции источников, синтаксис, claims, registered paths)
не тронуты. Негативные контроли — в отчёте финальной сборки (REPORT.md §3):
незаписанная битая ссылка падает; подмена преемника на несуществующий путь
падает; удаление секции падает; поведение на несвязанных входах
байт-идентично прежнему чекеру. На финальном посте чекер — PASS с теми же
счётчиками, что на базе (535/429/1278/197). Замороженные README не тронуты
(сверено побайтово с базой). Ни один discover-тест чекер не запускает
(проверено grep по тестам).

### 5.2. `bibliographic_metadata_audit --self-test`: cache refresh исполнен в пакете

Единственная ошибка приор-поста: `EXT-BR-1975: project_sources differs from
reviewed cache` — точный прецедент Pittel (отчёт
`record/audits/metadata_cache_refresh_20261023/report.md`, пуш `c6a4e38`).
Финальная сборка исполняет рецепт тем же коммитом, а не отдельным шагом:
новый снимок `evidence/source_metadata/registry_metadata_20261024_refresh.json`
(копия текущего; меняется ровно одно accepted-поле:
EXT-BR-1975 `project_sources[2]` → `record/spectral_research/trace_closure.md`;
все `source_observations`, покрытие и impact-множества — без изменений;
`previous_snapshot_sha256` — SHA-256 superseded-снимка
`c27cff0f8593af9373e6822e2ab499bdd1455e6a63943a5c7e1ec69007fb2a7c`;
новый SHA-256 `16e01d7975ff75f79af0462388b4747eae907c41798949cea1aa1560180ba711`),
новый `.sha256`, отчёт `record/audits/metadata_cache_refresh_20261024/report.md`
по образцу 20261023, перевыбор указателя в `literature/metadata_audit.json`
(ровно 3 строки, policy без изменений). Исторические снимки 20261022/20261022_recheck
и текущий 20261023_refresh не меняются (superseded-снимок сверен побайтово).
Отличие от прецедента Pittel, зафиксированное честно: переезд Pittel был
байт-идентичным, а переезд trace_closure — только перевод ссылок по геометрии
(§1); это не затрагивает сертифицируемое кэшем (внешний источник и его review hash
не меняются; меняется только project-internal location). На финальном посте
self-test — rc=0 (515 mutation tests), полный аудит — 57 cached identities match.

## 6. Удаления (браузером, после landing и readback)

1. `record/spectral_final_integration_20261021.md`
2. `record/spectral_master_audit_20261021.md`
3. `record/trace_closure_20261022.md`
   Каждое — с 404-сверкой и подтверждением нового файла в `record/spectral_research/`.

## Succession table (machine-readable; read by check_spectral_edition.py)

| Old path | Successor path |
|---|---|
| record/spectral_final_integration_20261021.md | record/spectral_research/spectral_final_integration.md |
| record/spectral_master_audit_20261021.md | record/spectral_research/spectral_master_audit.md |
| record/trace_closure_20261022.md | record/spectral_research/trace_closure.md |
