import random
import os
from typing import List

import databases
import pymysql
import sqlalchemy
import json
from fastapi import FastAPI
from fastapi.responses import Response
from pydantic import BaseModel

pymysql.install_as_MySQLdb()

AYSNC_DATABASE_URL = f"mysql+aiomysql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}:3306/demo"
SYNC_DATABASE_URL = f"mysql+mysqldb://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}:3306/demo"

database = databases.Database(AYSNC_DATABASE_URL, max_size=10000)

metadata = sqlalchemy.MetaData()

demo_data = sqlalchemy.Table(
    "demo_data",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("create_time", sqlalchemy.DATETIME),
    sqlalchemy.Column("update_time", sqlalchemy.DATETIME),
)
engine = sqlalchemy.create_engine(SYNC_DATABASE_URL)
metadata.create_all(engine)
TEMP = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"


class DemoData(BaseModel):
    id: int
    name: str


app = FastAPI()

init = False


@app.get("/demo", response_model=List[DemoData])
async def demo_code():
    global init
    if not init:
        await database.connect()
        init = True

    query = demo_data.select().where(
        demo_data.c.name == "".join(random.choices(TEMP, k=random.randrange(1, 254)))
    )
    data = await database.fetch_all(query)
    response = json.dumps(data, default=str)
    return Response(content=response, status_code=200, media_type="application/json")