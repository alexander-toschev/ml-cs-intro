# Лекция 05 — Анализ ошибок / Error analysis

Цель: перейти от общей метрики к проверяемой гипотезе улучшения. / Goal: move from an overall metric to a testable improvement hypothesis.

1. [Практика P05 — Digits / Practice](https://colab.research.google.com/github/alexander-toschev/ml-cs-intro/blob/main/practise/P05_Error_Analysis.ipynb): матрица ошибок, ручной просмотр, срезы, сравнение 1-NN и 5-NN. / Confusion matrices, manual inspection, slices, 1-NN versus 5-NN.
2. [ДЗ HW05 — Wine / Homework](https://colab.research.google.com/github/alexander-toschev/ml-cs-intro/blob/main/home-work/HW05_Error_Analysis.ipynb): показатели классов, ID ошибок, срез alcohol, сравнение глубины дерева 2 и 4. / Class metrics, error IDs, alcohol slice, tree depths 2 versus 4.
3. [Оценивание / Assessment](ASSESSMENT.md): код 80, исследование 20; улучшение метрики не обязательно. / Code 80, analysis 20; improvement is not required.

Оба ноутбука двуязычные, для Colab CPU; данные входят в sklearn, отдельная загрузка или GPU не нужны. / Both notebooks have full RU/EN instructions and run on Colab CPU using datasets bundled with sklearn.

Практика: 60–90 минут. ДЗ: 120–180 минут. / Practice: 60–90 minutes. Homework: 120–180 minutes.

Источники / Sources: [Digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html), [Wine](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html). Никакой генерации синтетических объектов. Нет ID авторов в Digits и партий/производителей в Wine: разбиение по наблюдениям не проверяет новые группы. / No synthetic observations. Writer IDs in Digits and batch/producer IDs in Wine are unavailable; sample splits do not evaluate unseen groups.

[Слайды, сценарии, озвучка и видео RU/EN / Slides, scripts, narration and videos](https://drive.google.com/drive/folders/1tdmrsBMP_Nn3Jmu9FPZAMalPy108f4es) — Google Drive «ВведениеПИ / Лекция 05». Видео по 30 минут, включая паузы на упражнения. / Each video is 30 minutes including exercise pauses.

Сдайте выполненный ноутбук `Группа_Фамилия_HW05.ipynb` в [Сдача ДЗ / Submissions](https://drive.google.com/drive/folders/1NNElGtsfynHtIHNngesVgpm71Hi9lkXm). Срок — в [матрице по группам / group deadline matrix](https://docs.google.com/spreadsheets/d/1zzedKe77LfubpYsN4gsesqrvGwnb4pAoEuqLpkfNr6A/edit). / Upload the executed notebook with your name and group. Use the group deadline matrix; no deadline is invented in the notebook.
