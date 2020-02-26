# fetchTV techtest

A Django application that interacts with the OMDB API to return results of a simple query

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing

Create a new virtual environment if desired (recommended), and activate it:

```
source $VENV/bin/activate
```

Change to project directory, clone repository and install any further dependencies with pip:

```
git clone https://github.com/freelancemeteo/fetchtv_techtest.git
pip install -r requirements.txt
```

Perform needed DB migrations:
```
python manage.py make migrations
python manage.py migrate
```

Create a super user to acccess admin:
```
python manage.py createsuperuser
```

### Usage

To run locally, launch a Django server:

```
python manage.py runserver
```

And navigate to the suggested localhost address.

To update the cached OMBD requests, simply run the management command:

```
python manage.py updateResults
```

To edit cached results, navigate to admin section (suffix admin/), login with superuser credentials and edit the Results using the provided interface.

## Running tests

A small suite of Django tests can be run with:

```
python manage.py test
```
