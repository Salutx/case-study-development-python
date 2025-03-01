from peewee import *
from app.models.database import db
from app.models.category import Category
from app.models.user import User


class BaseModel(Model):
    class Meta:
        database = db


class LogAccess(BaseModel):
    account = ForeignKeyField(User, backref="logs", on_delete="CASCADE")

    class Meta:
        table_name = "log_access"
        primary_key = False


db.connect()
db.close()
