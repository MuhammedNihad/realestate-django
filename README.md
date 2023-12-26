# Realestate

## Installation

- Make sure to install [pip](https://pip.pypa.io/en/stable/), [Python](https://www.python.org/downloads/), [virtualenv](https://pypi.org/project/virtualenv/) and [PostgreSQL](https://www.postgresql.org/download/)

Create a database using PostgreSQL GUI App.

If you prefer command line, install and use psql CLI tool as below:
```bash
sudo -u postgres psql
```
Create database using psql CLI 
```bash
CREATE DATABASE databasename;
CREATE USER username WITH ENCRYPTED PASSWORD 'password';
ALTER ROLE username SET client_encoding TO 'utf8';
ALTER ROLE username SET default_transaction_isolation TO 'read committed';
ALTER ROLE username SET timezone TO 'Asia/Kolkata';
GRANT ALL PRIVILEGES ON DATABASE databasename TO username;
```
## Environment Variables

Create .env file by copying example file in the root folder
```bash
cp .env.example .env
```
And feed your previously created database credentials in .env file


## Usage

Activate virtual environment using 

```bash
virtualenv venv
source venv/bin/activate
```

Install dependencies/packages using
```bash
pip install -r requirements.txt
```

Make migrations using
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
Create super user using 
```bash
python3 manage.py createsuperuser
```
Run server using
```bash
python3 manage.py runserver
```
