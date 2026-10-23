# Отдельный аудит maintained переноса TRACE-081/082

Дата: 14 октября 2026 года. Это отдельный pass после независимых рецензий frozen O1–O5 и frozen companion M1–M3; он проверяет конечные maintained источники, исправление prose, ссылки и границы подтверждения.

**Нормализованное утверждение.** TRACE-081 сохраняет ровно O1–O5 и лемму для всех обратимых комплексных матриц из frozen blob `666e8a9ab551e945936198638ebb4d4286a67454`. TRACE-082 сохраняет block-resolvent identity M1, norm plateau M2 для всех унитарных $U$, $N\ge2$, $0\le r<N$, и observed return M3 для того же perturbed семейства TRACE-081. В M1 разрешено совпадение измеряемой и неизмеряемой эволюции для отдельных унитарных матриц.

**Единственный основной verdict: proved as written — доказано в сформулированном виде для точно указанных maintained источников.** Формулы и кванторы перенесены без усиления. Прозаический дефект frozen companion устранён. Аналитическое доказательство отделено от конечной арифметики и от некомпилированного здесь Lean arithmetic kernel. Этот verdict не утверждает внешнюю рецензию, приоритет или BGS.

## Точные входы

| Роль | Путь | SHA-256 |
|---|---|---|
| TRACE-081 frozen | `research_session/flat_spectrum_obstruction_20261013.md` | `08de07484be6e6a8fb2612ac9abbbb12ecdeb6660c23b3cb57ba158de62c1030` |
| TRACE-081 maintained | `BGS/mathematics/flat_spectrum_obstruction_20261014.md` | `d78e0a8b27e77c3853caab03e05357a0f878e27ed7fe1d8c57d066008ee94c91` |
| TRACE-082 frozen | `research_session/coherence_memory_candidate_20261014.md` | `b7b90c31b51f5cca32c1ef189d064f6896fcb38a232a740e8dccc05b995afb09` |
| TRACE-082 corrected maintained draft | `research_session/coherence_memory_maintained_20261014.md` | `39cc445b963d4b8a3fa6868a66a0300be48b661791ea34c3c9ad7c3d240cd1a0` |
| TRACE-082 final maintained | `BGS/mathematics/coherence_memory_plateau_20261014.md` | `5c311f6f09714abfe3da9e4e50befa33a5acda3449f19bdb30e331183bb561bc` |
| Независимая полная рецензия O1–O5 | `research_session/flat_spectrum_obstruction_independent_review_20261014.md` | `1b0fca70d10031c01f78117c14840b2a48b305c87de46d0b5ee52b3fd6ed804c` |
| Независимая полная рецензия frozen M1–M3 | `research_session/coherence_memory_independent_review_20261014.md` | `ea0416ff94dc03fc18295cbf44b74370dc44ac3eaaf5c72a2b0c6c6b6d253063` |

Все пути выше относительны к `/workspace/scratch/06745ba532e4`. Два последних SHA относятся к окончательно исправленной Markdown-разметке независимых отчётов. Математические выводы и hashes их проверочного кода/JSON при этой правке не менялись.

## Проверенный перенос математической зависимости

| Проверка | Статус | Точный результат |
|---|---|---|
| TRACE-081, весь текст разделов 1–7 | passed | Побайтно равен frozen sections 1–7; SHA сегмента `8f2918e02d94591fdc52ff1a5d0ce52efc4b430d636cf8b9a26ada1dd484cd02` |
| TRACE-082 definitions и весь M1–M3 | passed | Побайтно равны corrected draft `39cc...`; SHA сегмента `adef5cb1d3f2d08409180c3a4a000a2cbdd7552c255c2a3bd2748d65d411238f` |
| Перенос frozen companion в corrected draft | passed | Diff прочитан полностью; $D,Q,T,E,L,C$ последовательно заменены на соответствующие calligraphic symbols, все domains и norm meanings сохранены |
| M1 Schur complement | passed | Множитель $z^2$, знак минус и порядок $L(I-zE)^{-1}C$ сохранены |
| M1 recurrence | passed | Индексы $s=0,\ldots,n-1$, степень $n-1-s$ и условие $c_0=0$ сохранены |
| M1 prose correction | passed | «These operators need not agree. They do agree for particular unitaries, including diagonal and monomial matrices» устраняет неверное универсальное прочтение |
| M2 полный квантор | passed | Все унитарные $U$, $N\ge2$, целое $0\le r<N$; не добавлены flatness, normality of compression или hypotheses о reversal |
| M2 trace-zero budget | passed | $N^2-1-(r+1)(N-1)=(N-1)(N-r)>0$, времена $j=0,\ldots,r$, complex vector dimensions |
| M3 constants, типы и объект | passed | То же $U_k=A_kE_k$, $t_k=N_k-4p_k$, factor 2 для HS conjugation, entrywise square отдельно от $P(U_k)^{t_k}$ |
| M3 dependency closure | passed | Использует finite order, малые фазы и $P=J$ TRACE-081; M2 и локальные пределы O2–O4 не используются |
| Scope | passed | Abstract family и unaveraged coherence block; signed source, actual quantizer и BGS не объявлены закрытыми |

