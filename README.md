## Backery Backend Project

#### Order backery items with admin panel

Frontend for this project is published on https://github.com/cptc0ld/BackeryAppFrontend

## Install

    - Create Virtual environment
        python3 -m venv env
        env\Scripts\activate (for cmd)
    - Install all packages in Virtual environment
        pip install -r requirements.txt

## Install by Docker

    - docker-compose build   
    - docker-compose up

## Run the app
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

```
Point to note:
Set your db credentials in settings.py
```

# Solution Approach

Posted with postman collection  https://documenter.getpostman.com/view/8283532/UV5WDxyP


# Errors encountered while running in docker

- initdb: error: directory "/var/lib/postgresql/data" exists but is not empty

        delete the `postgres-data` folder from your project dir
