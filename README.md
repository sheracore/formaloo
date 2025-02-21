# formaloo
formaloo assignment

## Postgres
Change values in brackets to what you set in .env file for db name, user and password.
Also create database for running tests
```commandline
sudo -u postgres psql
postgres=# CREATE DATABASE [your db name];
postgres=# CREATE USER [your db user] WITH PASSWORD [your db password];
postgres=# ALTER USER [your db user] CREATEDB;
postgres=# GRANT ALL PRIVILEGES ON DATABASE [your db name] TO [your db user];
postgres=# \q
```