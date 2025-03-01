from app.controllers.category_controller import get_categories, add_category
import tkinter as tk
from tkinter import ttk, messagebox


def open_category_view():
    root = tk.Tk()
    all_categories = get_categories().dicts()

    root.title("Painel de Controle - Categorias")
    root.geometry("500x530")

    for widget in root.winfo_children():
        widget.destroy()

    back_button = tk.Button(root, text="Fechar janela", command=lambda: root.destroy())
    back_button.pack(pady=10)

    tree = ttk.Treeview(root)
    tree["columns"] = ("one", "two")
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("one", width=150, minwidth=150, stretch=tk.NO)
    tree.column("two", width=150, minwidth=150, stretch=tk.NO)

    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("one", text="ID", anchor=tk.W)
    tree.heading("two", text="Nome", anchor=tk.W)

    for category in all_categories:
        tree.insert("", tk.END, values=(category["id"], category["name"]))

    tree.pack(pady=10, fill="both", expand=True)

    tk.Label(root, text="Nome da Categoria:").pack()
    entry_name = tk.Entry(root)
    entry_name.pack(pady=2)

    def validate_input():
        name = entry_name.get().strip()

        if not name:
            messagebox.showerror("Erro", "O nome da categoria não pode estar vazio.")
            return None

        return name

    def add_category_to_db():
        name = validate_input()
        if name:
            add_category(name)
            messagebox.showinfo("Sucesso", "Categoria adicionada com sucesso!")

            entry_name.delete(0, tk.END)
            update_categories()

    def update_categories():
        all_categories = get_categories().dicts()
        tree.delete(*tree.get_children())
        for category in all_categories:
            tree.insert("", tk.END, values=(category["id"], category["name"]))

    btn_add = tk.Button(root, text="Adicionar Categoria", command=add_category_to_db)
    btn_add.pack(pady=5)

    root.mainloop()
