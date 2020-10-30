# Flask-RESTful API 

Main libraries used:
1. Flask-Migrate - for handling all database migrations.
2. Flask-RESTful - restful API library.
3. Flask-Script - provides support for writing external scripts.
4. Flask-SQLAlchemy - adds support for SQLAlchemy ORM.

* endpoints - holds all endpoints.
* app.py - flask application initialization.
* settings.py - all global app settings.
* manage.py - script for managing application (migrations, server execution, etc.)

## Running 

1. Clone repository.
2. pip3 install -r requirements.txt
3. Run following commands:
    0. rm -rf ./migrations
    1. python3 manage.py db init
    2. python3 manage.py db migrate
    3. python3 manage.py db upgrade
4. Start server by running: python3 manage.py runserver

## Usage
### Endpoints
Methods in request.rest