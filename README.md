
# API Cavalo Árabe

An API where a campaign can be created, where a user receives a card which can be completed by stamps. Once the card is completed, the user receives a bonus.


## Running the project

This project uses Python and Django Rest Framework

Create and activate virtual enviroment (Venv)

Installing the requirements
```bash
  pip install -r requirements.txt
```
Migrating the project models to the database
```bash
  
  python manage.py makemigrations
```
```bash
  python manage.py migrate
```
Creating Super User in order to access and manipulate the admin
```bash
  python manage.py createsuperuser
```
Running the server
```bash
    python manage.py runserver
```