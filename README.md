# apps
ЗАПУСК ПРИЛОЖЕНИЯ:
1. Сначало нужно сформировать env-файл с переменными (существует два варианта):

   1) Для прода: cat .env.prod > .env
   2) Для дева: cat .env.dev > .env
2. Для запуска приложения нужно набрать команду docker-compose up app или docker-compose up -d app

API:
Предпологается делать запросы curl в данном случае
1. Авторизация:
    1) curl -X POST -H "Content-Type: application/json" -d '{"username": "admin", "password": "admin"}' http://localhost:8000/api/token/
    Получаем в ответ JSON со структурой  {"refresh": "String", "access": "String"}
    Сохраняем значение которое лежит в поле access
2. Добавление приложения:
    1) curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg1NjU1ODczLCJqdGkiOiIwYzU4MTYwMmQ3OWE0MTVjOWJlNjEyZjQ4NTVhZGM4YyIsInVzZXJfaWQiOjF9.ka--iLPt1iWytxGi3FUlIegHbtk9Krrsnu_7nf4qsg0" -d '{"name": "First app", "key_api": "Key API"}' http://localhost:8000/api/apps/
    POST-запрос, указываем необходимые заголовки, токен авторизации и данные для нашего приложения
3. Получение приложений:
    1) curl -X GET -H "Content-Type: application/json" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg1NjU2NTE3LCJqdGkiOiIxYTBkZDJmMGE2ZWY0OTk4OWVhYjk5ZTdhMmMzOTkwYiIsInVzZXJfaWQiOjF9.DtzCbesI2Kitw-i96GTbYyYWMOLermdKFGcW_gUTDfc" http://localhost:8000/api/apps/
    GET-запрос, указываем необходимые заголовки, токен авторизации и получаем список приложений
4. Обновления имени приложения:
    1) curl -X PUT -H "Content-Type: application/json" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg1NjU2OTg5LCJqdGkiOiI1YTY1YzdkOTU4MmU0ZDI0ODBlOGEzM2RjMWEyODhmMyIsInVzZXJfaWQiOjF9.aO7nSRRaIeLvQdmvRQvphTJFqgU-MQld0CtfKM2eb4U" -d '{"name": "First APP"}' http://localhost:8000/api/apps/1/
    PUT-запрос, указываем необходимые заголовки, токен авторизации, обновленные поля и id приложения в конце урла для обновления
5. Обновления имени приложения:
    1) curl -X PUT -H "Content-Type: application/json" -H "Authorization: BearoiYWNjZXNzIiwier eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjZXhwIjoxNTg1NjU2OTg5LCJqdGkiOiI1YTY1YzdkOTU4MmU0ZDI0ODBlOGEzM2RjMWEyODhmMyIsInVzZXJfaWQiOjF9.aO7nSRRaIeLvQdmvRQvphTJFqgU-MQld0CtfKM2eb4U" -d '{"key_api": "Key APIAPI"}' http://localhost:8000/api/apps/1/update_key_api/
    PUT-запрос, указываем необходимые заголовки, токен авторизации, обновленные поля и id приложения в конце урла для обновления
6. Получение информации по приложению с помощью key api:
    1) curl -X GET -H "Content-Type: application/json" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg1NjYwNDg1LCJqdGkiOiI3YWY0Y2I0MDUzYjk0ZTYxOGQ2ZmMyNDYxZjg2Mzg2NSIsInVzZXJfaWQiOjF9.DX2xUfsbjP47PnX-rNDVH7zCB5960us05ppyTOAfZbY" http://localhost:8000/api/apps/test/?key_api=KeyAPI
    GET-запрос, указываем необходимые заголовки, токен авторизации, и key_api для получения объекта приложения
6. Удаление приложения:
    1) curl -X DELETE -H "Content-Type: application/json" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg1NjU2OTg5LCJqdGkiOiI1YTY1YzdkOTU4MmU0ZDI0ODBlOGEzM2RjMWEyODhmMyIsInVzZXJfaWQiOjF9.aO7nSRRaIeLvQdmvRQvphTJFqgU-MQld0CtfKM2eb4U" http://localhost:8000/api/apps/1/
    DELETE-запрос, указываем необходимые заголовки, токен авторизации, id приложения в конце урла для удаления
