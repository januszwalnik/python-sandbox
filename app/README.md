# 🐍 Python Project Setup Guide

Welcome to your Python project! Follow these steps to set up your environment and get started. 🚀

## 🌟 Set Up Your Python Environment with Poetry

Poetry helps you manage dependencies and virtual environments easily. Here's how to get started:

1. **Install Poetry** (if you haven't already):
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
    Or see [Poetry's official installation guide](https://python-poetry.org/docs/#installation).

2. **Navigate to your project directory:**
    ```bash
    cd /home/janusz/python/python_app
    ```

3. **Install dependencies and set up the virtual environment:**
    ```bash
    poetry install
    ```

4. **Activate the Poetry shell:**
    ```bash
    poetry shell
    ```
    You should now see your Poetry-managed virtual environment active.

## 🛠️ Using the Makefile

Common project tasks are automated with a `Makefile`. Here are some useful commands:

- **Install dependencies:**
    ```bash
    make poetry-add-dep
    make poetry-install-deps  
    ```
- **Run the FastAPI application:**
    ```bash
    make poetry-run
    ```

Check the `Makefile` for more available commands or type `make help.

You're now ready to develop with Poetry and Make! 🎉

To start your FastAPI application, follow these steps:

1. Open your browser and navigate to `http://127.0.0.1:8000` to access your application.

1. To explore the automatically generated API documentation, visit:
    - Swagger UI: `http://127.0.0.1:8000/docs`
    - ReDoc: `http://127.0.0.1:8000/redoc`

You're now running your FastAPI application! 🎉

1. You're all set! 🛠️

## 🐳 Build a Docker Image

To containerize your FastAPI application, you can build a Docker image. Follow these steps:

1. Ensure you have Docker installed on your system. If not, download and install it from [Docker's official website](https://www.docker.com/).

1. Navigate to your project directory:
    ```bash
    cd /home/janusz/python/python_app
    ```

1. Build the Docker image using the following command:
    ```bash
    docker build -t my-fastapi-app .
    ```

After building the Docker image, you can run your FastAPI application inside a container. Follow these steps:

1. Run the Docker container using the following command:
    ```bash
    docker run -d -p 8000:8000 --name fastapi-container my-fastapi-app
    ```

    - `-d`: Runs the container in detached mode.
    - `-p 8000:8000`: Maps port 8000 on your host to port 8000 in the container.
    - `--name fastapi-container`: Assigns a name to the container.
    - `my-fastapi-app`: The name of the Docker image you built.

1. Open your browser and navigate to `http://127.0.0.1:8000` to access your application running in the container.

1. To stop the container, use the following command:
    ```bash
    docker stop fastapi-container
    ```

1. To remove the container, use:
    ```bash
    docker rm fastapi-container
    ```

You're now running your FastAPI application in a Docker container! 🎉

## 🔄 Database Migrations with Alembic

Alembic is a lightweight database migration tool for SQLAlchemy. Follow these steps to manage your database migrations:

### ⚙️ Initialize Alembic

1. Update the `alembic.ini` file to include your database connection URL. For example:
    ```ini
    sqlalchemy.url = postgresql://user:password@localhost/dbname
    ```

1. Modify the `env.py` file in the `alembic` directory to include your SQLAlchemy models.


### ✏️ Create a Migration Script

1. Generate a new migration script:
    ```bash
    alembic revision --autogenerate -m "Add your migration message here"
    ```

2. Review the generated migration script in the `alembic/versions` directory and make any necessary adjustments.

### ⬆️ Apply the Migration

1. Apply the migration to your database:
    ```bash
    alembic upgrade head
    ```

1. This will apply all pending migrations to bring your database schema up to date.

1. Verify that the database schema has been updated correctly after the downgrade.

## 🔄 Revert a Migration

If you need to undo a database migration applied using Alembic, follow these steps:

1. Identify the revision ID of the migration you want to revert by running:
    ```bash
    alembic history
    ```
    This will display a list of migrations. Note the revision ID of the migration you want to revert.

1. Revert the migration by specifying the revision ID you want to downgrade to. For example:
    ```bash
    alembic downgrade <revision-id>
    ```
    Replace `<revision-id>` with the ID of the migration you want to revert to. Use `base` as the revision ID to revert all migrations.

## 📝 Notes

- To deactivate the virtual environment, simply run:
  ```bash
  deactivate
  ```

- If you need to update your dependencies, modify the `requirements.txt` file and re-run the install command.

Happy coding! 💻✨