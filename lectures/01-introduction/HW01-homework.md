# HW01. Паспорт проекта / Project brief

**Объём:** до 4 академических часов самостоятельной работы (180 минут). **Результат:** `HW01_<фамилия>.md` или PDF на 2–4 страницы. Это развитие P01, а не новый проект. Первая работа сдаётся индивидуально; будущего партнёра можно указать отдельно.

## Что сделать

1. Уточнить постановку задачи по результатам практики: пользователь, полезный результат, вход, выход, границы задачи.
2. Выбрать трек LLM, VLM или RL. Объяснить, почему он подходит; указать, достаточно ли для части задачи простых правил.
3. Описать источник данных и условия их использования. Подготовить **5 примеров с ожидаемыми результатами**. Для RL — 5 сценариев с начальным состоянием, целью и условием завершения. Не включать личные данные, пароли и API-ключи. Примеры можно составить самостоятельно, явно отметив это.
4. Описать baseline и **одно предполагаемое улучшение**. Сформулировать проверяемую гипотезу. Реализовывать и обучать модели сейчас не нужно.
5. Определить метрику и правило подсчёта, ограничение и предварительный критерий успеха. Показать расчёт на своих пяти примерах с **иллюстративными результатами**, явно обозначив, что это не измерения работающей системы.
6. Составить план честного сравнения: одинаковые условия для baseline и улучшения, отдельные данные для итоговой проверки, что фиксировать при запуске. Пять подготовленных примеров служат для разработки задания и не заменяют итоговый тест проекта.
7. Назвать два риска и способ их проверить. Разбить дальнейшую работу на четыре этапа: данные → baseline → улучшение → оценка и анализ ошибок.

## Самопроверка

- [ ] Задача имеет конкретного пользователя, вход и выход.
- [ ] Есть пять примеров или сценариев с ожидаемыми результатами.
- [ ] Источник данных указан; собственные примеры помечены.
- [ ] Baseline и улучшение можно сравнить одной процедурой.
- [ ] Метрика вычислима; иллюстративные числа не выданы за эксперимент.
- [ ] Разработка и итоговая проверка разделены.
- [ ] Указаны риски, этапы, автор и использованные источники/AI-помощь.

До 20 баллов по [рубрике](ASSESSMENT.md). Срок и канал сдачи — в Moodle. Тема предварительная и может быть уточнена с преподавателем.

---

## English

**Time budget:** up to 180 minutes (4 academic hours). **Deliverable:** `HW01_<surname>.md` or a 2–4 page PDF. Extend P01 instead of starting another project. Submit this first assignment individually; you may name a prospective project partner separately.

1. Refine the user need, useful outcome, inputs, outputs and scope using practical-session feedback.
2. Choose LLM, VLM or RL and justify the choice. Identify any part that simple rules could handle.
3. Describe the data source and usage conditions. Prepare **five examples with expected outputs**. For RL, provide five scenarios with initial states, goals and termination conditions. Exclude personal data, passwords and API keys. Clearly label self-created examples.
4. Specify a baseline and **one proposed improvement**, with a testable hypothesis. No implementation or model training is required now.
5. Define a computable metric, a constraint and a provisional success criterion. Demonstrate the metric on the five examples using clearly labelled **illustrative outcomes**, not claimed system measurements.
6. Plan a fair comparison: equal conditions, separate final evaluation data, and recorded run settings. These five development examples do not replace the final project test set.
7. Identify two risks and how to check them. Plan four stages: data → baseline → improvement → evaluation and error analysis.

Before submitting, check that all seven requirements are addressed, calculations are reproducible, and the author, sources and any AI assistance are acknowledged.

Worth up to 20 points under the [rubric](ASSESSMENT.md). See Moodle for the deadline and submission method. The topic is provisional and can be refined with the instructor.
