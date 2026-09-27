# HW03: оценивание / Assessment

100 баллов: код 80 + объяснение 20. Практика P03 без отдельной оценки. / 100 points: code 80 + explanation 20. P03 practice is ungraded.

| Задача / Task | Баллы / Points | Требование / Requirement |
|---|---:|---|
| T1 | 20 | NumPy, точный алгоритм разбиения, отсутствие потерь и пересечений / NumPy, specified split algorithm, complete disjoint coverage |
| T2 | 20 | Train-only mean/std, ddof=0, постоянный признак, применение без fit / Train-only statistics, constant feature, transform without fitting |
| T3 | 15 | Необученный Pipeline с заданными шагами и параметрами / Unfitted pipeline with specified steps and settings |
| T4 | 15 | Максимальный val_f1, точное равенство → меньший C, вход неизменён / Highest val_f1, exact ties → smaller C, no mutation |
| T5 | 10 | Полный сериализуемый журнал и фактические версии / Complete serializable log with actual versions |
| **Код / Code** | **80** | |

Каждая задача получает полный балл, только если выполняет все требования; иначе 0. Преподаватель проверяет код, а не только напечатанный score. Нельзя подменять тесты, жёстко прописывать ответы для тестовых массивов или использовать запрещённый в задании метод. Нарушение обнуляет соответствующую задачу без повторного штрафа. Ошибка одной функции не должна автоматически обнулять независимые задачи. / Each task earns full points only if all its requirements are met; otherwise 0. The instructor reviews code, not just the printed score. Do not alter tests, hardcode test answers, or use disallowed methods. A violation invalidates that task without a duplicate penalty; an error should not invalidate independent tasks.

| Объяснение / Explanation | Баллы / Points |
|---|---:|
| Число строк, групп и доля класса по частям (3); смысл группового разделения (2) / Split row/group/class counts (3); group-split rationale (2) | 5 |
| mean=1, scale=1, transform(100)=99 (3); конкретный механизм утечки (2) / Correct manual values (3); specific leakage mechanism (2) | 5 |
| Таблица кандидатов и выбор по правилу (2); Test модели и baseline (2); интерпретация и ограничение синтетики (2) / Candidates and selection (2); model/baseline test results (2); interpretation and synthetic-data limitation (2) | 6 |
| Источник времени сдачи без выдуманной даты (1); источники и помощь (1); одна проверяемая гипотеза следующего эксперимента (2) / Submission-time source (1); attribution (1); one testable follow-up hypothesis (2) | 4 |
| **Объяснение / Explanation** | **20** |

Для трёх чисел: по 1 баллу за каждое; для трёх видов статистик: по 1 за корректное представление во всех частях. Для пары Test-результатов: по 1 за каждый. Для интерпретации/ограничения: по 1 за каждый. Таблица/выбор: по 1 за каждый. Остальные пункты по 2: 0 — отсутствует/неверно, 1 — частично, 2 — полно и конкретно. / The three manual values and three types of split statistics earn 1 point each. Model/baseline test results, interpretation/limitation, and table/selection each earn 1 per component. Other two-point items: absent/incorrect 0, partial 1, complete and specific 2.

Валидность эксперимента проверяется отдельно: если модель выбиралась по Test или обучалась с утечкой, баллы за соответствующее объяснение выбора и Test-результатов не начисляются (пункты 2+2), даже если число высокое. Корректные независимые функции оцениваются отдельно. / If model selection used Test or training included leakage, the selection and test-result explanation components (2+2 points) are invalid, regardless of the score. Correct independent functions are assessed separately.

Самопроверка выдаёт `score`/`code_score` из 80 и `score_kind=code_only`; `explanation_score` и `total_score` остаются null. Преподаватель добавляет объяснение перед расчётом штрафа. Не считать code_score итогом из 100 и не применять штраф дважды. / Self-check reports code credit out of 80 and leaves explanation/total null. Add reviewed explanation points before calculating penalties; do not treat code_score as a grade out of 100 or apply a penalty twice.

Не требуется достигать заданного F1 или выигрывать у baseline. Важны корректность протокола, воспроизводимость и объяснение. / No target F1 or guaranteed improvement over baseline is required. Correct procedure, reproducibility, and explanation matter.
