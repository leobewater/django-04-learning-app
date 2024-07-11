Book: Django 5 by Example (5th Edition)

# To Run
```
> py -m venv env/educa
> source env/educa/bin/activate
> py -m pip install -r requirements.txt
> django-admin startproject educa

> py manage.py runserver


# Dump Courses data in JSON format
> cd educa
> py manage.py dumpdata courses --indent=2

> mkdir courses/fixtures
> py manage.py dumpdata courses --indent=2 --output=courses/fixtures/subjects.json

# Load data. Django looks for files in the fixtures/ directory of each application
> py manage.py loaddata subjects.json
```