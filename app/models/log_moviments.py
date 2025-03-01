from peewee import *
from app.models.database import db
from app.models.product import Product
from app.models.user import User
from datetime import datetime


class BaseModel(Model):
    class Meta:
        database = db


class LogMoviments(BaseModel):
    type_choices = ["input", "output"]

    id = AutoField()
    account = ForeignKeyField(User, backref="logs", on_delete="CASCADE")
    product = ForeignKeyField(Product, backref="logs", on_delete="CASCADE")
    created_at = DateTimeField(default=datetime.now)
    type = CharField(choices=type_choices)
    quantity = IntegerField()

    class Meta:
        table_name = "log_moviments"


db.connect()
db.close()
