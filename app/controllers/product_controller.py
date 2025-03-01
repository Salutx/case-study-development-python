from app.models.product import Product
from app.controllers.category_has_product_controller import add_categories_in_product


def add_product(name, description, quantity, min_stock, categories):
    product = Product.create(
        name=name, description=description, quantity=quantity, min_stock=min_stock
    )

    add_categories_in_product(product.id, categories)

    print("Product created: ", product.name)
    return product


def get_products():
    return Product.select()
