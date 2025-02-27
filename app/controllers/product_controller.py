from app.models.product import Product


def add_product(name, description, quantity, min_stock):
    product = Product.create(
        name=name, description=description, quantity=quantity, min_stock=min_stock
    )
    print("Product created: ", product.name)
    return product


def get_products():
    return Product.select()
