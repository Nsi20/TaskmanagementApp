# TaskMaster - Task Management Application

A full-featured task management application built with Django and Django REST Framework.

## Features

- User authentication and authorization
- Create, read, update, and delete tasks
- Task prioritization and status tracking
- RESTful API endpoints
- Responsive Bootstrap UI
- MySQL database integration

## Technologies Used

- Python 3.x
- Django 5.2
- Django REST Framework
- MySQL
- Bootstrap 5
- HTML/CSS
- JavaScript

## Live Demo

[View Live Demo](your-deployed-url-here)

## Screenshots

![TaskMaster Dashboard](screenshots/dashboard.png)
![Task Creation](screenshots/create-task.png)

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/taskmaster.git
cd taskmaster
```

2. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a .env file with:
```
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=taskmaster
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=3306
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

## API Documentation

### Endpoints

- `GET /api/tasks/` - List all tasks
- `POST /api/tasks/` - Create a new task
- `GET /api/tasks/{id}/` - Retrieve a task
- `PUT /api/tasks/{id}/` - Update a task
- `DELETE /api/tasks/{id}/` - Delete a task
- `POST /api/tasks/{id}/complete/` - Mark task as complete

## Deployment

This application is deployed on [Platform Name] using [Technology Stack].

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)