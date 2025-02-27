import tkinter as tk
from app.views.login_view import open_login_view
from app.services.session import get_session
from app.views.overview_view import open_overview_view

root = tk.Tk()
root.title("Painel de Controle - Estoque")
root.geometry("400x300")

user_id = get_session()


def open_main():
    if not user_id:
        open_login_view(root)
    else:
        open_overview_view(root)
        tk.Label(
            root, text=f"Usuário ID {user_id} está logado!", font=("Arial", 12)
        ).pack()

    root.mainloop()
