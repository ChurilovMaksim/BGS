# Актуальный main: проверка только по GitHub, а не по локальной копии

**HEAD main НЕ сдвинулся: a562e0cf — тот же, что и на старте программы.**
**Проверено по main, а не по локальной копии.**

- Репозиторий: ChurilovMaksim/BGS, ветка main.
- HEAD: `a562e0cfc86ab481f1d351c1a9c7209626568be2`.
- Коммит HEAD: слияние PR #74, «Final independent audit: notation paragraph,
  dated qualifiers, changelog gap, receipt», автор Nemo,
  дата коммита 2026-11-01T08:36:54Z.
- Дата этой проверки: 2026-11-01, 14:34 по Екатеринбургу (09:34 UTC).
- Метод: только GitHub-коннектор, только read-инструменты
  (`list_commits`, `get_file_contents`, `search_code`). Локальные снимки
  от 29 октября и каталоги `bgs-full-head-*` / `bgs-test-*` как источник
  НЕ использовались. Они читались только в конце — для сравнения с уже
  сданными файлами, а не для цифр этого отчёта.
- В main ничего не пушилось, Lean не собирался, другие файлы не правились.

## 1. formalization/Bgs.lean на HEAD

- Blob SHA (по коннектору): `00774264e8c7435ec1a72335a2224219970df2c2`.
- Строк `import`: **108**.
- Из них: **107 прямых модулей** + агрегатор `import Bgs.Mathlib`.
- Итого листовых модулей в графе: 107 (верхний уровень) + 39 (Mathlib-слой)
  = **146**. Вместе с агрегатором `Bgs/Mathlib.lean` — 147 файлов `Bgs/`
  в графе, плюс сам корневой `Bgs.lean`.

Прямые модули (107, в порядке файла, без агрегатора):

AnalyticOrbitKernels, CayleyCurveEnergy, CayleyEnergy, CueLoopKernels,
FibonacciRatioSmall, GeneralHyperbolicParity, HistoricalMobiusDegenerateFiber,
LocalityKernels, MagneticTraceSmall, PairKeyFourthMoment, PairKeySecondMoment,
PellCoboundary, PellCohomology, PellEchoWeights, PellFourierKernel,
TorusLevelSets, TorusScaleLaw, FourCutKernel, SevenPrimary,
PhaseChannelJetKernels, PhaseFrameWitness, TorusDimensionBound,
ActiveRankDefect, CoherenceBudget, TraceStatement, RetTowerGeometry,
Fm009TraceObstruction, Fm001Statement, Fm021Statement, KickBlindRational,
OrbitOrthogonalRational, PositiveTimeRational, OrderLadderRational,
OrderTrichotomyRational, CrtCompositeRational, SquarefreeProductRational,
OddModulusRational, UniformOrbitOverlapRational, PhaseFormFactorRational,
DiagonalPhaseFormFactorRational, DiagonalPhaseShortTimeRational,
ScalarReturnBesselRational, SixteenPhaseSymmetryRational,
HyperbolicDiagonalFormFactor, HyperbolicShortTime, RevivalClosureRational,
MomentumPhaseCue, LineCEncounter, LineDCerts, LineBDerand, LineBPhase2,
LineBPhase3, LineBPhase4, LineE, LineEResonance, LineF, LineG, LineH, LineI,
LineIArith, LineDDefs, LineDOrbitPair, LineDBridge, LineDPhaseLemma,
LineD149Props, LineDParity, LineDOrbitPairFull, LineJArith,
LineBTraceFormula, LineBGauss, LineBExpand, LineBTsum, LineDDmBridge,
LineDStrongKick, LineDStrongKickBridge, LineDStrongKickConc,
LineDParityBridge, LineDCoeff, LineDCoeffBridge, LineDCoeffReality,
LineBNAverage, LineBNAverageBridge, LineBNAverageM1, LineBNAverageUnits,
LineKFinite, LineBTraceM1, LineBHfib, LineLConst, LineMArith, LineNArith,
LineN2Arith, LineN3Arith, LineN4Arith, LineN5Arith, LineN6Arith,
LineN7Arith, LineN8Arith, LineN10Arith, LineN11Arith, LineN12Arith,
LineN13Arith, LineN14Arith, LineN15Arith, LineN16Arith, LineN20Arith,
LineN20TailArith, LineN21Arith.

Замечание о счёте: это счёт импортов, а не счёт файлов в каталоге.
Файл, лежащий в `Bgs/`, но не импортированный, в этот счёт не входит
и здесь не утверждается ни его наличие, ни его отсутствие — список
каталога через коннектор в этой проверке не снимался.

## 2. formalization/Bgs/Mathlib.lean на HEAD

