# HW09 — Оценивание / Assessment

100 баллов: 80 код + 20 объяснения. / 100 points: 80 code + 20 explanations.

| Блок / Block | Код / Code | Анализ / Analysis |
|---|---:|---:|
| 1. Построчная нормализация, сохранение входа, нулевые строки / Row normalization, immutable input, zero rows | 20 | 5 |
| 2. Матрица сходства, порядок классов, argmax / Similarity matrix, class ordering, argmax | 20 | 5 |
| 3. Validation-метрики, строгое улучшение, baseline при ничьей / Validation metrics, strict improvement, baseline on ties | 20 | 5 |
| 4. Матрица, все ID ошибок, единственный Test и JSON / Matrix, all error IDs, single Test evaluation and JSON | 20 | 5 |

Анализ 1: объяснить норму по строкам (2), масштабирование (2), обработку нуля (1). Анализ 2: интерпретировать реальные scores (2), порядок столбцов (1), отличие от вероятности (2). Анализ 3: прогноз до candidate (1), реальные метрики обоих вариантов (2), объяснение выбора без подбора по Test (2). Анализ 4: конкретные наблюдения и гипотезы по показанным ошибкам либо явное отсутствие ошибок (2), два ограничения (2), следующий независимый эксперимент (1).

Analysis 1: row norms (2), scaling (2), zero handling (1). Analysis 2: interpret actual scores (2), column ordering (1), distinction from probability (2). Analysis 3: prediction before the candidate (1), measured metrics for both variants (2), explain selection without Test tuning (2). Analysis 4: concrete observations and hypotheses for displayed errors or explicitly no errors (2), two limitations (2), independent follow-up (1).

Срок из живой матрицы группы включительно по Москве. Штраф после срока: raw × max(0, 1 − lateness / 14 суток). Затем отсутствие отметки P09 даёт множитель 0.9 один раз. Лучшей считается попытка после обоих штрафов. / The group-matrix date is inclusive in Moscow time. After the deadline: raw × max(0, 1 − lateness / 14 days). Missing P09 then multiplies by 0.9 once. Compare attempts after both penalties.
