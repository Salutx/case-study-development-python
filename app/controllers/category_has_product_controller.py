from app.models.category_has_product import CategoryHasProduct
from app.models.category import Category

def add_categories_in_product(product_id, categories):
    for category in categories:
        CategoryHasProduct.create(product_id=product_id, category_id=category)

    print("Categories added to product: ", product_id)


def get_categories_in_product():
    return CategoryHasProduct.select()


def get_categories_in_product_by_product_id(product_id):
    return (
        Category.select()
        .join(CategoryHasProduct)
        .where(CategoryHasProduct.product == product_id)
        .dicts()
    )
