# Лекция 06 — Перенос обучения и ML-системы / Transfer learning and ML systems

Цель: сравнить пиксельный baseline с замороженными признаками нейросети и собрать проверяемую функцию предсказания. / Goal: compare a pixel baseline with frozen pretrained features and build a testable prediction function.

1. [Практика P06 / Practice in Colab](https://colab.research.google.com/github/alexander-toschev/ml-cs-intro/blob/main/practise/P06_Transfer_Learning.ipynb): готовый пример и пять заданий для групп. / A worked example and five group exercises.
2. [ДЗ HW06 / Homework in Colab](https://colab.research.google.com/github/alexander-toschev/ml-cs-intro/blob/main/home-work/HW06_Transfer_Learning.ipynb): пять функций, заданный эксперимент и объяснения. / Five functions, a prescribed experiment and explanations.
3. [Оценивание / Assessment](ASSESSMENT.md): код 80, исследование 20. / Code 80, analysis 20.

Оба ноутбука полностью двуязычные и рассчитаны на Colab CPU. Первый запуск скачивает CIFAR-10 (~163 MiB) и MobileNetV3 Small (~10 MiB). Сервер датасета иногда отвечает медленно; при прерывании загрузки повторите ячейку. Бесплатного CPU достаточно, платные API не используются. / Both notebooks have full RU/EN instructions and target Colab CPU. First run downloads CIFAR-10 (~163 MiB) and MobileNetV3 Small (~10 MiB). The dataset server can be slow; rerun the download cell after an interrupted download. A free CPU runtime is sufficient; no paid API is used.

Источник данных: [CIFAR-10, Krizhevsky](https://www.cs.toronto.edu/~kriz/cifar.html). Объект: RGB-изображение 32×32. Признаки доступны при запросе, цель — категория из 10 классов. Train/Validation берутся из official Train, Test — из official Test. Нет ID авторов и времени, поэтому перенос на новых авторов/будущие данные не проверяется. / Source: CIFAR-10. One observation is a 32×32 RGB image; pixels are available at request time, and the target is one of ten categories. Train/Validation come from official Train, Test from official Test. Missing author/time IDs prevent evaluation of generalization to new authors or future observations.

Практика: 600/200/200, seed=2026. ДЗ: 1000/300/300, seed=2027. MobileNetV3 Small IMAGENET1K_V1 выдаёт 576 признаков после замены classifier на Identity. Обучается только новая sklearn-голова. Возможное пересечение источников предобучения и CIFAR не проверено. / Practice: 600/200/200, seed=2026. Homework: 1000/300/300, seed=2027. MobileNetV3 Small IMAGENET1K_V1 yields 576 features after replacing classifier with Identity. Only the new sklearn head is trained. Pretraining/CIFAR source overlap has not been audited.

Практика рассчитана на 60–90 минут, ДЗ на 150–210 минут, без учёта загрузки данных. / Estimated practice: 60–90 minutes; homework: 150–210 minutes, excluding downloads.

Сдайте выполненный `Группа_Фамилия_HW06.ipynb` с выводами ячеек и письменными ответами в [Сдача ДЗ / Submissions](https://drive.google.com/drive/folders/1NNElGtsfynHtIHNngesVgpm71Hi9lkXm). / Submit the executed notebook with cell outputs and written answers.

Срок: [живая матрица группы / live group matrix](https://docs.google.com/spreadsheets/d/1zzedKe77LfubpYsN4gsesqrvGwnb4pAoEuqLpkfNr6A/edit). Пустая дата означает, что срок ещё не установлен. После срока применяется линейное снижение за 14 суток, одинаково для всех. / A blank date means the deadline is not set. After the deadline, credit decreases linearly over 14 days for all students.

[Слайды, озвучка и видео RU/EN / Slides, narration and videos](https://drive.google.com/drive/folders/1G7KhMzN8Por2JYvYjSBa4qhBJpdMItmR) — Google Drive. Видео: RU 14:31, EN 12:34, без добавленных пауз. / Videos: RU 14:31, EN 12:34, without added pauses.
