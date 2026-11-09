# CIFAR-10 / CLIP — provenance

Источник / Source: https://www.cs.toronto.edu/~kriz/cifar.html (Alex Krizhevsky, Vinod Nair, Geoffrey Hinton). Используется учебный поднабор реальных фотографий. / A teaching subset of real photographs is used.

Модель / Model: https://huggingface.co/openai/clip-vit-base-patch32 ; pinned revision in manifest.json. Код / Code: https://github.com/openai/CLIP ; paper: https://arxiv.org/abs/2103.00020 .

Каждый NPZ содержит исходные изображения uint8 RGB, исходные ID train:N/test:N, целевые метки, необработанные выходы image encoder и text encoder для bare/photo. Никакие случайные признаки или синтетические изображения не используются. / Each NPZ contains original uint8 RGB images, train:N/test:N IDs, targets, and raw image/text encoder outputs for bare/photo. No random features or synthetic images are used.

Отбор: первые 10 объектов каждого класса для practice, следующие 10 для homework, отдельно из official train (validation) и official test (test). Это 400 изображений, четыре файла по 100. Отбор детерминированный, не репрезентативный benchmark. Совпадения авторов/сцен и пересечение с предобучением не исключены. / Select the first ten per class for practice and the next ten for homework, independently from official train (validation) and official test (test). Four files of 100 images total 400 observations. This deterministic subset is not a representative benchmark. Author/scene overlap and pretraining overlap are not ruled out.

SHA256 в manifest.json проверяется ноутбуками. Для пересчёта установите torch, transformers==4.46.3, pillow, numpy, huggingface_hub и выполните `python recompute_features.py` из этой папки. Это скачает официальный архив и веса модели; вычисление на CPU занимает больше времени, чем сама практика. / Notebooks verify SHA256 hashes from manifest.json. To recompute, install torch, transformers==4.46.3, pillow, numpy, huggingface_hub and run `python recompute_features.py` here. It downloads the official archive and model weights; CPU extraction takes longer than the practice itself.

CIFAR-10 не распространяется под лицензией кода репозитория автоматически; условия исходного набора и модели применяются отдельно. / The repository’s code license does not automatically relicense CIFAR-10; original data and model terms apply separately.
