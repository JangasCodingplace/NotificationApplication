# Notification Application
A repo for a tutorial to understand different webprotocolls and methods for update needed & realtime applications.

## Functionality Description
The Application is able to create some ToDo Tasks. A tasks has the properties `assigned_to, created_by, title, creaton_date, is_done` if the `assigned_to` user is different from the `created_by` user, a notification gets created for the `assigned_to` user, if this task gets marked to `is_done=True` the `created_by` user receive a notification. **The use case of this application should not be by a creation of some tasks. It's a playground of transporting the notification in realtime to the users.**

## Requirements
- This project is programmed with **Python 3.7.6** on a Mac OS. `f-Strings` are in used - *Python >= 3.6 is recommended*.
- **Django >= 2.X**, **Channels == 2.X** are recommended
- **Redis** is in used. Please take a look for your system to get a quick installation & start Guide

### Quick Start (Hopefully)
- Clone this Repo
- Create a virtualenv (its recommended) _Mac OS_`python3 -m venv venv`  // _Win_ `python -m venv venv`
- Start venv _Mac OS / Ubuntu_ `source venv/bin/activate` // _Win_ `venv\Scripts\activate.bat`
- Install all requirements `pip install -r requirements.txt`
- migrate the database `python manage.py migrate`
- create a superuser `python manage.py createsuperuser`
- start your local Redis server (How to start depends on your preferences and System)
- run your application `python manage.py runserver`
- go to admin & login `http://127.0.0.1:8000/admin`
- create a testuser
- create some todos or notifications
- open the landingpage `http://127.0.0.1:8000/`
