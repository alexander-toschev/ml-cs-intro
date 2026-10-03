# HW04 · Оценивание / Assessment

100 баллов: код 80, объяснения 20. Практика P04 без отдельной оценки. / 100 points: code 80, explanations 20. P04 is ungraded.

| Раздел / Section | Баллы / Points | Проверяемые компоненты / Components |
|---|---:|---|
| A: данные и split / data and split | 15 | Digits, смысл объектов и просмотр классов — 5; заданный stratified 60/20/20 seed=2026 — 5; полное покрытие без пересечений и все классы — 5 / Digits and inspection 5; specified split 5; coverage, disjointness and labels 5 |
| B: baseline | 10 | LogisticRegression C=1 обучена только на Train — 5; Validation loss и accuracy — 5 / Train-only baseline 5; validation metrics 5 |
| C: обучение / training | 25 | Правильный MLP и 60 эпох partial_fit — 5; история Train/Validation — 5; deepcopy лучшей модели — 10; правильные best_epoch и val_loss — 5 / Model and loop 5; history 5; independent best checkpoint 10; selected epoch and loss 5 |
| D: сравнение / comparison | 20 | Четыре заданных запуска — 5; кривые всех запусков с выбранной эпохой — 5; таблица — 5; выбор по min Validation loss и запись до Test — 5 / Four runs 5; marked curves 5; table 5; validation-based frozen selection 5 |
| E: Test | 10 | Корректные вероятности и метрики baseline — 5; выбранной MLP — 5 / Valid probabilities and metrics: baseline 5, selected MLP 5 |
| F: объяснения / explanations | 20 | Четыре ответа по 5, см. ниже / Four answers worth 5 each |

Компоненты кода оцениваются независимо: полный балл за выполненное требование, 0 за невыполненное. Ошибка выше по ноутбуку не должна автоматически обнулять независимый корректный код ниже. Для checkpoint: условие сравнения и сохранение лучшего состояния — 5, независимая глубокая копия — 5. / Code components are assessed independently, full credit or zero per requirement. An upstream failure must not automatically invalidate independent correct code. Checkpointing: correct comparison and best-state retention 5, independent deep copy 5.

Объяснения / Explanations:

1. Кривые конкретных запусков — 3; обоснование эпохи — 2. / Actual curve evidence 3; epoch rationale 2.
2. Различие loss/accuracy — 3; связь со своими результатами — 2. / Conceptual distinction 3; connection to results 2.
3. Сравнение скоростей при одинаковой ширине — 3; осторожный вывод без выдуманного эффекта — 2. / Matched-width comparison 3; justified interpretation 2.
4. Отсутствие writer ID и ограничение переноса — 3; запрет настройки по Test — 2. / Missing writer IDs and scope limitation 3; no test-based tuning 2.

Для частей по 3: 0 — нет/неверно; 1 — общая фраза; 2 — верно, но неполно; 3 — конкретно и полно. Для частей по 2: 0 — нет/неверно; 1 — частично; 2 — полно. / Three-point items: absent/incorrect 0, generic 1, correct but incomplete 2, specific and complete 3. Two-point items: absent/incorrect 0, partial 1, complete 2.

Самопроверка — структурная, не итоговая оценка. Преподаватель отдельно проверяет графики, объяснения, протокол и отсутствие утечки. Если выбор сделан по Test, компонент выбора D и оценка выбранной MLP в E не считаются корректным экспериментом; независимые пункты оцениваются отдельно. / Self-checks are structural, not a grade. Figures, explanations and protocol require review. Test-based selection invalidates D's selection component and E's selected-model evaluation; independent components remain separately assessable.

Не требуется заданная accuracy, обязательно видимое переобучение или победа над baseline. Используйте реальные измерения; не подменяйте результаты. Укажите источники и полученную помощь. Штрафы за сроки и нарушения академической честности применяются по общим правилам курса; здесь новая формула штрафа не вводится. / No target accuracy, mandatory overfitting pattern or baseline victory. Report measured results and acknowledge sources and assistance. Existing course policies govern lateness and academic integrity; no new penalty formula is introduced here.
