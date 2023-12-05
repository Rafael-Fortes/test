import tkinter as tk
from tkinter import ttk

class CadastroProdutoView(tk.Toplevel):
    def __init__(self, master, controller, main_view):
        super().__init__(master)

        self.controller = controller
        self.main_view = main_view

        self.title("Cadastro de Produto")
        self.geometry("300x200")
        self.resizable(False, False)
        self.grab_set()

        # Formulário para cadastro de novo produto
        self.form_frame = ttk.Frame(self)
        self.form_frame.pack(padx=10, pady=10)

        self.codigo_label = ttk.Label(self.form_frame, text="Código:")
        self.codigo_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.codigo_entry = ttk.Entry(self.form_frame)
        self.codigo_entry.grid(row=0, column=1, padx=5, pady=5)

        self.descricao_label = ttk.Label(self.form_frame, text="Descrição:")
        self.descricao_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.descricao_entry = ttk.Entry(self.form_frame)
        self.descricao_entry.grid(row=1, column=1, padx=5, pady=5)

        self.preco_label = ttk.Label(self.form_frame, text="Preço:")
        self.preco_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.preco_entry = ttk.Entry(self.form_frame)
        self.preco_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botão "Cadastrar Produto"
        self.cadastrar_button = ttk.Button(self, text="Cadastrar Produto", command=self.cadastrar_produto)
        self.cadastrar_button.pack(pady=10)


    def cadastrar_produto(self):
        codigo = int(self.codigo_entry.get())
        descricao = str(self.descricao_entry.get())
        preco = float(self.preco_entry.get())

        resultado = self.controller.cadastrarProduto(codigo, descricao, preco)

        self.main_view.atualizar_lista_produtos()

        self.destroy()


class ListaProdutosView(tk.Toplevel):
    def __init__(self, master, controller, main_view):
        super().__init__(master)
        self.controller = controller
        self.main_view = main_view

        self.title("Lista de Produtos")
        self.geometry("640x360")
        self.resizable(False, False)
        self.grab_set()


        self.produtos_frame = ttk.Frame(self)
        self.produtos_frame.pack(padx=10, pady=10)
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(padx=10, pady=10)

        self.produtos_columns = ["Código", "Descrição", "Preço por Quilo"]
        self.produtos_tree = ttk.Treeview(self.produtos_frame, columns=self.produtos_columns, show="headings", height=12)

        for col in self.produtos_columns:
            self.produtos_tree.heading(col, text=col)
            self.produtos_tree.column(col, width=150, anchor='center') 

        self.produtos_tree.pack()

        produtos = controller.getEstoque()
        for produto in produtos:
            codigo = produto.getCodigo
            desc = produto.getDesc
            preco = produto.getPreco

            self.produtos_tree.insert("", "end", values=(codigo, desc, preco))

        self.alterar_button = ttk.Button(self.button_frame, text="Alterar Dados do Produto", command=self.alterar_produto)
        self.alterar_button.pack(side='left', pady=5)

        self.deletar_button = ttk.Button(self.button_frame, text="Deletar Produto", command=self.deletar_produto)
        self.deletar_button.pack(side='left', pady=5)


    def atualizar_lista_produtos(self):
        for item in self.produtos_tree.get_children():
            self.produtos_tree.delete(item)

        produtos = self.controller.getEstoque()

        for produto in produtos:
            codigo = produto.getCodigo
            desc = produto.getDesc
            preco = produto.getPreco
            self.produtos_tree.insert("", "end", values=(codigo, desc, preco))


    def alterar_produto(self):
        selected_item = self.produtos_tree.selection()
        codigo = int(self.produtos_tree.item(selected_item, "values")[0])
        desc = str(self.produtos_tree.item(selected_item, "values")[1])
        preco = float(self.produtos_tree.item(selected_item, "values")[2])

        AlterarProdutoView(self, self.controller, selected_item, codigo, desc, preco, self.main_view, self)


    def deletar_produto(self):
        selected_item = self.produtos_tree.selection()
        codigo = int(self.produtos_tree.item(selected_item, "values")[0])
        resultado = self.controller.deletarProduto(codigo)

        if resultado:
            self.atualizar_lista_produtos()
            self.main_view.atualizar_lista_produtos()
        
        selected_item = None


class AlterarProdutoView(tk.Toplevel):
    def __init__(self, master, controller, id, codigo_produto, descricao_atual, preco_atual, main_view, second_view):
        super().__init__(master)
        self.title("Alterar Produto")
        self.geometry("300x200")
        self.resizable(False, False)

        self.controller = controller
        self.id = id
        self.codigo_produto = codigo_produto
        self.main_view = main_view
        self.second_view = second_view

        self.descricao_label = ttk.Label(self, text="Descrição:")
        self.descricao_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.descricao_entry = ttk.Entry(self)
        self.descricao_entry.insert(0, descricao_atual)
        self.descricao_entry.grid(row=0, column=1, padx=5, pady=5)

        self.preco_label = ttk.Label(self, text="Preço:")
        self.preco_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

        self.preco_entry = ttk.Entry(self)
        self.preco_entry.insert(0, preco_atual)
        self.preco_entry.grid(row=1, column=1, padx=5, pady=5)

        self.confirmar_button = ttk.Button(self, text="Alterar", command=self.confirmar_alteracao)
        self.confirmar_button.grid(row=2, column=0, columnspan=2, pady=10)

    def confirmar_alteracao(self):
        nova_descricao = str(self.descricao_entry.get())
        novo_preco = float(self.preco_entry.get())

        # Chama a função no controlador para alterar o produto
        resultado = self.controller.alterarProduto(self.codigo_produto, nova_descricao, novo_preco)

        if resultado:
            self.main_view.atualizar_lista_produtos()
            self.second_view.atualizar_lista_produtos()

            self.destroy()
        else:
            # Pode adicionar lógica para lidar com falhas na alteração, se necessário
            print("Falha na alteração do produto")
