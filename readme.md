# Sports Registration App

## Установка

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/Swagnate/sports_project.git
```

### 2. Перейдите в папку проекта:

`cd sports_registration`

### 3. Создайте виртуальное окружение:

`python -m venv venv`

### 4. Активируйте виртуальное окружение:

# на Windows

`venv\Scripts\activate`

# Для macOS/Linux:
`source venv/bin/activate`
### 5. Установите зависимости:

`pip install -r requirements.txt`

### 6. Примените миграции базы данных:
`python manage.py migrate`
### 7. Создайте суперпользователя для доступа к административной панели:

`python manage.py createsuperuser`
### 8. Запустите сервер:

`python manage.py runserver`