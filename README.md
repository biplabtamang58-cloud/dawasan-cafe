# Dawasan Cafe

A responsive single-page website for a cafe, built with Django. Black and gold luxury theme.

## Features
- Smooth-scrolling one-page layout with animated sections
- Menu managed from the Django admin (categories, items, photos, featured and vegetarian flags)
- Table reservation form that saves bookings to the database
- Contact form with an admin inbox
- Photo gallery and editable cafe info (address, hours, about text)
- Mobile-first responsive design with a hamburger menu

## Tech stack
Python, Django, SQLite, HTML, CSS, JavaScript

## Run locally
```bash
git clone https://github.com/biplabtamang58-cloud/dawasan-cafe.git
cd dawasan-cafe
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
