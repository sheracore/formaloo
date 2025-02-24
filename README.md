# Formaloo

# Running the project using docker
### If you have run the Postgres service in your local server please stop the service or change the port in docker-compose
* **by running the below command-line**:
  * **Dockerfile(django-project) will be build**
    * **requirements will be installed**
    * **8000 port will be exposed**
  * **Postgres image will be downloaded**
  * **migrate and collectstatic commands will be run**
  * **project will be run and listened on 8000**
* **Also the containers will be connected together and each one will have persistent storage(volume)**
```angular2html
docker-compose up --build
```
## Create superuser for admin panel
```angular2html
docker-compose run django-web python manage.py createsuperuser
```

## Project api documentations are on the http://127.0.0.1:8000/api/redoc/ and http://127.0.0.1:8000/api/docs/

## Running tests
```angular2html
docker-compose run django-web python manage.py test
```

# Runnign the project without docker
## First of all, change database host to 'localhost' in settings.py

## Postgres
Change values in brackets to what you set in .env file for db name, user and password.
```commandline
sudo -u postgres psql
postgres=# CREATE DATABASE [your db name];
postgres=# CREATE USER [your db user] WITH PASSWORD [your db password];
postgres=# ALTER USER [your db user] CREATEDB;
postgres=# GRANT ALL PRIVILEGES ON DATABASE [your db name] TO [your db user];
postgres=# \q
```

## Migrations
```angular2html
python manage.py migrate
```

## Superuser for admin panel
```angular2html
python manage.py createsuperuser
```

## run server
### On local
```angular2html
python manage.py runserver 0.0.0.0:8000
```

## Project api documentations are on the http://127.0.0.1:8000/api/redoc/ and http://127.0.0.1:8000/api/docs/

## Running tests
```angular2html
- python manage.py test
- or using pycharm ide
```

### On production
* Create gunicorn service
* Connect Nginx to the gunicorn


