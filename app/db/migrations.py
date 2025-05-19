from alembic import command
from alembic.config import Config
import os

def run_migrations():
    config = Config("alembic.ini")
    command.upgrade(config, "head")