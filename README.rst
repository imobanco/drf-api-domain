.. _local server: http://localhost:8000/
.. _local server admin: http://localhost:8000/admin/

**************
drf-api-domain
**************

demostração da arquitetura sugerida no
`styleguide django-api-domains <https://phalt.github.io/django-api-domains>`_


Install
=======
Docker + docker-compose
-----------------------
Install [docker-ce](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/) from each documentation

Setting up
==========
On the project folder run the following commands:

#. `$ make config.env` to copy the file `.env.example` to `.env`
#. `$ make build` to build docker containers

Running the project
===================
Simply run the command `$ make up` and *voilà*.

This command will start 3 services on your machine:

- Django server on `local server`_
- PostgreSQL service on port 5432

Tests
=====
On the project folder:
- run the command `$ make test` or `$ make test app=$(app_name)`. You may run the command `$ make coverage` instead.
- run the command `$ make flake8`

Administration
==============
Django Admin Site is enabled for the project on `local server admin`_.

The command `$ make populate.superuser` may be used to create the superuser `User(email='superuser@admin.com', password='@Admin123')`.

Using the API
=============
Access the `local server`_ and browse the api.

You may interact with the API via browser or via http request softwares such as [Insomnia](#insomnia-setup)