- Blob SHA (по коннектору): `05c32e13a5076cb2298a1e76e9bb3b496a448440`.
- Строк `import`: **39** — то же число, что и в снимке от 29 октября,
  и тот же набор имён (AbelPoisson, AbsorptionBound, CatMap,
  ClockCharacter, ClockFloor, ClockRigidity, CoherenceMemory,
  CueReference, DeletedClock, DigitFUP, DigitFUPBinary, ExactCumulants,
  FirstReturnPulse, FlatChirp, FlatPerturb, FlatTensor, FormFactorCurve,
  FreshPhaseAverage, HardyClock, HardyIdentity, HardyRigidity,
  HyperbolicEigenline, LocalJetObstruction, MultiradiusRigidity,
  PairSumFactorization, PeriodicPoints, PhaseChannel, PureLoss,
  QuadraticResponse, RadialTail, ResonanceComb, SineKernel, TraceMobius,
  TraceMobiusGeneral, TraceReconstruction, TwoClock, TwoStepObstruction,
  TwoStepVariance, UniformCluster).
- То есть рост графа с 29 октября произошёл за счёт верхнего уровня
  (48 → 107 прямых модулей), а Mathlib-слой по числу и именам
  не изменился.

## 3. claims.json на HEAD: как искали, что нашли

Все попытки зафиксированы, неудачи не скрыты:

1. `search_code` с аргументом `q` — ошибка схемы: инструмент требует
   поле `query`, а не `q`.
2. `search_code` с `query = "filename:claims.json"` — вернул 70 912
   результатов по всему GitHub, без ограничения репозиторием.
   Как поиск по репозиторию BGS этот результат непригоден и не
   использовался.
3. Прямой путь `claims.json` (корень) — файла нет: коннектор вернул
   только совпадения в архиве
   (`archive/evidence/charge_strengthening_20261007/...`,
   `archive/evidence/fractional_hamming_20261007/...`).
   Это не реестр, и его цифры здесь не используются.
4. Прямой путь `record/claims.json` — **УСПЕХ**. Это и есть реестр.
5. `formalization/claims.json`, `data/claims.json`, `evidence/claims.json` —
   файла нет (ошибка коннектора «path does not point to a file»).

Итог по реестру на HEAD:

- Путь: `record/claims.json`.
- Blob SHA (по коннектору): `7bcfeaef5e18d40f8c30266c1b02855055549785`.
- Поля: `schema = "bgs-claims-v1"`, `updated = "2026-11-01"`,
  `status_authority = "record/claims.json"`.
- Размер скачанного текста: 845 102 символа.
- Всего записей: **419**.
- По полю `state`:

| state | записей |
|---|---|
| proved | 338 |
| open | 42 |
| conditional | 21 |
| verification-pending | 17 |
| refuted | 1 |
| всего | 419 |

- Новое по сравнению со срезом 29 октября: состояние `refuted`
  (одна запись: BGS-TRACE-179). В старом срезе его не было.
- Записей с непустым `formalization`: **147** из 419.
- Из 338 `proved`: с ссылкой на Lean — **134**, без ссылки — **204**.
- Различных ссылок на Lean-файлы: **127**, из них ссылок на `Line*` —
  **57** различных.
- Различных значений `ledger_status`: **312** — ярлык ещё менее
  однороден, чем в старом срезе (там было 115 различных при 201
  `proved`).

Ключевые записи (только по HEAD):

- BGS-BGS-001 — **open**, ссылок на Lean нет. Центральная BGS
  по-прежнему открыта.
- BGS-TRACE-005 — **open**, единственная ссылка —
  `formalization/Bgs/TraceStatement.lean` (только формулировка).
- BGS-TRACE-149 — proved: LineDCerts, LineD149Props.
- BGS-TRACE-150 — proved: LineDPhaseLemma.
- BGS-TRACE-154 — proved: LineDParity, LineDParityBridge.
- BGS-TRACE-157 — proved: LineDCoeff, LineDCoeffBridge, LineDCoeffReality.
- BGS-TRACE-163 — proved: 8 ссылок (LineBDerand, LineBTraceFormula,
  LineBGauss, LineBExpand, LineBTsum, LineDDmBridge, LineBTraceM1,
  LineBHfib).
- BGS-TRACE-175 — proved: 4 ссылки (LineBNAverage, LineBNAverageBridge,
  LineBNAverageM1, LineBNAverageUnits).

Важно: `proved` здесь — значение поля `state` в реестре проекта.
Оно не означает «доказано в полной общности» и не отменяет оговорок
в `boundary` и `ledger_status` каждой записи.

## 4. Что именно устарело в уже сданных файлах

Все три файла опирались на срез 29 октября (232 записи, 49 импортов).
Их качественные предупреждения сохраняются, а все числа подлежат
замене таблицей из раздела 3.

### INVENTORY.md — устарели все счётчики

