# GoalForge

The server for an app to help achieve your goals.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Run Docker Containers](#run-docker-containers)
- [Usage](#usage)
  - [Run Migrations](#run-migrations)
  - [Run Development Server](#run-development-server)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Make sure you have the following installed on your machine:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Getting Started

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/WhiskyToad/goalforge-django

   ```

2. Navigate to the project-directory

   ```bash
   cd goalforge-django
   ```

### Run Docker Containers

1. Build and run the containers

   ```bash
   docker compose up --build
   ```

## Usage

### Run Migrations

1. Apply database migrations to set up the initial database schema:

   ```bash
   docker compose exec web python src/manage.py makemigrations
   docker compose exec web python src/manage.py migrate
   ```

### Run Development Server

1. Start the Django development server:

   ```bash
   docker compose exec web python src/manage.py runserver 0.0.0.0:8000
   ```

   The development server will be accessible at <http://localhost:8000/>

### Troubleshooting

1.  Unresolved Imports:
    If you face unresolved import errors in your IDE, ensure that your Docker containers are running, and the volume is correctly mounted.

2.  Database Relation Does Not Exist:
    If you encounter "relation does not exist" errors, run migrations:

        ```bash
        docker compose exec web python src/manage.py makemigrations
        docker compose exec web python src/manage.py migrate
        ```

3.  Other Issues: Check the Troubleshooting section in this README for common issues and solutions.
