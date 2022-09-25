## test-django
Sur base du fichier CSV fourni (test.csv), ceci est une solution permettant le chargement des données dans une base de données SQLite avec Django.

## Installation

First you need to clone the repository.

`git clone https://github.com/billkurios/test-django.git`

Create virtualenv folder in the root of project. The last name _venv_ is your venv folder name.

`python3 -m venv venv`

Activate your venv environment

`source venv/bin/activate`

Install required packages

`pip install -r requirements.txt`

Install the git hook scripts

`pre-commit install`


## License

MIT