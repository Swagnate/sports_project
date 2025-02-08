# Sports Registration App

Добро пожаловать в приложение!

## Установка

Следуйте этим шагам, чтобы установить и запустить приложение на своем локальном компьютере.

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/Swagnate/sports_project.git
```

### 2. Перейдите в папку проекта:
```
cd sports_registration
```

### 3. Создайте виртуальное окружение:
```
python -m venv venv
```

### 4. Активируйте виртуальное окружение:

### для Windows
```
venv\Scripts\activate
```

### для macOS/Linux:
```
source venv/bin/activate
```

### 5. Установите зависимости:
```
pip install -r requirements.txt
```

### 6. Примените миграции базы данных:
```
python manage.py migrate
```

### 7. Создайте суперпользователя для доступа к административной панели:
```
python manage.py createsuperuser
```

### 8. Запустите сервер:
```
python manage.py runserver
```
Теперь вы можете открыть браузер и перейти по адресу
```
http://127.0.0.1:8000
```
для доступа к приложению.
