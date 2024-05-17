## Дипломный проект. Задание 2: API-тесты

### Автотесты для проверки API сайта https://stellarburgers.nomoreparties.site

### Реализованные сценарии

Созданы тесты, покрывающие API методы работы с заказами и пользователями 

### Структура проекта

- `allure_results` - Allure отчет
- `tests` - пакет, содержащий тесты, разделенные по классам.

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

#### Запуск тестов
`pytest tests/ --alluredir=allure_results`
#### Запуск отчетности allure
`allure serve allure_results`
