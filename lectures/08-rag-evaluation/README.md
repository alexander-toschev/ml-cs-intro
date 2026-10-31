# 08 — RAG и оценка ответов / RAG and answer evaluation

[Лекции, слайды, видео RU/EN / Lectures, slides and videos](https://drive.google.com/drive/folders/1whFBXtuBvkXNHNg_w2GjXRxCPbsc3nmr)

1. [Практика P08 / Practice in Colab](https://colab.research.google.com/github/alexander-toschev/ml-cs-intro/blob/main/practise/P08_RAG_Evaluation.ipynb)
2. [ДЗ HW08 / Homework in Colab](https://colab.research.google.com/github/alexander-toschev/ml-cs-intro/blob/main/home-work/HW08_RAG_Evaluation.ipynb)
3. [Оценивание / Assessment](ASSESSMENT.md)

Реальные вопросы SQuAD 2.0; TF-IDF, Hit@k, MRR, ограничение контекста, FLAN-T5-small, Exact Match и token F1. Практика и ДЗ используют разные статьи. / Real SQuAD 2.0 questions; TF-IDF, Hit@k, MRR, context budgets, FLAN-T5-small, Exact Match and token F1. Practice and homework use different articles.

Практика: ровно 4 блока «материал → пример → задание → решение студента → проверка». CPU Colab, без API-ключа. Первый запуск требует интернета для зависимостей и модели. / Exactly four interleaved practice blocks: explanation → worked example → task → student solution → executable check. CPU Colab; no API key. Initial installation and model download require internet.

Сдайте только ДЗ: выполненный ipynb и JSON-журнал в свою папку [сдачи](https://drive.google.com/drive/folders/1NNElGtsfynHtIHNngesVgpm71Hi9lkXm). Имя: `Группа_Фамилия_HW08.ipynb`. Срок задаётся в матрице группы. / Submit only homework: the executed notebook and JSON log to your submission folder. Name: `Group_Surname_HW08.ipynb`. Use the deadline in the group matrix.

Данные / Data: [SQuAD 2.0](https://rajpurkar.github.io/SQuAD-explorer/), CC BY-SA 4.0. Подробнее о происхождении, отборе и ограничениях: [data/rag](../../data/rag/README.md).
