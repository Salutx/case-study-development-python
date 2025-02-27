from app.models.user import User
from app.services.session import save_session


def add_user(full_name, email, password, type):
    user = User.create(
        full_name=full_name,
        email=email,
        password=password,
        type=type,
    )
    print("User created: ", user.name)
    return user


def get_users():
    return User.select()


def login_user(email, password):
    user = User.get_or_none(User.email == email)

    if user and user.password == password:
        print(f"Usuário logado: {user.full_name}")
        save_session(user)
        return user
    else:
        print("Falha no login")
        return None
