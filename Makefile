################################################################################
# Docker-compose django service commands for dev
################################################################################
current_dir = $(notdir $(shell pwd))

migrate:
	docker-compose run django python manage.py migrate $(app)

makemigrations:
	docker-compose run django python manage.py makemigrations $(app)

test:
	docker-compose run django python manage.py test $(app)

bash:
	docker-compose run django bash

shell:
	docker-compose run django python manage.py shell

coverage:
	docker-compose run django coverage run --source='.' manage.py test $(app)
	docker-compose run django coverage report

up:
	docker-compose up -d

logs:
	docker-compose logs -f $(service)

down:
	docker-compose down

django.stop:
	docker stop django

django.restart: django.stop up

build:
	docker-compose build

remove.volumes:
	docker-compose down
	docker volume rm $(current_dir)_pg_volume $(current_dir)_media_volume $(current_dir)_log_volume $(current_dir)_static_volume

clear.docker:
	docker ps | awk '{print $$1}' | grep -v CONTAINER | xargs docker stop

################################################################################
# Populate commands
################################################################################
populate.superuser:
	docker-compose run django python manage.py populate_superuser

populate.clients:
	docker-compose run django python manage.py populate_clients

populate.companies:
	docker-compose run django python manage.py populate_companies

populate.address:
	docker-compose run django python manage.py populate_address

populate.all: populate.superuser populate.clients populate.companies populate.address

################################################################################
# Bare host commands
################################################################################
pip.install:
	pip install -r requirements-dev.txt

test.local:
	python manage.py test

black:
	black --check .

black.reformat:
	black .

clear.python:
	find . -type d -name __pycache__ -o \( -type f -name '*.py[co]' \) -print0 | xargs -0 rm -rf

config.env:
	cp .env.example .env
