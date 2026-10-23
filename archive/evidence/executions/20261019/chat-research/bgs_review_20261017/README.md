# Проверка BGS и продолжение: 17 октября 2026

Основной документ: **review_and_progress.md**. Полный двухканальный предел
и полная BGS остаются открытыми в этой рабочей программе.

Новые рабочие доказательства:

* `classical_compression_all_sizes.md`: классическое поглощение с ошибкой
  `4B/N` для любого непустого оставленного множества.
* `fixed_channel_total_variation_compactness.md`: при полном G либо явном
  ранговом условии R — компактность в полной вариации, отмеченные полостные
  законы и равномерная интегрируемость первых часов.
* `positive_bernstein_path_law.md`: положительное конечное приближение всего
  закона T с явной W1-ошибкой; при полном G бета-сглаживание даёт TV-приближение.
* `positive_clock_and_moment_window.md`: восстановление уже имевшегося в
  приложении линейного множителя k и более сильного совместного окна моментов.

`self_review.md` содержит собственную проверку новых переходов.
`research_checkpoint.json` разделяет рабочие теоремы, условные выводы и открытый
переход. `attachment_inventory.json` — указатель всех 88 разделов приложения
с границами проверки. Оригинал `two_channel_transmission(4).md` не редактировался
и не дублируется в этом комплекте; его исходный идентификатор и SHA256 записаны.

Вычисления используют только точную рациональную/алгебраическую арифметику,
Python 3.12.14 и, для символических вычетов, SymPy 1.14.0. Семь каталогов
`*_run` содержат контракты, исходные контрольные суммы, результаты и логи.
Все они завершились успешно. `evidence_summary.json` сводит результаты.

Прямое воспроизведение, например:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_classical_all_sizes.py classical_result.json
PYTHONDONTWRITEBYTECODE=1 python3 verify_harmonic_contraction.py harmonic_result.json
PYTHONDONTWRITEBYTECODE=1 python3 verify_haar_covariances.py covariance_result.json
PYTHONDONTWRITEBYTECODE=1 python3 verify_phase_jacobian.py jacobian_result.json
PYTHONDONTWRITEBYTECODE=1 python3 verify_transmission_appendix.py appendix_result.json
PYTHONDONTWRITEBYTECODE=1 python3 verify_positive_path_law.py bernstein_result.json
PYTHONDONTWRITEBYTECODE=1 python3 verify_beta_smoothing.py smoothing_result.json
```

Команды со скриптами, импортирующими SymPy, требуют установленную указанную
версию библиотеки. `*_contract.json` задают точную область каждого вычисления.
Успех конечной проверки не означает доказательства универсальной асимптотики.

Предыдущие условные рабочие входы и их хеши приведены в `inputs/` и
`proof_inputs.json`; они не выдаются за заново проверенные внешние теоремы.
`repo_integrity.json` фиксирует неизменность всех 716 файлов снимка BGS.
Новых коммитов, push или изменений репозитория не выполнялось.

`attachment_corrections.patch` — проверенный патч к приложенному Markdown:
разводит повторные метки CE и синхронизирует QC7 с линейным хвостом k.
`structure_audit.json` содержит фактический подсчёт тегов и AST-проверку всех
встроенных Python-блоков. Патч проверен на временной копии; оригинал не изменён.
