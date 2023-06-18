## RUSSPASS HACKATHON

The backend part of the application is made using technologies such as: FastApi, PostgreSQL, Sklearn, Pandas. The latter were used to implement a collaborative recommendation system for users.


### Set Up the app

>Download the code
```
$ git clone https://github.com/Svogg/xakaton
Create .dbenv and .env_dev files in root folder
$ cd xakaton
```

>.env_dev contains
```
SECRET_KEY=some secret key
```

>.dbenv contains
```
POSTGRES_DRIVER=postgresql
POSTGRES_CONNECTOR=asyncpg
POSTGRES_USER=user
POSTGRES_PASS=pass
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_NAME=db_name
```

>Install modules VENV
```
$ virtualenv env
$ .\env\Scripts\activate
$ pip install -r requirements.txt
```

>Start the app
```
Create database 'db_name' in PostgreSQL
$ alembic init migrations
$ alembic revision --autogenerate -m "initial"
$ alembic upgrade head
$ uvicorn main:app --reload
```

At this point, the app runs at http://127.0.0.1:8000/

### OpenAPI documentation

```
This application implements swagger for documenting endpoints.
The documentation can be accessed via the url http://.../docs
```
