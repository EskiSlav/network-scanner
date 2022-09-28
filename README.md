# Simple Web App



## How To Use
Before starting it up make sure that all the credentials are provided in `docker-compose.yaml` file.

You can run application as is but it is reccomended to change poswords, database names and etc. for using in production env.

`API_TOKEN` is used by `bot-sender` and `bot`

`DJANGO_DB_NAME` -- is used for database name.

`DJANGO_DB_USER` -- is used for user oh whose behalf will be services interacting with DB.

`DJANGO_DB_PASSWORD` -- is used for password got `DJANGO_DB_USER`.

`DJANGO_DB_PORT` -- is used for specification which port will be used for accessing DB. Do not change this value 
because it won't work on this version.
`DJANGO_ADMIN_USER` -- is username for creating Django user for site you will get access on `http://localhost:8081/`

`DJANGO_ADMIN_MAIL` -- is email for Django user

`DJANGO_ADMIN_PASSWORD` -- is password for Django user

`POSTGRES_USER` -- is used for database service account

`POSTGRES_PASSWORD` -- is used for database service account


After setting all needed variables you can finally lauch the program.

```
docker-compose build
docker-compose up -d
```

After a few seconds you can access the server at `http://localhost:8081/login`.


## Services Description
`bot-sender` -- service that sends messages on behalf of the bot. Needs API_TOKEN for bot which you can get from 
BotFather in Telegram.
`web` -- Django service which provides web site for interaction with users who have written to the bot.

`bot` -- service responsible for getting messages from the bot and writting them to the database. Uses AIOgram lib for 
python.
`db` -- PostgreSQL database which is used to store data about users who write to bot and for Django database also.

`python-seeder` -- service that can be uncommented to fill the database with mockup messages and users. If this service in use then you won't be able to message fake users.
