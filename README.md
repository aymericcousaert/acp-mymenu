# my-menu-acp1

Trabajo Práctico Grupal "My Menu" - ACP 1 - FIUBA

#### Requirements:
    - Python 3.x
    - pip (https://pip.pypa.io/en/stable/installing/)
    - virtualenv (https://virtualenv.pypa.io/en/stable/)

## Set up environment

### Create and activate virtualenv

```
virtualenv -p python3 env
source env/bin/activate
```
Make sure that you are using python 3 inside the virtualenv by typing:
```
python --version
```

### Install requirements

```
pip install -r requirements.txt
```

## Set up the database

- Create a postgresql database with the DATABASES config in settings.py

### Run migrations
```
python manage.py migrate
```
## Start the server

```
python manage.py runserver
```

## Access to admin site
### Create SuperUser
```
python manage.py createsuperuser
```
Follow the instructions

Enter to: http://127.0.0.1:8000/admin and login
