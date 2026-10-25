# HW07 — Оценивание / Assessment

100 баллов: код 80 и анализ 20. Самопроверка не является итоговой оценкой. / 100 points: code 80 and analysis 20. Self-checks are not a final grade.

| Код / Code | Баллы / Points |
|---|---:|
| Реальная первая Validation-статья: текст, токены, слова, 48-token budget, длины обоих запросов / Actual first validation article, text, tokens, words, budget and both prompt lengths | 10 |
| parse_label: strip/casefold, точные четыре метки, прочие ответы −1 / Exact four labels after strip/casefold, all other responses −1 | 15 |
| metric_report: accuracy (5), macro-F1 labels 0–3 zero_division=0 (5), valid_rate (5); INVALID не удаляется / Three metrics over all observations | 15 |
| Одинаковые Validation ID, zero-shot/four-shot без Test (10); строгое правило выбора и tie→zero-shot (5) / Matched validation comparison and strict selection rule | 15 |
| Реальные ID/text/true/raw/parsed ошибок (5); matrix 5×5 включая INVALID (5) / Actual error records and complete confusion matrix | 10 |
| Test только после фиксации выбора (5); журнал настроек и ID (5), реальные версии и корректный JSON (5) / Frozen final evaluation, configuration/ID log and real versions | 15 |

| Анализ / Analysis | Баллы / Points |
|---|---:|
| Измеренные длины и различие слов/токенов (2); цена обрезки контекста (2) / Measured token lengths and truncation tradeoff | 4 |
| Ошибка формата против ошибки класса на реальных выводах (2); почему INVALID остаётся в метриках (2) / Real format versus class errors and retention of INVALID | 4 |
| Проверяемая гипотеза до candidate (2); численное сравнение и корректный вывод, даже при проигрыше (2) / Prespecified hypothesis and measured interpretation | 4 |
| Наблюдение и гипотеза для каждой доступной ошибки, до трёх; отсутствие ошибок указано честно / Observation versus hypothesis for up to three actual failures; honestly report none | 4 |
| Два ограничения (2), следующий эксперимент без подбора по Test (1), источники/AI-помощь (1) / Two limits, a follow-up without test tuning, attribution | 4 |

Не требуется получить высокий F1. Ошибки генерации не штрафуются, если честно учтены и разобраны. Копирование чужих чисел вместо собственного запуска не засчитывается в соответствующем пункте. Для двухбалльного пункта: 2 — полно, 1 — частично, 0 — отсутствует/неверно; код оценивается по независимым подпунктам. / High F1 is not required. Model failures are acceptable when honestly counted and analysed. Reusing someone else's numbers earns no credit for the affected criterion. Two-point criteria earn 2/1/0 for complete/partial/missing or incorrect evidence; code subcriteria are independent.

Штраф: исходный балл × max(0, 1 − просрочка / 14 суток), после группового срока из живой матрицы. Время — подтверждённая сдача Drive, не локальная дата. / Final = raw × max(0, 1 − lateness / 14 days), using the live group deadline and verified Drive submission event.
