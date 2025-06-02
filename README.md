# Restaurant Menu API

A simple RESTful API for managing restaurant menu items and categories using Django and Django REST Framework.

## Features
- CRUD operations for menu items and categories
- Category relationships
- RESTful endpoints using DRF
- Browsable API interface

## Endpoints
- `/api/categories/`
- `/api/menu-items/`

## Setup

```bash
git clone https://github.com/yourusername/restaurant-menu-api.git
cd restaurant-menu-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
