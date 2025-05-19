# Set env vars
ALEMBIC=alembic


# Docker config
IMAGE_NAME=fastapi_app
CONTAINER_NAME=fastapi_app_container
DOCKERFILE=app/Dockerfile

# Poetry dependencies
APP_REQS := $(shell cat app/requirements.txt)


# Default target
.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make pg-downgrade                         - Downgrade one Alembic migration step"
	@echo "  make pg-upgrade                           - Upgrade to head (latest) migration"
	@echo "  make pg-revision msg=\"message\"            - Create new Alembic revision"
	@echo "  make docker-build                         - Build Docker image"
	@echo "  make docker-run                           - Run Docker container"
	@echo "  make docker-compose-run                   - Run Docker Compose for pg contiainer"
	@echo "  make docker-compose-stop                  - Stop Docker Compose for pg container"
	@echo "  make poetry-run                           - Run FastAPI app with Uvicorn using Poetry"
	@echo "  make poetry-install-deps                  - Install dependencies with Poetry"
	@echo "  make poetry-add-dep                       - Add dependencies from requirements.txt with Poetry"
	@echo "  make poetry-add-dev-dep pkg=package_name  - Add a development dependency with Poetry"

# Downgrade by one revision
.PHONY: pg-downgrade
pg-downgrade:
	$(ALEMBIC) downgrade -1

# Upgrade to latest (head)
.PHONY: pg-upgrade
pg-upgrade:
	poetry run $(ALEMBIC) upgrade head

# Create a new migration revision with a message
.PHONY: pg-revision
pg-revision:
ifndef msg
	$(error "Missing msg param: usage: make revision msg=\"add users table\"")
endif
	poetry run $(ALEMBIC) revision --autogenerate -m "$(msg)"

# Docker commands
.PHONY: docker-build
docker-build:
	docker build -t $(IMAGE_NAME) -f $(DOCKERFILE) ./app

.PHONY: docker-run
docker-run:
	docker run -d --rm --name $(CONTAINER_NAME) -p 8000:8000 $(IMAGE_NAME)

.PHONY: docker-compose=run
docker-compose-run:
	docker compose -f app/dev-docker-compose.yml up -d

.PHONY: docker-compose-stop		
docker-compose-stop:
	docker compose -f app/dev-docker-compose.yml down

.PHONY: poetry-run
poetry-run:
	poetry run uvicorn app.main:app --reload

.PHONY: poetry-install-deps
poetry-install-deps:
	poetry install

.PHONY: poetry-add-dep
poetry-add-dep:
	poetry add $(APP_REQS)

.PHONY: poetry-add-dev-dep
poetry-add-dev-dep:
ifndef pkg
	$(error "Missing pkg param: usage: make add-dev-dep pkg=package_name")
endif
	poetry add --dev $(pkg)