# Лекция 03: честный ML-эксперимент / Lecture 03: a valid ML experiment

Продолжение блока «Данные и метрики»: групповые разбиения, подготовка признаков без утечки, baseline, выбор модели и журнал эксперимента. / Continuation of Data and Metrics: group splits, preprocessing without leakage, baselines, model selection, and experiment logs.

1. [Практика P03 — Colab / Practice](https://colab.research.google.com/github/alexander-toschev/ml-cs-intro/blob/main/practise/P03_Experiment.ipynb) — выполненный пример / worked example.
2. [ДЗ HW03 — Colab / Homework](https://colab.research.google.com/github/alexander-toschev/ml-cs-intro/blob/main/home-work/HW03_Experiment.ipynb) — пять функций и объяснение / five functions and explanation.
3. [Оценивание / Assessment](ASSESSMENT.md).

## Запуск / Run

Достаточно Colab CPU и предустановленных NumPy/scikit-learn. Данные генерируются в ноутбуке, скачивание и ключи API не нужны. Проверено на NumPy 2.5.3, scikit-learn 1.9.1; запишите версии своего сеанса. / Colab CPU with NumPy/scikit-learn is sufficient. Data is generated in the notebook, without downloads or API keys. Tested with NumPy 2.5.3 and scikit-learn 1.9.1; record your session's versions.

Откройте практику, выполните пример, затем решите HW03. Перед сдачей: Restart and Run all. Укажите ФИО и группу, оставьте выводы и объяснение, назовите файл `Group_Surname_HW03.ipynb`. / Run the practice example, then complete HW03. Before submitting, restart and run all cells. Include your name, group, outputs, and explanation; name the file `Group_Surname_HW03.ipynb`.

[Сдача ДЗ / Submit homework](https://drive.google.com/drive/folders/1NNElGtsfynHtIHNngesVgpm71Hi9lkXm). Загрузите файл в свою папку; не меняйте чужие работы. / Upload the file to your folder; do not modify other students' work.

Сроки публикуются преподавателем в [Moodle](https://edu.kpfu.ru/course/view.php?id=6076). Штраф рассчитывается отдельно по подтверждённому времени сдачи принятой версии и утверждённому правилу. Локальные часы ноутбука не используются. / Deadlines are announced by the instructor in Moodle. Penalties are calculated separately using verified submission time and the approved policy, never the notebook's local clock.

Лекции, презентации и видео RU/EN находятся в Google Drive курса. / Russian and English lecture notes, slides, and videos are stored in the course Google Drive.

## Источники / Sources

- [Preprocessing and leakage](https://scikit-learn.org/stable/common_pitfalls.html)
- [GroupShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupShuffleSplit.html) — промышленный аналог; HW03 использует явно заданный алгоритм NumPy / library alternative; HW03 specifies its own NumPy algorithm.
- [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)
- [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
- [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
- [F1 score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html)
