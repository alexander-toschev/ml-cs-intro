# Лекция 02. Данные и метрики / Lecture 02. Data and metrics

Лекции, презентации, видео RU/EN хранятся в Google Drive. Здесь практика, ДЗ и оценивание. / Lecture slides, scripts and videos are in Google Drive. This folder holds practice, homework and assessment.

1. [P02: практика в Colab / guided practice](https://colab.research.google.com/github/alexander-toschev/ml-cs-intro/blob/main/practise/P02_Data_Metrics.ipynb) — 90 минут / minutes.
2. [HW02: самостоятельное ДЗ / homework](https://colab.research.google.com/github/alexander-toschev/ml-cs-intro/blob/main/home-work/HW02_Data_Metrics.ipynb) — до 180 минут / up to 180 minutes.
3. [Критерии / Assessment](ASSESSMENT.md) — код 80 + объяснение 20 / code 80 + explanation 20.

Сдача / Submit: выполненный / executed `Группа_Фамилия_HW02.ipynb` в [общую папку / shared folder](https://drive.google.com/drive/folders/1NNElGtsfynHtIHNngesVgpm71Hi9lkXm). Дедлайн / deadline: [Moodle](https://edu.kpfu.ru/course/view.php?id=6076).

P02 обновлена 05.10.2026: реальный **Digits** (scikit-learn/UCI), задача «9 против остальных», визуальные confusion matrix, accuracy/precision/recall/F1, естественный дисбаланс, выбор порога на validation и 7 заданий студентам. Ноутбук RU/EN работает в Colab на CPU; датасет включён в scikit-learn. / P02 updated 2026-10-05: real **Digits** (scikit-learn/UCI), “9 vs the rest”, visual confusion matrices, accuracy/precision/recall/F1, natural imbalance, validation-based threshold selection and 7 student exercises. The RU/EN notebook runs on Colab CPU; data are bundled with scikit-learn.

Ранее выданное HW02 сохраняет исходные условия и критерии оценивания. / Previously issued HW02 retains its original requirements and assessment criteria.

[Предыдущая версия P02 / Previous P02](../../Archive/practise/2026-10-05/P02_Data_Metrics.ipynb) сохранена для истории; для нового занятия используйте ссылку P02 выше. / Archived for reference; use the P02 link above for the current practice.

Темы: разбиение train/validation/test, утечка, матрица ошибок, accuracy/precision/recall/F1, baseline, порог и выбор по ограничению. / Topics: splits, leakage, confusion matrix, metrics, baseline, thresholds and constrained selection.

## Источники / Sources

- [scikit-learn: metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [scikit-learn: common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html)
- [train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
