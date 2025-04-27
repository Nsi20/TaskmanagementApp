# TaskMaster - Task Management Application

A full-stack task management application built with Django and MySQL.

## Features
- User authentication and authorization
- Task creation, editing, and deletion
- Priority levels and status tracking
- RESTful API endpoints
- Responsive Bootstrap UI

## Tech Stack
- Django 5.2
- Django REST Framework
- MySQL
- Bootstrap 5
- HTML/CSS/JavaScript

## Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/Nsi20/TaskmanagementApp.git
cd TaskmanagementApp
```

2. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
Create a `.env` file with the following:
```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=taskmaster
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_HOST=127.0.0.1
DB_PORT=3306
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start development server:
```bash
python manage.py runserver
```

## Deployment
The application is configured for deployment on Render.com with MySQL database support.

## API Documentation
Access the API at `/api/tasks/` for task management operations.

## License
MIT License