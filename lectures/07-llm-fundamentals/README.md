# 07 — Основы LLM / LLM fundamentals

Токены и контекст, Transformer, предобучение и instruction tuning, генерация, zero-shot/few-shot, формат ответа и оценивание. / Tokens and context, Transformer, pretraining and instruction tuning, generation, zero-/few-shot, output contracts and evaluation.

- [Практика RU/EN / Practice](../../practise/P07_LLM_Fundamentals.ipynb) · [Colab](https://colab.research.google.com/github/alexander-toschev/ml-cs-intro/blob/main/practise/P07_LLM_Fundamentals.ipynb)
- [Отдельное ДЗ7 RU/EN / Separate homework](../../home-work/HW07_LLM_Fundamentals.ipynb) · [Colab](https://colab.research.google.com/github/alexander-toschev/ml-cs-intro/blob/main/home-work/HW07_LLM_Fundamentals.ipynb)
- [Слайды, видео и аудио RU/EN / Slides, video and audio](https://drive.google.com/drive/folders/1uKEe2r6H4jNV5lUbDPqHLFvzovGV5CAe)
- [Оценивание / Assessment](ASSESSMENT.md)

Реальные данные: [AG News](https://huggingface.co/datasets/SetFit/ag_news). Объект — статья, признак — её текст при поступлении, цель — World/Sports/Business/Sci/Tech. Демонстрации и Validation берутся из official train, Test — из official test; точные дубликаты исключаются. 4 + 16 + 16 объектов; это учебный поднабор, не benchmark. Нет гарантии независимости событий, авторов или пересечения с предобучением. / Real articles, arrival-time text as input, four news topics as targets. Demonstrations and validation use official train, final test uses official test; exact duplicates are excluded. A 4 + 16 + 16 teaching subset is not a benchmark; event/author independence and pretraining overlap are unknown.

Модель [FLAN-T5-small](https://huggingface.co/google/flan-t5-small), CPU Colab без API-ключей. Версии данных и весов закреплены в ноутбуке. Практика использует seed 2026, ДЗ — 2027: результаты практики нельзя переносить в ДЗ. / CPU Colab without API keys; dataset/model revisions are pinned. Practice uses seed 2026, homework uses 2027: do not reuse practice results in homework.

Сдайте только выполненное ДЗ с ФИО, группой, выводами и ответами в [папку сдачи](https://drive.google.com/drive/folders/1NNElGtsfynHtIHNngesVgpm71Hi9lkXm), имя `Group_Surname_HW07.ipynb`. Приложите `llm_experiment.json` внутрь вывода ноутбука либо отдельным файлом с тем же префиксом. Срок — из матрицы группы. / Submit the executed homework with name, group, outputs and answers; include the experiment log in the notebook output or as a matching file. Group deadlines follow the instructor matrix.

Ответы преподавателя хранятся отдельно. / Instructor answers are stored separately.
