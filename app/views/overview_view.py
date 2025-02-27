import tkinter as tk
from app.controllers.overview_controller import (
    get_users_count,
    get_products_count,
    get_categories_count,
)
from app.views.category_view import open_category_view
from app.views.product_view import open_product_view
from app.views.user_view import open_user_view


def open_overview_view(current_root):
    root = current_root
    root.title("Painel de Controle - Estoque")
    root.geometry("400x300")

    def update_overview():
        label_usuarios.config(text=f"Usuários cadastrados: {get_users_count()}")
        label_produtos.config(text=f"Produtos cadastrados: {get_products_count()}")
        label_categorias.config(
            text=f"Categorias cadastradas: {get_categories_count()}"
        )

    label_usuarios = tk.Label(root, text="Usuários cadastrados: 0", font=("Arial", 12))
    label_usuarios.pack(pady=5)

    label_produtos = tk.Label(root, text="Produtos cadastrados: 0", font=("Arial", 12))
    label_produtos.pack(pady=5)

    label_categorias = tk.Label(
        root, text="Categorias cadastradas: 0", font=("Arial", 12)
    )
    label_categorias.pack(pady=5)

    btn_categoria = tk.Button(
        root, text="Criar Categorias", command=open_category_view, width=20
    )
    btn_categoria.pack(pady=5)

    btn_produto = tk.Button(
        root, text="Criar Produtos", command=open_product_view, width=20
    )
    btn_produto.pack(pady=5)

    btn_usuario = tk.Button(
        root, text="Criar Usuários", command=open_user_view, width=20
    )
    btn_usuario.pack(pady=5)

    update_overview()

    root.mainloop()
