from peewee import *
from app.models.database import db
from datetime import datetime


class BaseModel(Model):
    class Meta:
        database = db


class Category(BaseModel):
    name = CharField(max_length=32)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        table_name = "category"


db.connect()
db.close()
