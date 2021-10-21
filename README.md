![picture](https://user-images.githubusercontent.com/49750349/138281701-bccb4779-5bdc-4794-a911-38899cd9eec8.png)
# DemoTelegramBot
<h3>
Демо версия простого телеграмм бота, который разворачивается на Docker
</h3>

# Тестовое задание
Данный проект является тестовым заданием

# Подготовка
Установите Docker/Docker compose

После установки, клонируйте репозиторий и настройте <b>Dockerfile</b>
```dockerfile
ENV TOKEN_BOT=токен_бота
ENV APP_PORT=8443
```
Установите свой <b>TOKEN_BOT</b>

По умолчанию поставлен порт <b>8443</b>, в случае необходимости можете указать свой

<h2>Запуск бота</h2>
Запустите последовательно данные команды. Может выполняться каждая команда около 3-5 минут
```bash
docker-compose build
docker-compose up
```
Если вы увидели данную надпись, значит бот запущен и готов к работе.
```bash
bot_1  | ✅ Start bot!
```
