## Веб приложение по учету персонала компании

- карточка работника
- создание карточки
- удаление карточки
- редактирование карточки

## API

● GET /api/v1/: Получить список всех карточек (с пагинацией).
● POST /api/v1/: Добавить новую карточку (с картинкой и текстом).
● GET /api/detail/{id}: Получить конкретную карточку по его ID.
● PUT /api/detail/{id}: Обновить существующую карточку.                                        
● DELETE /api/detail/{id}: Удалить карточку.

## Требования:

● Используйте реляционную СУБД для хранения данных.
● Обеспечьте обработку ошибок и валидацию входных данных.
● Используйте Swagger/OpenAPI для документирования API.
● Напишите хотя бы несколько unit-тестов для проверки основной функциональности.
● Напишите Readme, из которого понятна функциональность проекта и инструкция по локальному запуску для разработки.
● Проект должен состоять минимум из:
    - 1 сервис с публичным API
    - 1 сервис с приватным API для изображений
● Напишите docker-compose.yml для запуска проекта. (не сделано)