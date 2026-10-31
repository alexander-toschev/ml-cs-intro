# HW08 — 100 баллов / points

| Часть / Part | Баллы / Points | Критерий / Criterion |
|---|---:|---|
| T1 ranking | 20 | Порядок score, tie по ID, границы k, входы неизменны / Score ordering, ID ties, k boundaries, no mutation |
| T2 retrieval | 20 | Hit@k, MRR@k, n, отсутствие эталона / Correct Hit@k, MRR@k, n and missing-reference handling |
| T3 packing | 20 | Полные абзацы, полный токенный бюджет, правильные ID и ValueError / Whole passages, full prompt budget, correct IDs and ValueError |
| T4 answer metrics | 20 | EM/F1, кратность, несколько эталонов, пустые ответы / EM/F1, multiplicity, multiple references and empty answers |
| Анализ / Analysis | 20 | Четыре подробно описанных пункта по 5 / Four detailed notebook analysis items, five points each |

Высокий F1 не является условием оценки. Нужны корректный эксперимент, честная интерпретация, источники и раскрытие AI-помощи. Не изменяйте проверки и не выбирайте настройки по Test. / High F1 is not required. A valid experiment, honest interpretation, sources and AI disclosure are required. Do not edit checks or tune on test.

Штраф за опоздание / Late penalty: `final = raw * max(0, 1 - late_seconds / (14 * 86400))`. От подтверждённого срока группы, по серверному времени сдачи; без дополнительного запаса. / From the confirmed group deadline, using server submission time, with no extra grace period.
