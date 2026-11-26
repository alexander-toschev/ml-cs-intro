# Лекция 10 — Обучение с подкреплением / Lecture 10 — Reinforcement learning

Агент, среда, политика, награда, возврат, Q-learning и контекстный бандит. Практика P10 использует реальные Digits. ДЗ10 от 26.11.2026 — пять небольших функций Q-learning для робота на явно заданной учебной полосе препятствий. / Agent, environment, policy, reward, return, Q-learning and contextual bandits. P10 uses real Digits. HW10 revised on 26 Nov 2026 contains five small Q-learning functions for a robot in an explicitly defined teaching obstacle course.

- [P10: практика / practice](../../practise/P10_RL.ipynb) · [Colab](https://colab.research.google.com/github/alexander-toschev/ml-cs-intro/blob/main/practise/P10_RL.ipynb)
- [HW10: домашняя работа / homework](../../home-work/HW10_RL.ipynb) · [Colab](https://colab.research.google.com/github/alexander-toschev/ml-cs-intro/blob/main/home-work/HW10_RL.ipynb)
- [Критерии / Assessment](ASSESSMENT.md)
- [Слайды и сценарии RU/EN / Slides and scripts](https://drive.google.com/drive/folders/16QP9_phlrHZ6fHqyARGnoOhBEEuehmlY)

## Новое ДЗ10: робот / Revised HW10: robot

Пять блоков: шаг среды → выбор движения → обновление Q → обучение → маршрут без обучения. Перед каждой функцией есть простое объяснение, пример, пошаговое задание, каркас и проверка. CPU, NumPy и matplotlib. / Five blocks: environment step → action selection → Q update → training → frozen route evaluation. Each has plain explanation, an example, step-by-step instructions, scaffold and checks. CPU, NumPy and matplotlib.

Это симуляция, а не реальный датасет. Проверка на той же карте демонстрирует алгоритм, но не перенос на новые карты. / This is a simulation, not a real dataset; evaluating the same map demonstrates the algorithm without establishing transfer.

Ранее сданные работы Wine сохраняют [свою рубрику](ASSESSMENT_Wine_v1.md) и [шаблон](../../home-work/archive/HW10_RL_Wine_v1.ipynb); обязательной пересдачи нет. / Previous Wine submissions retain their rubric and template; no resubmission is required.

## Практика P10 / Practice P10

Четыре блока: материал → пример → подробное задание → решение студента → проверка. / Four blocks: material → example → detailed task → student solution → check.

1. ε-greedy: нормированные вероятности, первый argmax при равенстве. / Normalised probabilities, first-argmax ties.
2. Обновление только выбранного действия по скалярной награде. / Update only the chosen action from scalar reward.
3. Воспроизводимое обучение и журнал событий только на Train. / Reproducible training and interaction logs on Train only.
4. Оценка замороженной политики, метрики и confusion matrix. / Frozen-policy evaluation, metrics and confusion matrix.

Colab CPU: NumPy, pandas, matplotlib, scikit-learn; датасеты встроены, GPU и внешняя загрузка не нужны. После решения выполните Restart and Run all. / Colab CPU: NumPy, pandas, matplotlib, scikit-learn; bundled datasets require neither GPU nor external downloads. Restart and Run all after completing the tasks.

Train/Validation/Test: стратифицированное разбиение 60/20/20 с округлением размеров; scaler обучается только на Train. Два epsilon, три заранее заданных seed; выбор по средней validation-награде, точная ничья сохраняет 0.1. Все три выбранных запуска оцениваются на Test без выбора лучшего. / Stratified 60/20/20 split with integer rounding; fit scaler only on Train. Two epsilon values and three prespecified seeds; choose by mean validation reward, exact ties keep 0.1. Evaluate all three selected runs on Test without choosing a winner.

Источники / Sources: [Digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html), [Wine](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html), [Sutton & Barto](https://www.incompleteideas.net/book/bookdraft2018mar21.pdf).
