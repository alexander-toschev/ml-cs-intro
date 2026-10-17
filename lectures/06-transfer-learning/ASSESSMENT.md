# HW06 — Оценивание / Assessment

100 баллов: код 80 + объяснения 20. / 100 points: code 80 + explanations 20.

| Задача / Task | Баллы / Points | Контракт / Contract |
|---|---:|---|
| T1 Split | 15 | Заданный порядок вызовов одного RNG, классы 0…9, точные размеры и порядок ID, отсутствие пересечения Train/Validation / Specified single-RNG call order, classes 0…9, exact counts and ID order, disjoint Train/Validation |
| T2 Features | 20 | Переданный transform, eval, inference_mode, порядок ids, конечная матрица (N,576), неизменные параметры и буферы / Supplied transform, eval, inference_mode, ids order, finite (N,576) matrix, unchanged parameters and buffers |
| T3 Head | 15 | StandardScaler + LogisticRegression с заданными параметрами, fit только на переданных Train / Specified scaler and classifier, fit on supplied Train only |
| T4 Selection | 15 | Максимум val_macro_f1, точное равенство: меньшее C, вход неизменён / Max val_macro_f1, exact tie: smaller C, no input mutation |
| T5 Predict | 15 | Контракт входа, ValueError, корректная обработка, class_id/label/10 вероятностей, classes_ / Input contract, ValueError, correct processing, class_id/label/10 probabilities, classes_ mapping |

За каждую функцию: полный балл при выполнении контракта, иначе 0. Проверяются дополнительные случаи и реализация, не только вывод самопроверки. Не требуются дополнительные проверки входа, которые явно не указаны в задании. Независимые функции оцениваются независимо. / Each function receives full credit if its contract is met, otherwise zero. Additional cases and implementation are reviewed, not only self-check output. Extra input checks beyond the task contract are not required. Independent functions are assessed independently.

| Объяснение / Explanation | Распределение 5 баллов / Allocation of 5 points |
|---|---|
| 1. Данные / Data | Источник (1), объект и доступность пикселей (1), counts всех частей (2), ограничение переноса (1) / Source (1), observation and pixel availability (1), all split counts (2), generalization limitation (1) |
| 2. Эксперимент / Experiment | Три validation-результата (1), правильный выбор и аргумент (2), финальные Test baseline/transfer и интерпретация (2) / Three validation results (1), correct selection and rationale (2), final baseline/transfer Test and interpretation (2) |
| 3. Ошибка / Error | Изображение и ID Validation (1), истинный/предсказанный классы (1), score выбранного класса (1), наблюдение (1), проверяемая гипотеза (1) / Validation image and ID (1), true/predicted classes (1), predicted-class score (1), observation (1), testable hypothesis (1) |
| 4. Система / System | Полный latency и условия (2), риск training/serving (1), freeze/fine-tuning (1), источники и AI-помощь (1) / Full latency and conditions (2), training/serving risk (1), freeze versus fine-tuning (1), sources and AI assistance (1) |

Для двухбалльного пункта: 2 — полно и верно, 1 — частично верно без ключевой ошибки, 0 — отсутствует или неверно. Если Validation не содержит ошибок, для пункта 3 достаточно подтверждения по всем validation-предсказаниям (3), корректной интерпретации (1) и гипотезы следующей независимой проверки (1). / Two-point items: complete and correct 2; partially correct 1; absent or incorrect 0. If Validation has no errors, item 3 accepts evidence across all validation predictions (3), correct interpretation (1) and a follow-up independent evaluation hypothesis (1).

Низкая метрика и проигрыш baseline сами по себе не снижают балл. Использование Test для выбора параметров лишает баллов за выбор и финальную оценку в объяснении 2; код оценивается отдельно. / Low performance and losing to the baseline do not reduce credit by themselves. Using Test for selection invalidates selection and final-evaluation points in explanation 2; code remains assessed separately.

Срок берётся из живой матрицы группы. После срока: `итог = raw × max(0, 1 − просрочка_в_сутках / 14)`. Дополнительного бесплатного периода после даты матрицы нет. Время сдачи подтверждается событием Google Drive, а не локальной датой ноутбука. / The live group matrix defines the deadline. Afterwards: `final = raw × max(0, 1 − lateness_in_days / 14)`. No extra penalty-free period follows the matrix date. Submission time comes from a verified Google Drive event, not a local notebook timestamp.
