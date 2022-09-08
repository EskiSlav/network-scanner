# Simple Web App

## How To Use
```
git clone https://git.ext.opinov8-intra.net/viak/simple-web-app
cd simple-web-app
python3 -m venv env
. ./env/bin/activate
pip install -r requirements.txt
docker-compose -f yaml/postgres.yml -p postgres up
python3 simplewebapp/manage.py runserver 8081
```
Now you can access the server at `http://localhost:8081/login`

