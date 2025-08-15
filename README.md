## Student DBMS (Django)

A simple Student Database Management System built with Django. It supports secure login, student CRUD, and attendance tracking with per-day uniqueness and percentage calculations.

### Features
- **Authentication**: Login required for all views
- **Student management**: Add, view, update, and delete students
- **Attendance**: Record daily attendance (one record per student per day) and see attendance percentages
- **Admin panel**: Manage data via Django Admin

### Tech stack
- **Backend**: Django 5
- **Language**: Python 3.12
- **Database**: MySQL (via `mysqlclient`)
- **Frontend**: Django templates, HTML/CSS

### Project structure (key paths)
```
Mini Project DBS/
  project/
    studentdbms/
      manage.py
      studentdbms/           # Project settings & URLs
      database/              # App (models, views, urls, templates, static)
        models.py
        views.py
        urls.py
        templates/
          base.html
          login.html
          index.html
          database.html
          view.html
          attendance.html
        static/
          css/style.css
```

### Prerequisites
- Python 3.12
- MySQL Server (e.g., 8.x)
- Pipenv or pip
- Build tools for `mysqlclient` if needed (on Windows, Visual C++ Build Tools)

### Database setup (MySQL)
1. Create a database and user (example):
```sql
CREATE DATABASE student CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'student_user'@'localhost' IDENTIFIED BY 'strong_password_here';
GRANT ALL PRIVILEGES ON student.* TO 'student_user'@'localhost';
FLUSH PRIVILEGES;
```
2. Update Django DB credentials in `project/studentdbms/studentdbms/settings.py` under `DATABASES['default']`:
   - `NAME`: `student`
   - `USER`: your MySQL username
   - `PASSWORD`: your MySQL password
   - `HOST`: `localhost`
   - `PORT`: `3306`

Note: The repo currently points to MySQL with placeholders. For production, never hardcode credentials or the Django `SECRET_KEY`. Prefer environment variables or a `.env` file with a loader.

### Installation

You can use Pipenv (preferred) or plain pip. Run commands from `project/studentdbms/` where `manage.py` lives.

- Using Pipenv:
```bash
# from repo root
cd "project/studentdbms"
pipenv install --dev
# Ensure mysqlclient is installed
pipenv run pip install mysqlclient
```

- Using virtualenv + pip:
```bash
# from repo root
cd "project/studentdbms"
python -m venv .venv
# Windows PowerShell
. .venv\Scripts\Activate.ps1
# macOS/Linux
# source .venv/bin/activate
pip install django mysqlclient
```

If `mysqlclient` fails to install on Windows, install the Visual C++ Build Tools and retry, or use a prebuilt wheel appropriate for your Python version.

### Environment variables (.env)
This project reads settings from environment variables. A sample file is provided:
- Copy `project/studentdbms/.env.example` to `project/studentdbms/.env` and fill values.

On Windows PowerShell:
```powershell
Copy-Item project\studentdbms\.env.example project\studentdbms\.env
```

The app will automatically load `project/studentdbms/.env` during development.

### Apply migrations and create a superuser
```bash
cd "project/studentdbms"
# If using pipenv, prefix commands with: pipenv run
python manage.py migrate
python manage.py createsuperuser
```

### Run the development server
```bash
cd "project/studentdbms"
python manage.py runserver
```
- App: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

### App URLs and usage
- `/` → Login page
- `/home/` → Dashboard
- `/database/` → Add a new student (name, email, DOB, course, CGPA, department)
- `/view/` → List and manage students (update/delete)
- `/attendance/` → Mark daily attendance and view attendance percentage per student
- `/logout/` → Logout

Attendance records are unique per student per date. The app computes attendance percentage as \(present\_days / total\_days \times 100\) and shows it on the attendance page.

### Environment and security
- Set `DEBUG=False` and configure `ALLOWED_HOSTS` for production in `settings.py`.
- Do not commit secrets (e.g., `SECRET_KEY`, DB password). Use environment variables or a secret manager.

### Static files
During development, static files are served from `database/static/`. For production, configure `STATIC_ROOT` and run:
```bash
python manage.py collectstatic
```

### Troubleshooting
- **mysqlclient install issues**: Ensure MySQL headers and a compatible compiler are available. On Windows, install the “Desktop development with C++” workload (Visual Studio Build Tools).
- **Cannot connect to MySQL**: Verify DB name, user, password, host, and that MySQL is running. Test with: `mysql -u <user> -p -h 127.0.0.1 -P 3306`.
- **Migrations**: If schema changed, run `python manage.py makemigrations` then `python manage.py migrate`.


### Acknowledgements
Built with Django. Thanks to the Django community for documentation and tooling.
