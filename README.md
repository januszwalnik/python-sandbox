# Python App

This project uses [Poetry](https://python-poetry.org/) for dependency management and [Uvicorn](https://www.uvicorn.org/) as the ASGI server.

## Prerequisites

- Python 3.7+
- [Poetry](https://python-poetry.org/docs/#installation)

## Installation

```bash
poetry install
```

## Adding Dependencies

To add all dependencies listed in `app/requirements.txt`:

```bash
poetry add $(cat app/requirements.txt)
```

## Running the Project

Start the Uvicorn server:

```bash
poetry run uvicorn your_module:app --reload
```

Replace `your_module:app` with the actual Python module and ASGI app instance.

## Useful Commands

- Add a dependency:  
    ```bash
    poetry add <package>
    ```
- Run tests:  
    ```bash
    poetry run pytest
    ```

## More Information

See the [Poetry documentation](https://python-poetry.org/docs/) for more details.