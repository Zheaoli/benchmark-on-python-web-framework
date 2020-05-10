import random
from typing import List

import databases
import pymysql
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel

pymysql.install_as_MySQLdb()

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

demo_data = sqlalchemy.Table(
    "demo_data",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("create_time", sqlalchemy.DATETIME),
    sqlalchemy.Column("update_time", sqlalchemy.DATETIME),
)
engine = sqlalchemy.create_engine(DATABASE_URL)
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
    return await database.fetch_all(query)
