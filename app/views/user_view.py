from app.controllers.user_controller import get_users, add_user
import tkinter as tk
from tkinter import ttk, messagebox
import re


def open_user_view():
    root = tk.Tk()
    root.title("Painel de Controle - Usuários")
    root.geometry("500x530")

    for widget in root.winfo_children():
        widget.destroy()

    all_users = get_users().dicts()

    back_button = tk.Button(root, text="Fechar janela", command=lambda: root.destroy())
    back_button.pack(pady=10)

    users_table = ttk.Treeview(
        root,
        columns=("id", "full_name", "email", "type", "created_at"),
        show="headings",
    )
    users_table.heading("id", text="ID")
    users_table.heading("full_name", text="Nome Completo")
    users_table.heading("email", text="E-mail")
    users_table.heading("type", text="Tipo de Usuário")
    users_table.heading("created_at", text="Criado em")

    users_table.column("id", width=50, anchor="center")
    users_table.column("full_name", width=150, anchor="w")
    users_table.column("email", width=180, anchor="w")
    users_table.column("type", width=100, anchor="center")
    users_table.column("created_at", width=120, anchor="center")

    formatted_created_at = lambda user: user["created_at"].strftime("%d/%m/%Y %H:%M:%S")

    for user in all_users:
        users_table.insert(
            "",
            "end",
            values=(
                user["id"],
                user["full_name"],
                user["email"],
                user["type"],
                formatted_created_at(user),
            ),
        )

    users_table.pack(pady=10, fill="both", expand=True)

    tk.Label(root, text="Nome Completo:").pack()
    entry_name = tk.Entry(root)
    entry_name.pack(pady=2)

    tk.Label(root, text="E-mail:").pack()
    entry_email = tk.Entry(root)
    entry_email.pack(pady=2)

    tk.Label(root, text="Senha:").pack()
    entry_password = tk.Entry(root)
    entry_password.pack(pady=2)

    tk.Label(root, text="Tipo de Usuário:").pack()
    user_type_dropdown = ttk.Combobox(root, values=["administrator", "default"])
    user_type_dropdown.current(0)
    user_type_dropdown.pack(pady=2)

    def validate_inputs():
        new_user_name = entry_name.get().strip()
        new_user_email = entry_email.get().strip()
        new_user_password = entry_password.get().strip()
        new_user_type = user_type_dropdown.get()

        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

        if not new_user_name:
            messagebox.showerror("Erro", "O nome completo é obrigatório.")
            return None

        if not re.match(email_regex, new_user_email):
            messagebox.showerror("Erro", "E-mail inválido.")
            return None

        if len(new_user_password) < 6:
            messagebox.showerror("Erro", "A senha deve ter pelo menos 6 caracteres.")
            return None

        return {
            "name": new_user_name,
            "email": new_user_email,
            "password": new_user_password,
            "type": new_user_type,
        }

    def add_user_to_list():
        user_data = validate_inputs()
        if user_data:
            add_user(
                user_data["name"],
                user_data["email"],
                user_data["password"],
                user_data["type"],
            )
            messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso!")

            entry_name.delete(0, tk.END)
            entry_email.delete(0, tk.END)
            entry_password.delete(0, tk.END)
            user_type_dropdown.current(0)

            update_users()

    def update_users():
        all_users = get_users().dicts()
        users_table.delete(*users_table.get_children())
        for user in all_users:
            users_table.insert(
                "",
                "end",
                values=(
                    user["id"],
                    user["full_name"],
                    user["email"],
                    user["type"],
                    formatted_created_at(user),
                ),
            )

    add_user_button = tk.Button(
        root, text="Adicionar Usuário", command=add_user_to_list
    )
    add_user_button.pack(pady=10)

    root.mainloop()
