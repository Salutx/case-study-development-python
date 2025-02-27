from app.models.user import User
from app.models.product import Product
from app.models.category import Category

def get_users_count():
    return User.select().count()

def get_products_count():
    return Product.select().count()

def get_categories_count():
    return Category.select().count()