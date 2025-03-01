from app.controllers.product_controller import get_products
from app.controllers.user_controller import get_users
from app.controllers.log_moviments_controller import get_all_logs, create_moviment_log
import tkinter as tk
from tkinter import ttk, messagebox
from app.services.session import get_session

user_id = get_session()


def open_product_moviments_view():
    root = tk.Tk()
    root.title("Movimentação de Produtos")
    root.geometry("800x600")

    all_products = get_products().dicts()
    all_users = get_users().dicts()

    tk.Label(root, text="Produto:").pack()
    product_dropdown = ttk.Combobox(
        root, values=[f"{p['id']} - {p['name']}" for p in all_products]
    )
    product_dropdown.pack(pady=2)
    product_dropdown.current(0)

    tk.Label(root, text="Tipo de Movimentação:").pack()
    type_var = tk.StringVar(value="input")
    type_dropdown = ttk.Combobox(
        root, textvariable=type_var, values=["input", "output"], state="readonly"
    )
    type_dropdown.pack(pady=2)
    type_dropdown.current(0)

    tk.Label(root, text="Quantidade:").pack()
    entry_quantity = tk.Entry(root)
    entry_quantity.pack(pady=2)

    def add_moviment_log():
        selected_product = product_dropdown.get().split(" - ")[0]
        moviment_type = type_var.get()
        quantity = entry_quantity.get().strip()

        if not quantity.isdigit():
            messagebox.showerror("Erro", "A quantidade deve ser um número inteiro.")
            return

        create_moviment_log(user_id, int(selected_product), quantity, moviment_type)
        messagebox.showinfo("Sucesso", "Movimentação registrada com sucesso!")
        entry_quantity.delete(0, tk.END)
        update_moviment_table()

    btn_add = tk.Button(root, text="Registrar Movimentação", command=add_moviment_log)
    btn_add.pack(pady=5)

    tree = ttk.Treeview(
        root, columns=("id", "user", "product", "type", 'quantity', "created_at"), show="headings"
    )
    tree.heading("id", text="ID", anchor="center")
    tree.heading("user", text="Usuário", anchor="w")
    tree.heading("product", text="Produto", anchor="w")
    tree.heading("type", text="Tipo", anchor="center")
    tree.heading("quantity", text="Quantidade", anchor="center")
    tree.heading("created_at", text="Data/Hora", anchor="center")

    tree.column("id", width=50, anchor="center")
    tree.column("user", width=150, anchor="w")
    tree.column("product", width=150, anchor="w")
    tree.column("type", width=100, anchor="center")
    tree.column("quantity", width=100, anchor="center")
    tree.column("created_at", width=150, anchor="center")

    tree.pack(pady=10, fill="both", expand=True)

    def update_moviment_table():
        tree.delete(*tree.get_children())
        logs = get_all_logs().dicts()

        for log in logs:

            user_name = next(
                (u["full_name"] for u in all_users if u["id"] == log["account"]), ""
            )
            product_name = next(
                (p["name"] for p in all_products if p["id"] == log["product"]), ""
            )

            tree.insert(
                "",
                "end",
                values=(
                    log["id"],
                    user_name,
                    product_name,
                    log["type"],
                    log["quantity"],
                    log["created_at"].strftime("%d/%m/%Y %H:%M:%S"),
                ),
            )

    update_moviment_table()

    root.mainloop()
