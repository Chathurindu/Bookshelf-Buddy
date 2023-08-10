# Bookshelf Buddy

Bookshelf Buddy is a web application designed to help book enthusiasts manage and organize their personal book collections. It provides features for adding, editing, and searching for books, as well as tracking various details such as title, author, publication date, and ISBN.

## Table of Contents

- [Getting Started](#getting-started)
  - [Virtual Environment](#virtual-environment)
  - [Installation](#installation)
  - [Create Superuser](#create-superuser)
  - [Database Migrations](#database-migrations)
  - [Run Development Server](#run-development-server)

## Getting Started

These instructions will guide you through setting up and running the project locally.

### Virtual Environment

It's recommended to use a virtual environment to manage dependencies for your project. To create and activate a virtual environment, use the following commands:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS and Linux
source venv/bin/activate

```

### Installation

```bash

# Install project dependencies from the requirements.txt file:
pip install -r requirements.txt

```

### Create Superuser

```bash

# To access the Django admin interface, create a superuser account using the following command:
python manage.py createsuperuser

```
### Database Migrations

```bash

# Apply database migrations to set up the database schema:
python manage.py makemigrations
python manage.py migrate

```
### Run Development Server

```bash

# Start the development server to run the project:
python manage.py runserver

```