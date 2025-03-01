from peewee import *
from app.models.database import db
from app.models.category import Category
from app.models.product import Product

class BaseModel(Model):
    class Meta:
        database = db


class CategoryHasProduct(BaseModel):
    category = ForeignKeyField(Category, backref="products", on_delete="CASCADE")
    product = ForeignKeyField(Product, backref="categories", on_delete="CASCADE")

    class Meta:
        table_name = "category_has_product"
        primary_key = False


db.connect()
db.close()
