# Результаты проверки

Ниже записаны фактические результаты. Остальные ручные запросы в Postman пропущены по решению пользователя.

| Запрос в Postman | Фактический статус | Наблюдение |
| --- | --- | --- |
| GET /get с query | Не записан | args содержит name=Alice и page="2" |
| GET /get с заголовком | 200 | headers содержит x-homework=echo-test; args пустой |
| POST /post JSON | — | — |
| POST /post форма | — | — |
| POST /post текст | — | — |
| POST /get | — | — |
| GET /post | — | — |

Локальный pytest: 5 passed in 2.88s (Python 3.12.10).

Репозиторий: https://github.com/ILYA-RS/postman-echo-homework

Первый зелёный CI: —

Красный CI (ошибка ассерта): —

Зелёный CI после исправления: —

