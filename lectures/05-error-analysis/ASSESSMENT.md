# HW05 — Оценивание / Assessment

100 баллов: код 80 + исследование 20. / 100 points: code 80 + analysis 20.

| Код / Code | Баллы / Points | Критерий / Criterion |
|---|---:|---|
| T1 | 20 | support, precision, recall, F1 по матрице; NumPy; нулевые знаменатели; вход неизменён / Matrix-derived metrics; NumPy; zero denominators; no mutation |
| T2 | 15 | ID только ошибок в исходном порядке / Error IDs only, original order |
| T3 | 15 | n, errors, rate; пустой срез None / Correct counts and rate; empty slice None |
| T4 | 15 | Максимум validation macro-F1; равенство → baseline / Maximum validation macro-F1; ties retain baseline |
| T5 | 15 | Все поля журнала, версии, Python int ID, JSON / Complete log, actual versions, Python int IDs, JSON |

Задача получает полный балл при выполнении контракта, иначе 0. Валидация входов сверх указанного контракта не требуется. Проверять код и дополнительные случаи, а не только напечатанный score. Не подменять тесты и не прописывать ответы для конкретных массивов. Не обнулять независимые функции из-за одной ошибки. / Each task receives full credit if its contract is met, otherwise zero. Extra input validation beyond the stated contract is not required. Review implementation and additional cases, not only printed scores. Test tampering and hardcoded answers invalidate the affected task; independent tasks remain eligible.

| Исследование / Analysis | Баллы / Points |
|---|---:|
| Counts/recall всех классов (2); слабый класс со знаменателем (1); два ID ошибок, признаки и наблюдение/гипотеза (2) / All class counts/recall (2); weakest class with denominator (1); two error IDs and observation versus hypothesis (2) | 5 |
| Порог alcohol из Train (2); low/high n/errors/rate (2); малые срезы (1) / Training-derived alcohol threshold (2); both slice reports (2); small-slice limitation (1) | 5 |
| Гипотеза до candidate (2); корректный выбор по validation (2); финальный Test и интерпретация (2) / Prespecified hypothesis (2); valid validation selection (2); final test and interpretation (2) | 6 |
| Журнал (1); источник времени Drive (1); источники/AI (1); ограничения Wine (1) / Log (1); Drive timestamp source (1); attribution (1); Wine limitations (1) | 4 |

Для двухбалльного пункта: 2 — полно и правильно, 1 — частично без ключевой ошибки, 0 — отсутствует или неверно. Для пары примеров — по 1 за каждый; если ошибок меньше двух, полный балл возможен при честном указании фактического количества и разборе всех доступных ошибок. / Two-point items: complete and correct 2; partially correct 1; absent or incorrect 0. Error examples earn 1 each; if fewer than two exist, reporting the actual count and analysing all available errors can earn full credit.

Если Test использован для выбора модели, пункты «выбор по validation» и «финальный Test» не засчитываются; код оценивается независимо. Сам по себе низкий F1 или проигрыш baseline не снижает балл. Срок и штраф берутся из действующих правил и матрицы преподавателя; локальная дата не является временем сдачи. / If test data guide selection, selection and final-test analysis points are invalid, while code is assessed independently. Low F1 or losing to baseline alone does not reduce credit. Deadlines and penalties follow the instructor policy and live matrix; local notebook time is not submission time.
