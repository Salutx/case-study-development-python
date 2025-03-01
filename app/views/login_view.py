import tkinter as tk
from tkinter import messagebox
from app.controllers.user_controller import login_user
from app.services.session import save_session
from app.views.overview_view import open_overview_view
from app.controllers.log_access_controller import create_access_log


def open_login_view(root):
    root = root if root else tk.Tk()

    root.title("Login")
    root.geometry("300x200")

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Email:").pack()
    entry_email = tk.Entry(root)
    entry_email.pack()

    tk.Label(root, text="Senha:").pack()
    entry_password = tk.Entry(root, show="*")
    entry_password.pack()

    def process_login():
        email = entry_email.get()
        password = entry_password.get()

        user = login_user(email, password)

        if user:
            save_session(user)
            messagebox.showinfo("Login Bem-Sucedido", f"Bem-vindo, {user.full_name}!")
            create_access_log(user.id)

            for widget in root.winfo_children():
                widget.destroy()

            open_overview_view(root)
        else:
            messagebox.showerror("Erro de Login", "Email ou senha incorretos!")

    tk.Button(root, text="Entrar", command=process_login).pack(pady=10)
