# SQuAD 2.0 teaching subsets / Учебные поднаборы

Source: https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v2.0.json
Dataset authors: Pranav Rajpurkar, Robin Jia, Percy Liang; Stanford SQuAD project.
License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). These redistributed subsets retain that license. Wikipedia source text remains subject to its source attribution/license obligations.

Изменение: выбор поднабора и добавление ID/ролей разбиения; исходные абзацы, вопросы и ответы не переписаны. / Modification: subset selection and added IDs/split roles; original paragraphs, questions and answers are unchanged.

`practice-squad2.json`: Normans, Computational complexity theory, Southern California, Sky (United Kingdom).
`homework-squad2.json`: Victoria (Australia), Huguenot, Steam engine, Oxygen.

Each: 48 paragraphs, 24 answerable questions, four additional paragraph-specific unanswerable examples for optional inspection. First two articles validation, last two test. Full selection description and source SHA-256 are embedded in each JSON. This is not the official full benchmark. Questions are correlated within articles; short-paragraph selection is biased; model pretraining overlap is unknown. The fixed collection includes test-source documents, while test questions and labels are held out from selection.

В каждом файле 48 абзацев, 24 ответимых вопроса и 4 дополнительных вопроса без ответа в своём абзаце. Первые две статьи — Validation, последние две — Test. Это не полный benchmark; вопросы внутри статьи зависимы, отбор коротких абзацев смещён, пересечение с предобучением неизвестно. База содержит документы Test, но test-вопросы и эталоны не участвуют в выборе настроек.
