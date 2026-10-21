> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round12_2026_10_21/root_critical_circle_wolfram_output.md`. Embedded SHA256: `2807ed2abafe29862492c0d22ca6d4b806bdd6fadacdf9ca2c0fed32ca795502`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Исходный ответ на точную символическую проверку

Выполнен код `root_critical_circle_wolfram.wl` в Wolfram Language.
Ответ инструмента получен 21 октября 2026 года:

```text
Out[1]= {9/10, 0, 0, (-2*Pi^2*(9800 + 3*Cos[2*p*Pi] - 4*Sin[2*p*Pi]))/125, 0, 0}
```

Поскольку
$\cos(2\pi p-\alpha_0)=(-3\cos 2\pi p+4\sin 2\pi p)/5$,
четвёртая компонента совпадает с

$$
-\frac{2\pi^2}{25}\bigl(1960-\cos(2\pi p-\alpha_0)\bigr).
$$

Проверка подтверждает только явно вычисленные производные. Никакого
утверждения об асимптотике спектральной статистики из ответа
вычислительной системы не выводится. Производные также вычислены
непосредственно через разложения косинуса в доказательстве.

