![alt text](https://raw.githubusercontent.com/MichaelPak/secretsanta/master/app/static/santa.png)

Secret Santa
===
[![dockerhub](https://img.shields.io/badge/docker-hub-green.svg)](https://hub.docker.com/r/michaelpak/secretsanta/)

## Setup

```bash
# Create keypair
$ ssh-keygen -f ~/.ssh/id_infra

# Init  terraform
$ terraform init iaac/

# Install ansible rolers
$ ansible-galaxy install geerlingguy.docker
$ ansible-galaxy install antoiner77.caddy

# Create user list
$ cp resources/users-example.yml resources/users.yml
```

## Commands
```bash
# Initialize database
$ pipenv run loaddb

# Run flask server
$ pipenv run server

# Create infra by terraform
$ pipenv run tfapply

# Setup infra by ansible
$ pipenv run ansplay --ip 127.0.0.1

# Destroy infra by terraform
$ pipenv run tfdestroy
```

## Run

```bash
# Need docker & docker-compose
$ docker-compose run
```

## Dependencies
- [`docker ansible role`](https://galaxy.ansible.com/geerlingguy/docker)
- [`caddy ansible role`](https://galaxy.ansible.com/antoiner77/caddy)
