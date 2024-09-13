Тестовое задание QA:
Для запуска тестов нужно собрать образ docker с помощью команды:
```bash
docker-compose build
```
и запусть контейнеры с помощью команды:
```bash
docker-compose up
```
1. E2E UI:
    stages:
        -auth
        -add to cart
        -make purchase
2. GitHub API:
    stages:
        -create repo
        -check repo exists
        -delete repo