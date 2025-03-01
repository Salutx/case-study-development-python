from app.models.log_moviments import LogMoviments


def get_all_logs():
    return LogMoviments.select()


def get_log_by_id(log_id):
    return LogMoviments.get_by_id(log_id)


def create_moviment_log(userId, productId, quantity, type):

    return LogMoviments.create(
        account=userId, product=productId, quantity=quantity, type=type
    )


def get_all_logs_by_user(userId):
    return LogMoviments.select().where(LogMoviments.account == userId)


def get_all_logs_by_product(productId):
    return LogMoviments.select().where(LogMoviments.product == productId)


def get_all_logs_by_type(type):
    return LogMoviments.select().where(LogMoviments.type == type)
