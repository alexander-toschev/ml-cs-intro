# HW02: оценивание / Assessment

P02 — практика без отдельного балла. HW02 — 100 баллов: 80 код + 20 объяснение. / P02 is ungraded practice. HW02 is worth 100: 80 code + 20 explanation.

| Код / Code | Баллы / Points |
|---|---:|
| T1: проверка входов / validation | 10 |
| T2: матрица ошибок / confusion matrix | 20 |
| T3: четыре метрики / four metrics | 25 |
| T4: порог, включая равенство / threshold including equality | 10 |
| T5: ограничение, равенства, отсутствие кандидата / constraint, ties, no candidate | 15 |
| **Код / Code total** | **80** |

Самопроверка даёт полный балл задачи за прохождение всех её проверок, иначе 0. Преподаватель также проверяет требуемые методы: NumPy, отсутствие циклов по объектам и вызовов готовых метрик в T1–T4, отсутствие подстановки фиксированных ответов. Нарушение условия обнуляет соответствующую задачу, без отдельного повторного штрафа. Код T2–T3 может зависеть от T1, поэтому сначала исправьте валидацию.

Public checks award full task points only if all its checks pass. The instructor also reviews required methods: NumPy, no per-example loops or prebuilt metrics in T1–T4, no hardcoded answers. A requirement violation invalidates that task's points without an additional duplicate penalty. Fix validation first because T2–T3 may depend on T1.

| Объяснение / Explanation | Баллы / Points |
|---|---:|
| Counts и метрики всех вариантов (3), смысл дисбаланса (2) / Counts and metrics (3), imbalance interpretation (2) | 5 |
| Правильный выбор (2), объяснение ограничения и основной метрики (3) / Correct choice (2), constraint/objective reasoning (3) | 5 |
| Две утечки: за каждую обнаружение (1) + конкретное исправление (2) / Two leaks: identification (1) + concrete fix (2) each | 6 |
| Журнал: данные/версия библиотеки/роль выборки/правило (2), ограничение данных (1), источники и помощь (1) / Log (2), limitation (1), attribution (1) | 4 |
| **Объяснение / Explanation total** | **20** |

Для пункта на 2 балла: 0 — отсутствует/неверно, 1 — частично, 2 — полностью. Для пункта на 3: 0 — нет, 1 — общий ответ без связи с числами, 2 — верная логика с одним существенным пробелом, 3 — полное конкретное объяснение. Пункты на 1 балл: 0/1. / Two-point items: absent/incorrect 0, partial 1, complete 2. Three-point items: absent 0, generic 1, correct with one substantial gap 2, complete and concrete 3. One-point items are binary.

В JSON самопроверки `code_score` максимум 80, `explanation_score` и `total_score` остаются `null` до проверки преподавателем. Это не итоговая оценка курса. Сроки и пересдачи — в Moodle, локального штрафа нет. / Self-check JSON has code_score up to 80; explanation_score and total_score remain null until review. This is not a course-wide grade. Moodle specifies deadlines/resubmissions; no local-clock penalty.

| ID | T1/10 | T2/20 | T3/25 | T4/10 | T5/15 | Объяснение/20 | Всего/100 | Комментарий |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| — | — | — | — | — | — | — | — | — |

Заполненную ведомость храните отдельно от публичного репозитория. / Keep the completed gradebook private.
