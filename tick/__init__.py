import os

from pathlib import Path

import pytz

from dotenv import load_dotenv
from sqlalchemy import create_engine

from .models import Base


SECRETS = Path(".secrets/")
TZ = pytz.timezone("EST")

load_dotenv(SECRETS / ".env")

EMAIL = os.environ.get("EMAIL", "")
NAME = os.environ.get("NAME", "")

ENGINE = create_engine(f"sqlite:///{SECRETS / 'db.sqlite'}")

Base.metadata.create_all(ENGINE)
