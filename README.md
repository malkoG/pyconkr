# PyCon Korea Homepage

[![Build Status](https://travis-ci.org/pythonkr/pyconkr-2018.svg?branch=master)](https://travis-ci.org/pythonkr/pyconkr-2018)

## Requiremensts

- Python 3.7.3

## Getting started

```bash
$ git clone git@github.com:pythonkr/pyconkr.git
$ cd pyconkr
$ pip install -r requirements.txt
$ python manage.py compilemessages
$ python manage.py makemigrations  # flatpages
$ python manage.py migrate
$ python manage.py loaddata ./pyconkr/fixtures/flatpages.json
$ bower install
$ python manage.py runserver
```

