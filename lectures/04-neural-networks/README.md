# Лекция 04 · Нейросети и обучение / Neural networks and training

1. [P04 — практика в Colab / Practice](https://colab.research.google.com/github/alexander-toschev/ml-cs-intro/blob/main/practise/P04_Neural_Networks.ipynb)
2. [HW04 — ДЗ в Colab / Homework](https://colab.research.google.com/github/alexander-toschev/ml-cs-intro/blob/main/home-work/HW04_Neural_Networks.ipynb)
3. [Критерии оценивания / Assessment](ASSESSMENT.md)

Работаем с **Digits**, известным реальным набором рукописных цифр: 1 797 изображений 8×8, десять классов. Это не MNIST. Источник: [scikit-learn / UCI](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html). Загрузка встроена в scikit-learn; Google Colab CPU достаточно.

We use **Digits**, an established real handwritten-digit dataset: 1,797 images, 8×8 pixels, ten classes. It is not MNIST. The loader is included in scikit-learn; Colab CPU is sufficient.

P04: нормализация известной константой 16, stratified 60/20/20, LogisticRegression, MLP, прямой проход NumPy, кривые и выбор checkpoint. HW04: четыре запуска — hidden width 16/64 × learning rate .001/.01, 60 epochs, batch 64, seed 2026, alpha .0001. Критерий — minimum Validation cross-entropy; Test только после фиксации выбора. Не требуется победа над baseline.

P04 covers fixed-bound normalisation, a stratified split, baseline, MLP, a NumPy forward pass, curves and checkpoint selection. HW04 compares four configurations listed above. Select by validation cross-entropy; evaluate Test only after freezing selection. Beating the baseline is not required.

**Ограничение / Limitation:** загрузчик не предоставляет writer ID. Разбиение по изображениям не доказывает перенос на новых авторов. / The loader supplies no writer IDs; image-level splitting does not establish unseen-writer generalisation.

**Сдача / Submission:** выполненный ноутбук `Группа_Фамилия_HW04.ipynb` / executed `Group_Surname_HW04.ipynb` в [общую папку / shared folder](https://drive.google.com/drive/folders/1NNElGtsfynHtIHNngesVgpm71Hi9lkXm).

**Срок / Deadline:** HW04 в [матрице групп / group matrix](https://docs.google.com/spreadsheets/d/1zzedKe77LfubpYsN4gsesqrvGwnb4pAoEuqLpkfNr6A/edit). Введённая дата окончательная, дополнительный запас не прибавляется; пустая ячейка означает отсутствие назначенной даты. / The entered date is final; no extra grace period is added. A blank cell means no date has been assigned.

Лекции, презентации и видео RU/EN — в [папке курса Google Drive](https://drive.google.com/drive/folders/1sd5YSkWyXfc4UVnCyaqXSlY_WIhjvGIE). / Bilingual lectures, slides and videos are in the course Drive folder.

## Работа в группах / Group practice

P04 рассчитана на 60–90 минут, группы по 2–3 человека. Пять заданий: данные и формы тензоров; baseline и вероятности; гипотеза о learning rate и кривые; прямой проход и checkpoint; реальные ошибки Validation. Заполните ответы и зафиксируйте выбор до Test. Упражнения выполняются в ноутбуке отдельно от видео.

P04 takes 60–90 minutes in groups of 2–3. Five exercises cover data and tensor shapes, baseline probabilities, learning-rate hypotheses and curves, forward pass and checkpoints, and real validation mistakes. Record answers and freeze selection before Test. Exercises are completed in the notebook separately from the video.
