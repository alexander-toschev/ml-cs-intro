# P01. Постановка задачи / Problem formulation

**Объём:** 2 академических часа (90 минут). **Результат:** файл `P01_<фамилия>.md` или PDF на 1–2 страницы. Работа индивидуальная; обсуждение в паре допустимо.

## Задание

1. **0–10 минут:** выберите пользователя и реальную задачу. Стартовые темы: помощник по материалам курса (LLM), извлечение даты/места из афиш (VLM), навигация по клеточной карте (RL). Можно предложить свою тему сходного объёма.
2. **10–25 минут:** опишите вход и выход. Приведите три конкретных примера; включите один сложный случай или запрос, который система не должна выполнять.
3. **25–40 минут:** предложите baseline — простое сравнимое решение. Например, поиск по ключевым словам; ручные правила обработки уже распознанного текста; фиксированная стратегия движения. Назовите ограничения.
4. **40–60 минут:** определите основную метрику, способ её вычисления и одно ограничение. Например, доля правильных ответов с опорой на документ; точность извлечения полей; доля достижения цели и число шагов. Задайте правило, по которому отдельный пример считается успешным.
5. **60–75 минут:** наметьте источник данных и проверку. Опишите, какие примеры пойдут на разработку и какие останутся для итоговой проверки. Для RL используйте отдельные сценарии среды и несколько запусков.
6. **75–90 минут:** обменяйтесь описаниями, найдите одну неоднозначность и исправьте её. Запишите замечание и изменение. При индивидуальной работе выполните такую же самопроверку.

## Шаблон ответа

- Автор и группа:
- Пользователь и его потребность:
- Вход → выход (три примера):
- Baseline и ограничения:
- Основная метрика и правило успешности:
- Дополнительное ограничение:
- Данные и план разделения:
- Полученное замечание и внесённое исправление:

Оценка: до 10 баллов по [рубрике](ASSESSMENT.md). Код и готовый датасет на этом этапе не нужны.

---

## English

**Time:** 90 minutes (2 academic hours). **Deliverable:** `P01_<surname>.md` or a 1–2 page PDF. Submit individually; pair discussion is allowed.

1. **0–10 min:** choose a user and a real problem. Suggested tracks: an assistant for course materials (LLM), date/location extraction from posters (VLM), or grid navigation (RL). A similarly scoped original topic is welcome.
2. **10–25 min:** define inputs and outputs. Give three concrete examples, including one difficult case or unsupported request.
3. **25–40 min:** propose a simple, comparable baseline: keyword retrieval, rules over already recognised text, or a fixed navigation policy. State its limitations.
4. **40–60 min:** define a primary metric, its calculation and one constraint. Examples: supported correct-answer rate, field extraction accuracy, or goal success rate with a step limit. Specify how a single example passes or fails.
5. **60–75 min:** identify a data source and evaluation plan. Separate development examples from final evaluation examples. For RL, use separate environment scenarios and multiple runs.
6. **75–90 min:** exchange specifications, identify an ambiguity and correct it. Record the feedback and revision. If working alone, perform the same review yourself.

Use these headings: author/group; user need; three input/output examples; baseline/limitations; primary metric/pass rule; constraint; data/split plan; feedback/revision.

Worth up to 10 points under the [rubric](ASSESSMENT.md). No implementation or complete dataset is required yet.
