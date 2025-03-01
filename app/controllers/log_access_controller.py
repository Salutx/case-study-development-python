from app.models.log_access import LogAccess


def get_all_logs():
    return LogAccess.select()


def get_log_by_id(log_id):
    return LogAccess.get_by_id(log_id)


def create_access_log(userId):
    return LogAccess.create(account=userId)
