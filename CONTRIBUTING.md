# Contributing guide

## install pyenv
https://akrabat.com/creating-virtual-environments-with-pyenv/

## Install python

pyenv install 3.11

## create python virutal env

pyenv virtualenv 3.11 sudoauth-venv
pyenv virtualenv 3.11 sudoauth-app-venv

## Activate venv

pyenv activate sudoauth-venv

## Install dev requirements

### System pre-requisites (python-ldap)
apt install build-essential python3-dev \
    libldap2-dev libsasl2-dev slapd ldap-utils tox \
    lcov valgrind

### Upgrade pip and install dev requirements
pip install --upgrade pip
pip install -r requirements-dev.txt \
    -r src/backend/requirements.txt

## Upgrade packages

### in dev virtual env

pur -r requirements-dev.txt
pip install -r requirements-dev.txt

### in app virutal env

pur -r requirements.txt
pip install -r requirements.txt


## Install pre-commit hooks

pip install pre-commit
pre-commit install
pre-commit autoupdate

### Run pre commit hooks

pre-commit run --all-files
pre-commit run bandit --all-files

## Run app

### Django backend

cd /home/mmoglia/Develop/sudoauth/src/backend
python manage.py runserver


## Install Angular

### Install nodejs

sudo apt-get update && sudo apt-get install -y ca-certificates curl gnupg
curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
NODE_MAJOR=18
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list
sudo apt-get update && sudo apt-get install nodejs -y

### Install angular/cli

sudo npm install -g @angular/cli
sudo npm install -g npm@10.2.1
cd src/frontend
npm install

### Run frontend app

ng serve


### Upgrade Angular

ng update @angular/cli @angular/core
