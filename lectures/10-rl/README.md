# Лекция 10 — Обучение с подкреплением / Lecture 10 — Reinforcement learning

Агент, среда, политика, награда, возврат, Q-learning и контекстный бандит. Практика использует реальные Digits, ДЗ — реальные Wine. Награда 1[action==label] задана учебным протоколом, действия не меняют будущие контексты. Это не промышленный журнал взаимодействий и не последовательное управление. / Agent, environment, policy, reward, return, Q-learning and contextual bandits. Practice uses real Digits; homework uses real Wine. A teaching protocol defines reward 1[action==label]; actions do not affect future contexts. This is not an operational interaction log or sequential control.

- [P10: практика / practice](../../practise/P10_RL.ipynb) · [Colab](https://colab.research.google.com/github/alexander-toschev/ml-cs-intro/blob/main/practise/P10_RL.ipynb)
- [HW10: домашняя работа / homework](../../home-work/HW10_RL.ipynb) · [Colab](https://colab.research.google.com/github/alexander-toschev/ml-cs-intro/blob/main/home-work/HW10_RL.ipynb)
- [Критерии / Assessment](ASSESSMENT.md)
- [Слайды и сценарии RU/EN / Slides and scripts](https://drive.google.com/drive/folders/16QP9_phlrHZ6fHqyARGnoOhBEEuehmlY)

Четыре блока: материал → пример → подробное задание → решение студента → проверка. / Four blocks: material → example → detailed task → student solution → check.

1. ε-greedy: нормированные вероятности, первый argmax при равенстве. / Normalised probabilities, first-argmax ties.
2. Обновление только выбранного действия по скалярной награде. / Update only the chosen action from scalar reward.
3. Воспроизводимое обучение и журнал событий только на Train. / Reproducible training and interaction logs on Train only.
4. Оценка замороженной политики, метрики и confusion matrix. / Frozen-policy evaluation, metrics and confusion matrix.

Colab CPU: NumPy, pandas, matplotlib, scikit-learn; датасеты встроены, GPU и внешняя загрузка не нужны. После решения выполните Restart and Run all. / Colab CPU: NumPy, pandas, matplotlib, scikit-learn; bundled datasets require neither GPU nor external downloads. Restart and Run all after completing the tasks.

Train/Validation/Test: стратифицированное разбиение 60/20/20 с округлением размеров; scaler обучается только на Train. Два epsilon, три заранее заданных seed; выбор по средней validation-награде, точная ничья сохраняет 0.1. Все три выбранных запуска оцениваются на Test без выбора лучшего. / Stratified 60/20/20 split with integer rounding; fit scaler only on Train. Two epsilon values and three prespecified seeds; choose by mean validation reward, exact ties keep 0.1. Evaluate all three selected runs on Test without choosing a winner.

Источники / Sources: [Digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html), [Wine](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html), [Sutton & Barto](https://www.incompleteideas.net/book/bookdraft2018mar21.pdf).
