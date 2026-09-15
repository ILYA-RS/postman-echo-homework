# Postman Echo: домашнее задание

Пять интеграционных тестов на Python с `requests` и `pytest`.
Проект проверен на Python 3.12.10. Для запуска используйте Python 3.12 и доступ к интернету.

## Изучение в Postman

1. Импортируйте `postman_echo.postman_collection.json` через Import.
2. Откройте каждый запрос и нажмите Send.
3. Сопоставьте статус и JSON ответа с таблицей ниже.
4. Запишите фактические результаты в `observations.md`.

| Запрос | Что проверяет тест |
| --- | --- |
| GET /get с query-параметрами | Статус 200; `args` содержит переданные строки |
| GET /get с X-Homework | Статус 200; `headers.x-homework` содержит значение заголовка |
| POST /post с JSON | Статус 200; `json` сохраняет значения и типы; Content-Type соответствует JSON |
| POST /post с формой | Статус 200; `form` содержит поля; Content-Type соответствует форме |
| POST /post с текстом | Статус 200; `data` содержит текст; Content-Type соответствует тексту |

Это ожидаемые результаты для проверки, а не отчёт об уже выполненных запросах.
Дополнительно коллекция содержит POST /get и GET /post для изучения других методов.
Их фактические статусы нужно записать после отправки.

## Локальный запуск (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python -m pytest -v
.\.venv\Scripts\python -m pip freeze | Set-Content -Encoding utf8 requirements.txt
```

Каждый запрос ограничен таймаутом 20 секунд. Ошибки сети или сервиса
приведут к падению теста. Тесты обращаются к настоящему серверу.

## GitHub и CI

Создайте новый пустой публичный репозиторий. Выполняйте команды из этой папки,
заменив OWNER и REPOSITORY своими значениями:

```powershell
git init -b main
git add .gitignore README.md requirements.txt test_echo.py postman_echo.postman_collection.json observations.md
git commit -m "Add Postman Echo API tests"
git remote add origin https://github.com/OWNER/REPOSITORY.git
git push -u origin main
```

Для выполнения пункта о скачивании удалённого коммита добавьте workflow
через сайт GitHub: Add file → Create new file → `.github/workflows/tests.yml`.
Вставьте содержимое `ci-workflow.yml.example` и сохраните коммит в main.
Вкладка Actions должна показать успешный запуск и пять пройденных тестов
в шаге Run tests. Затем скачайте этот коммит:

```powershell
git pull --ff-only origin main
```

## Демонстрация падения и исправления

1. В `test_get_query_parameters` замените ожидаемый статус `200` на `201`.
2. Сохраните и отправьте изменение:

```powershell
git add test_echo.py
git commit -m "Demonstrate failing status assertion"
git push
```

3. Дождитесь завершения Actions. В логах должен быть `AssertionError`
   именно из-за сравнения фактического 200 с ожидаемым 201.
4. Верните `200` и отправьте исправление:

```powershell
git add test_echo.py
git commit -m "Fix expected response status"
git push
```

5. Дождитесь зелёного запуска и сохраните ссылки на все три запуска CI
   в `observations.md`. Не отправляйте исправление до завершения красного запуска.

## Статус подготовки

Локальная проверка выполнена: 5 passed in 2.88s. Версии установленных
зависимостей сохранены в requirements.txt. В Postman вручную проверены два GET-запроса; остальные ручные проверки пропущены. Настройка CI и демонстрация падения и исправления ещё предстоят.

