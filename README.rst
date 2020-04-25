.. _local server: http://localhost:8000/
.. _local server admin: http://localhost:8000/admin/
.. _docker: https://docs.docker.com/install/
.. _docker-compose: https://docs.docker.com/compose/install/
.. _insomnia: https://insomnia.rest

**************
drf-api-domain
**************

demostração da arquitetura sugerida no
`styleguide django-api-domains <https://phalt.github.io/django-api-domains>`_


Install
=======
Docker + docker-compose
-----------------------
Install `docker`_ and `docker-compose`_ from each documentation

Setting up
==========
On the project folder run the following commands:

.. code-block::

   make config.env
   make build

to copy the file `.env.example` to `.env` and build docker containers

Running the project
===================
Run the command

.. code-block::

    make up


This command will start 2 services on your machine:

- Django server on `local server`_
- PostgreSQL service on port 5432

Tests
=====
On the project folder

.. code-block::

    make test

    make coverage

    make black


Administration
==============
Django Admin Site is enabled for the project on `local server admin`_.

.. code-block::

    make populate.superuser

may be used to create the superuser

.. code-block::

    User(email='superuser@admin.com', password='@Admin123')

Using the API
=============
Access the `local server`_ and browse the api.

You may interact with the API via browser or via http request softwares such as `insomnia`_
