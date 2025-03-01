from app.controllers.product_controller import get_products, add_product
from app.controllers.category_controller import get_categories
from app.controllers.category_has_product_controller import (
    get_categories_in_product_by_product_id,
)
from app.views.product_moviments_view import open_product_moviments_view
import tkinter as tk
from tkinter import ttk, messagebox


def open_product_view():
    root = tk.Tk()
    root.title("Painel de Controle - Produtos")
    root.geometry("900x650")

    all_products = get_products().dicts()
    all_categories = get_categories().dicts()

    back_button = tk.Button(root, text="Fechar janela", command=lambda: root.destroy())
    back_button.pack(pady=10)
    
    moviments_button = tk.Button(root, text="Movimentação de Produtos", command=open_product_moviments_view)
    moviments_button.pack(pady=10)

    tree = ttk.Treeview(
        root,
        columns=(
            "id",
            "name",
            "description",
            "quantity",
            "min_stock",
            "missing",
            "categories",
            "created_at",
        ),
        show="headings",
    )

    tree.heading("id", text="ID", anchor="center")
    tree.heading("name", text="Nome", anchor="w")
    tree.heading("description", text="Descrição", anchor="w")
    tree.heading("quantity", text="Quantidade", anchor="center")
    tree.heading("min_stock", text="Estoque Mínimo", anchor="center")
    tree.heading("missing", text="Faltando", anchor="center")
    tree.heading("categories", text="Categorias", anchor="w")
    tree.heading("created_at", text="Criado em", anchor="center")

    tree.column("id", width=50, anchor="center")
    tree.column("name", width=150, anchor="w")
    tree.column("description", width=150, anchor="w")
    tree.column("quantity", width=100, anchor="center")
    tree.column("min_stock", width=100, anchor="center")
    tree.column("missing", width=100, anchor="center")
    tree.column("categories", width=150, anchor="w")
    tree.column("created_at", width=150, anchor="center")

    for product in all_products:
        product_categories = get_categories_in_product_by_product_id(
            product["id"]
        ).dicts()
        product_categories_names = [category["name"] for category in product_categories]
        product_categories_names = ", ".join(product_categories_names)
        product_missing_quantity = product["min_stock"] - product["quantity"]
        product_missing_quantity = (
            0 if product_missing_quantity < 0 else product_missing_quantity
        )

        tree.insert(
            "",
            "end",
            values=(
                product["id"],
                product["name"],
                product["description"],
                product["quantity"],
                product["min_stock"],
                product_missing_quantity,
                product_categories_names,
                product["created_at"],
            ),
        )

    tree.pack(pady=10, fill="both")

    tk.Label(root, text="Nome do Produto:").pack()
    entry_name = tk.Entry(root)
    entry_name.pack(pady=2)

    tk.Label(root, text="Descrição do Produto:").pack()
    entry_description = tk.Entry(root)
    entry_description.pack(pady=2)

    tk.Label(root, text="Quantidade do Produto:").pack()
    entry_quantity = tk.Entry(root)
    entry_quantity.pack(pady=2)

    tk.Label(root, text="Estoque Mínimo do Produto:").pack()
    entry_min_stock = tk.Entry(root)
    entry_min_stock.pack(pady=2)

    tk.Label(root, text="Categorias do Produto:").pack()
    listbox_categories = tk.Listbox(root, selectmode=tk.MULTIPLE, height=5)
    for category in all_categories:
        listbox_categories.insert(tk.END, category["name"])
    listbox_categories.pack(pady=2)

    def validate_inputs():
        name = entry_name.get().strip()
        description = entry_description.get().strip()
        quantity = entry_quantity.get().strip()
        min_stock = entry_min_stock.get().strip()
        selected_indices = listbox_categories.curselection()

        if not name or not description or not quantity or not min_stock:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return None

        if not quantity.isdigit() or not min_stock.isdigit():
            messagebox.showerror(
                "Erro", "Quantidade e Estoque Mínimo devem ser números inteiros."
            )
            return None

        if not selected_indices:
            messagebox.showerror("Erro", "Selecione pelo menos uma categoria.")
            return None

        return {
            "name": name,
            "description": description,
            "quantity": int(quantity),
            "min_stock": int(min_stock),
            "categories_ids": [all_categories[i]["id"] for i in selected_indices],
        }

    def add_product_to_db():
        product_data = validate_inputs()
        if product_data:
            add_product(
                product_data["name"],
                product_data["description"],
                product_data["quantity"],
                product_data["min_stock"],
                product_data["categories_ids"],
            )
            messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
            entry_name.delete(0, tk.END)
            entry_description.delete(0, tk.END)
            entry_quantity.delete(0, tk.END)
            entry_min_stock.delete(0, tk.END)
            listbox_categories.selection_clear(0, tk.END)
            update_products()

    def update_products():
        tree.delete(*tree.get_children()) 
        updated_products = get_products().dicts()
        for product in updated_products:
            product_categories = get_categories_in_product_by_product_id(
                product["id"]
            ).dicts()
            product_categories_names = ", ".join(
                [category["name"] for category in product_categories]
            )
            product_missing_quantity = product["min_stock"] - product["quantity"]
            product_missing_quantity = max(0, product_missing_quantity)

            tree.insert(
                "",
                tk.END,
                values=(
                    product["id"],
                    product["name"],
                    product["description"],
                    product["quantity"],
                    product["min_stock"],
                    product_missing_quantity,
                    product_categories_names,
                    product["created_at"],
                ),
            )

    btn_add = tk.Button(root, text="Adicionar Produto", command=add_product_to_db)
    btn_add.pack(pady=5)

    root.mainloop()
