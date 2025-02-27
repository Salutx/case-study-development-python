from peewee import *
from app.models.database import db
from datetime import datetime


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    type_choices = ["administrator", "default"]

    full_name = CharField(max_length=255)
    email = CharField(max_length=255, unique=True)
    password = CharField(max_length=255)
    type = CharField(choices=type_choices)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        table_name = "account"


db.connect()
db.close()
