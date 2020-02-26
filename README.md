# fetchTV techtest

A Django application that interacts with the OMDB API to return results of a simple query

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing

Create a new virtual environment if desired (recommended), and activate it:

```
source $VENV/bin/activate
```

Change to project directory, pull repository and install any further dependencies with pip:

```
git pull https://github.com/freelancemeteo/fetchtv_techtest.git
pip install -r requirements.txt
```

There is no need to initialise any Django databases.

### Usage

To run locally, launch a Django server:

```
python manage.py runserver
```

And navigate to the suggested localhost address.


## Running tests

A small suite of Django tests can be run with:

```
python manage.py test
```
