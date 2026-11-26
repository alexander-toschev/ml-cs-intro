# HW10 v2 — Робот / Robot Q-learning

Версия от 26.11.2026: `HW10_Robot_Qlearning_v2`, пять функций одного алгоритма. / Revision of 26 Nov 2026: five functions implementing one algorithm.

80 баллов код + 20 объяснения. / 80 code + 20 explanation points.

| Задание / Task | Код / Code: 16 баллов / points | Объяснение / Explanation: 4 балла / points |
|---|---|---|
| 1 step | Смещения 4; границы/стены 4; награды 4; терминальная цель 4 / Offsets 4; boundaries/walls 4; rewards 4; terminal goal 4 | Цена каждого шага 2; почему длинный путь хуже при прочих равных 2 / Per-step cost 2; longer-route cost 2 |
| 2 choose_action | epsilon-ветка 4; равномерный выбор 4; первый argmax 4; переданный RNG и неизменная Q 4 / Epsilon branch 4; uniform exploration 4; first argmax 4; supplied RNG and unchanged Q 4 | Равные начальные оценки 2; необходимость исследования 2 / Initial ties 2; exploration need 2 |
| 3 update_q | Нетерминальный target 4; terminal без продолжения 4; шаг alpha 4; ровно одна запись на месте 4 / Nonterminal target 4; no terminal continuation 4; alpha update 4; exactly one in-place entry 4 | Конец эпизода 2; отсутствие будущих наград 2 / Episode termination 2; no future rewards 2 |
| 4 train_robot | Сброс позиции и сохранение Q 4; выбор и переход 4; правильное обновление 4; остановка, журнал наград, воспроизводимость 4 / Reset position/retain Q 4; choice/transition 4; update 4; stopping, return log and reproducibility 4 | Сохранение опыта 2; новая попытка из S 2 / Retain experience 2; new attempt from S 2 |
| 5 run_robot | Жадные действия 4; маршрут и награда 4; цель и лимит 4; отсутствие обучения 4 / Greedy moves 4; path/return 4; goal/limit 4; no learning 4 | Проверка без исследования/обновления 2; ограничения переноса 2 / No exploration/update 2; transfer limits 2 |

Код проверять по независимым подпунктам: 4 — выполнено, 2 — частично без подмены задачи, 0 — отсутствует/неверно. Анализ: каждый двухбалльный пункт 2/1/0 (полно/частично/нет). Не обнулять независимые функции из-за ошибки в другой. Сломанный чистый запуск обрабатывать по общим правилам курса с сохранением прежней оценки. / Grade code subcriteria independently: 4 complete, 2 partial, 0 missing/incorrect. Each two-point explanation criterion earns 2/1/0. Do not invalidate independent functions because another fails. Apply the course clean-execution policy while preserving prior approved grades.

Маршрут на той же карте — демонстрация выученной политики, не независимый Test и не доказательство обобщения. Девять ходов в эталонном запуске не жёсткий критерий оценки: проверять алгоритм и честный результат, не зашитый маршрут. Изображение маршрута, выводы и пять коротких ответов должны присутствовать в ноутбуке. Отдельный JSON не требуется. / A route on the training map demonstrates the policy; it is not an independent test or evidence of generalization. Nine moves in the reference run are not a hard grading criterion. Check the algorithm and honest results rather than a hardcoded route. Include the route plot, outputs and five short answers; no separate JSON is required.

## Ранее сданная версия / Previously submitted version
Старый Wine-вариант оценивается исключительно по [ASSESSMENT_Wine_v1.md](ASSESSMENT_Wine_v1.md); шаблон сохранён в [архиве](../../home-work/archive/HW10_RL_Wine_v1.ipynb). Пересдача из-за изменения задания не требуется. Обе версии относятся к ДЗ10 и P10; сравнивать утверждённые попытки после штрафов, не складывать баллы разных версий. / Grade old Wine submissions only under the archived Wine rubric. No resubmission is required due to this revision. Both versions count as HW10/P10; compare approved attempts after penalties, never add their scores.

Сроки и штрафы прежние: raw × max(0,1−late_seconds/1209600), затем ×0.9 при пустой/FALSE отметке P10, ×1 при TRUE. Читать живой лист практики, не менять галочки самостоятельно. / Existing deadlines and penalties: raw × max(0,1−late_seconds/1209600), then ×0.9 for missing P10 or ×1 for TRUE; read live practice marks without changing them.
