# Contributing guide

## install pyenv
https://akrabat.com/creating-virtual-environments-with-pyenv/

## Install python

pyenv install 3.11

## create virutal env

pyenv virtualenv 3.11 sudoauth-venv

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

## Install pre-commit hooks

pip install pre-commit
pre-commit install
