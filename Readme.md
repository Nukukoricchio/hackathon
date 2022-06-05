# Hackathon Project


## Django Setting

Clone Repo

```bash
$ https://github.com/Nukukoricchio/hackathon.git
```

Install Packages:

```bash
$ cd qlda
$ cd backend
$ virtualenv -p python3 env
$ source env/bin/activate
$ pip install -r requirements.txt
```

Create database:

```bash
$ python manage.py makemigrations 
$ python manage.py migrate
```

Run development server

```bash
$ python manage.py runserver
```

Open Chrome or FireFox : **127.0.0.1:8000**


## Nuxt.js Setting

Install Packages:

```bash
$ cd frontend
$ yarn install
```

Run development server

```bash
$ yarn dev
```

Open Chrome or FireFox : **localhost:3000**