| Показатель | Было (срез 29.10) | Сейчас (main a562e0cf) |
|---|---|---|
| Импортов в Bgs.lean | 49 | 108 (107 модулей + Mathlib) |
| Прямых модулей | 48 | 107 |
| Листовых модулей в графе | 87 | 146 |
| Записей в реестре | 232 | 419 (+187) |
| proved | 201 | 338 (+137) |
| proved со ссылкой на Lean | 62 | 134 (+72) |
| proved без ссылки | 139 | 204 (+65) |
| open | 8 | 42 (+34) |
| conditional | 9 | 21 |
| verification-pending | 14 | 17 |
| refuted | не было | 1 (BGS-TRACE-179) |
| Записей со ссылками | 65 | 147 |

Не устарело как метод: подсчёт по графу импортов, а не по `ls`;
предупреждение, что реестр и дерево от 29 октября для пушей
непригодны. Но конкретные цифры 92 файла, 87 листовых, 35 тестовых
деревьев, 2,5 ГБ — это цифры рабочего каталога, а не main, и к main
их применять нельзя.

### PLAN.md — устарела база, но не сама фаза 0

- Цифра «116 файлов верхнего уровня в копии 0d1b» — это счёт файлов
  в каталоге копии, а не счёт импортов. Напрямую с нынешними
  107 импортами её сравнивать нельзя: файл без импорта в 107 не
  входит. Фаза 0 из плана (инвентаризация актуального HEAD) теперь
  частично выполнена для трёх файлов этим отчётом, но полный список
  каталога, заголовки и битые ссылки на HEAD здесь не снимались.
- Утверждение плана «снимок от 29 октября устарел» — подтверждено
  и усилено: разрыв не в несколько файлов, а в 59 прямых модулей
  и 187 записей реестра.
- Несогласованность внутри старых файлов по `native_decide`
  (PLAN: 16 файлов, INVENTORY: 12 файлов, 88 вхождений) этой
  проверкой НЕ разрешена: пересчёт `native_decide` / `sorry` по
  HEAD не проводился, и ни одна из двух цифр к main применять нельзя.

### ADVERSARIAL_REVIEW.md — метод жив, списки неполны

- Все счётчики рецензии (232 / 201 / 139 / 62 / 34 без верификаторов /
  12 без свидетельств / 5 с REFEREE) относятся к срезу 29 октября
  и как числа устарели. В частности, «proved без ссылки» выросло
  со 139 до 204 — проблема, которую рецензия описывает, на HEAD
  стала больше, а не меньше.
- Списки категории A неполны на HEAD: старых 8 open, 14
  verification-pending и 9 conditional теперь 42 / 17 / 21.
  Полные новые списки здесь не приводятся — для них нужен отдельный
  прогон по реестру HEAD, а не дополнение старых списков наугад.
- Конкретные примеры рецензии (TRACE-057–068, TRACE-134, TRACE-142
  и другие) на HEAD по отдельности не перепроверялись, кроме
  центральных BGS-BGS-001 и TRACE-005. Их нельзя автоматически
  переносить как «так и осталось» — только как «требует перепроверки
  по HEAD».
- Сохраняется как правило: цитировать только с квалификатором
  «по внутреннему реестру проекта, запись <ID>, состояние <state>,
  см. её boundary» и с сохранением слов finite / only / conditional /
  partial / project proof / author check / native_decide.

## 5. Два дополнительных факта, проверенных по main

1. `formalization/README.md` на HEAD (blob
   `4ec3913a0b56b995e5e5d0a16d5213565ad116a3`) в первом абзаце
   заявляет 33 модуля + 39 Mathlib + 32 дальнейших модуля.
   Это не сходится с посчитанным на том же HEAD графом
   (107 прямых + 39 Mathlib). То есть README устарел даже
   относительно текущего main, а не только относительно снимка
   29 октября. Полный текст README здесь не разбирался.
2. `formalization/Bgs/LineD150HcollapseFalse.lean` на HEAD
   по этому пути не найден коннектором, и в списке импортов
   `Bgs.lean` такого модуля нет. Модуль-фальсификатор ложного
   коллапса в граф main не входит — замечание INVENTORY о том,
   что его судьба по именам не прослеживается, на HEAD
   подтверждается для графа импортов.

## 6. Что этой проверкой НЕ установлено

- Список файлов в каталогах main (снимался только граф импортов).
- Содержимое модулей, их аксиомы, `sorry` / `native_decide` на HEAD.
- Сборка Lean на HEAD и её результат.
- Верификаторы и свидетельства записей реестра на HEAD.
- Полные списки open / conditional / verification-pending на HEAD.
- Содержимое `mathematics/`, `evidence/`, `archive/` на HEAD.

Этот файл — снимок трёх источников на HEAD a562e0cf для замены
устаревших чисел, а не проверка доказательств.

**Проверено по main, а не по локальной копии.**
