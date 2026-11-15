# HW10 — Критерии / Assessment

100 баллов: код 80, объяснения 20. Высокая награда не обязательна; важны корректный контракт, воспроизводимость и честная интерпретация. / 100 points: code 80, explanations 20. High reward is not required; correct contracts, reproducibility and honest interpretation matter.

| Код / Code | Баллы / Points |
|---|---:|
| T1: ε/K всем (5), первый argmax и 1−ε (5), крайние ε и нормировка (5), валидация входов без мутации (5) / Uniform mass, greedy mass/ties, endpoints/normalisation, validation/no mutation | 20 |
| T2: правильная ошибка r−q (5), шаг alpha*x (5), только выбранная строка (5), независимая копия (5) / Correct error, step, selected row only, independent copy | 20 |
| T3: нулевые веса и локальный RNG (4), каждый Train-контекст один раз за эпоху (4), выбор до feedback и один запрос (4), журнал до обновления и выбранная вероятность (4), правильное обновление и воспроизводимость (4) / Initialisation/RNG, epoch coverage, feedback order, pre-update log/propensity, update/reproducibility | 20 |
| T4: greedy-предсказания и награда (5), accuracy/macro-F1 всех классов (5), полная матрица true×predicted (5), заморозка весов и отсутствие fit по Val/Test (5) / Greedy actions/reward, all-class metrics, complete matrix, frozen evaluation | 20 |

Анализ / Analysis:

1. Источник, объект и признаки (1), доступность измерений и метка (1), размеры/непересечение и Train-scaler (1), почему бандит, а не последовательный RL (2). / Source/observation/features (1), availability/target (1), split counts/disjointness/train scaler (1), bandit versus sequential RL (2).
2. Прогноз до candidate (1), шесть фактических validation-результатов и средние (2), корректный выбор с правилом ничьей (1), train reward против frozen reward (1). / Prior hypothesis (1), six actual validation results and means (2), selection/tie rule (1), training versus frozen reward (1).
3. Реальная validation-ошибка: ID/true/action/scores/признаки или честное отсутствие (2), наблюдение отдельно от гипотезы (1), scores не вероятности (2). / Actual failure record or honest absence (2), observation versus hypothesis (1), why scores are not probabilities (2).
4. Три Test-результата и среднее без выбора лучшего (1), два ограничения и отличие от реальных логов (2), следующий эксперимент без подбора по Test (1), источники/AI-помощь (1). / Three final test results and mean (1), two limits and real-log distinction (2), independent follow-up (1), sources/AI disclosure (1).

Для двухбалльного пункта: 2 — полно, 1 — частично, 0 — отсутствует/неверно. Не засчитывать соответствующее требование, если числа скопированы вместо собственного запуска, Test использован для выбора или learner получает полную метку. Самопроверка не заменяет независимую проверку. / Two-point items earn 2/1/0 for complete/partial/missing or incorrect evidence. Do not credit an affected requirement when results are copied, Test informs selection, or the learner receives full labels. Self-checks do not replace independent evaluation.

Срок из живой матрицы группы включительно по Москве. После срока: raw × max(0,1−late/14 суток). Затем при пустой/FALSE отметке P10 множитель 0.9 ровно один раз; TRUE — 1. Неизвестная личность или сбой чтения — уточнение, не автоматический штраф. Лучшие попытки сравниваются после обоих штрафов. / The live group-matrix deadline is inclusive in Moscow time. After it: raw × max(0,1−lateness/14 days). Then apply 0.9 once for blank/FALSE P10, or 1 for TRUE. Unknown identity or failed reading requires clarification, not a default penalty. Compare attempts after both penalties.
