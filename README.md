Captain's log
==============

A simple task logger for personal use, built with Django.

to install:

    $ pip install -r requirements.txt

   You'll need to define the environment variables [DATABASE_URL](https://github.com/jacobian/dj-database-url) and [SECRET_KEY](https://docs.djangoproject.com/en/3.0/ref/settings/#secret-key). For local development, you may save these to a `.env` file and they will be pulled in by the settings.py.

   Generate the DB tables:

   $ python manage.py migrate

To deploy locally:

    $ python manage.py runserver

You'll need to create a user to be able to login, e.g:

    $ python manage.py createsuperuser

![picard at computer](https://i.pinimg.com/originals/71/8c/f9/718cf96029995dcc441cbbbec5c35f7a.jpg)
