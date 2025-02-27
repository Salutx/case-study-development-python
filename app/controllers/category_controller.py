from app.models.category import Category


def add_category(name):
    category = Category.create(name=name)
    print("Category created: ", category.name)
    return category


def get_categories():
    return Category.select()