Таким образом, dependency graph исходных рецензий сохраняется. Новых load-bearing внешних источников, вероятностных предпосылок, clock implications или формализационных зависимостей при переносе не добавлено. Ссылка TRACE-081 из M3 относится к реально существующему maintained файлу, mathematical sections которого побайтно совпадают с независимо проверенным frozen proof.

Новое предложение о monomial unitaries корректно: такая матрица сохраняет диагональное и off-diagonal подпространства при conjugation, поэтому $L=C=0$ и $DT^nD=P^n$ на диагональном пространстве. Для diagonal unitaries это частности с $P=I$.

## Ссылки и доверительная граница

Все девять прямых локальных ссылок двух maintained mathematical files на момент pass разрешались в существующие файлы:

| Источник | Target |
|---|---|
| TRACE-081 | `evidence/executions/20261014/spectrum-coherence/README.md` — обе ссылки на packet |
| TRACE-081 | `mathematics/unconditional_feedback_flatness_20261013.md` |
| TRACE-081 | `computations/verification/spectrum_coherence_controls.py` |
| TRACE-082 | `mathematics/flat_spectrum_obstruction_20261014.md` |
| TRACE-082 | `evidence/executions/20261014/spectrum-coherence/README.md` |
| TRACE-082 | `computations/verification/spectrum_coherence_controls.py` |
| TRACE-082 | `computations/cpp/coherence_memory_verifier.cpp` |
| TRACE-082 | `formalization/Bgs/CoherenceBudget.lean` |

Ссылка TRACE-080 в TRACE-081 обозначает применение отдельно maintained feedback theorem. Новое семейство действительно удовлетворяет указанным числовым startup inputs $C_0=1$, $\|P-J\|=0$. Истинность TRACE-080, все downstream process/clock assumptions и их физическая интерпретация не являются доказательственными листьями O1–O5; перенос явно сохраняет эту границу.

Прочитаны evidence README, Lean source и scope/assertion части maintained Python и C++ verifier sources. Lean source утверждает только:

```text
budget(n,r) = (n-1)*(n-r), n,r : Nat
n >= 2 and r < n  ==>  budget(n,r) > 0
```

Это правильная арифметическая часть dimension budget. Она не формализует trace-zero dimension, ranks/codimensions, выбор kernel witness, HS унитарность, norm plateau, discriminant lemma или какой-либо предел. Maintained текст говорит это явно. В этом pass Lean не компилировался; содержание исходника не выдается за actual compilation/axiom receipt. Для source audit утверждение compilation остаётся отдельным будущим CI-результатом.

Python и C++ verifier sources ограничивают свою область конечными algebraic controls. Родительский агент сообщил об их actual successful executions; данный pass не повторяет эти runs и не выдаёт это сообщение за моё исполнение. Собственные exact finite runs независимого reviewer приведены с commands и hashes в двух отдельных отчётах. Ни один из этих runs не является универсальным или асимптотическим доказательством.

Для documentary closure обнаружена одна техническая незавершённость на момент pass: copied `evidence/.../independent_spectrum_review.md` ещё имел старый SHA `7c89dfe3d7610098939012ec7f41e1b16ce63bc6a9444c9783419ebc76b8f644`, относящийся к неправильной inline Markdown-разметке моего отчёта. Окончательный source report имеет SHA `1b0f...` из таблицы выше; его нужно побайтно перенести при завершении packet. Родительский агент уведомлён. Это не изменение mathematical proof или verdict.

Остальные уже copied frozen inputs и spectrum controls/JSON совпали с проверенными hashes. Companion review, companion controls/JSON и этот transfer report на момент pass ещё ожидали публикационного переноса; это заявленная задача integration, а не неизвестная математическая предпосылка.

## Проверочные команды и итоговая граница

Самостоятельно исполнены SHA-256/Git-blob reads, полный diff frozen companion → corrected draft, точные substring byte comparisons и обход Markdown local links. Проверка core равенств дала:

```text
TRACE081_sections_1_to_7_byte_equal = True
TRACE082_definitions_M1_M2_M3_byte_equal = True
```

Также проверен баланс inline/display math delimiters в окончательных reviewer reports и corrected draft. Main и математические sources этим агентом не редактировались. Commit/push, полный regression, C++ rerun, Lean build и manuscript build в этом pass не выполнялись.

После сохранённого M1 prose correction оставшейся математической импликации для TRACE-081/082 нет. Documentary перенос окончательных отчётов и последующая CI-проверка арифметического Lean kernel сохраняют собственный статус и не усиливают аналитический результат. Истинность утверждений о приоритете или точном содержании библиографических сравнений этим transfer pass не проверялась: эти тексты не являются load-bearing листьями.
