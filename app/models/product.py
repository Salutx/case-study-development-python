from peewee import *
from app.models.database import db
from datetime import datetime


class BaseModel(Model):
    class Meta:
        database = db


class Product(BaseModel):
    name = CharField(max_length=255)
    description = TextField(null=True)
    quantity = IntegerField()
    min_stock = IntegerField()
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        table_name = "product"


db.connect()
db.close()
