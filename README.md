# fetchTV techtest

A Django application that interacts with the OMDB to return results of a simple query

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need SQLite3 installed:

```
sudo apt-get install sqlite3
```

SQLite3 browser is optional, but recommended for viewing data in the database:

```
sudo apt-get install sqlitebrowser
```

### Installing

Create a new virtual environment if desired.

Assuming python is installed on the system, install any further dependencies:

```
pip install pandas
```

In the project directory, setup of the local SQLite3 database is done with:

```
python init.py
```

One can add Accumulation block fields for ingest into the database as desired by editing the config.py file.


### Usage

To ingest a NEM13 csv file (with verbose output), use:

```
chmod u+x octopus_techtest.py
./octopus_techtest.py -v sample.csv
```
The sample.csv is provided.

Use the SQLite3 browser to view data in the database.


## Running the tests

Tests are run using pytest as follows:


### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

