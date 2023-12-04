import tkinter as tk
from tkinter import ttk

class CadastroProdutoView(tk.Toplevel):
    def __init__(self, master, controller, main_tree):
        super().__init__(master)

        self.controller = controller
        self.main_tree = main_tree

        self.title("Cadastro de Produto")
        self.geometry("300x200")
        self.resizable(False, False)

        # Bloqueia a interação com a janela principal enquanto a janela de cadastro estiver ativa
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
        # Lógica para cadastrar o produto
        codigo = self.codigo_entry.get()
        descricao = self.descricao_entry.get()
        preco = self.preco_entry.get()

        # Exemplo: Imprimir as informações (substituir por lógica real)
        print(f"Código: {codigo}, Descrição: {descricao}, Preço por Quilo: {preco}")

        resultado = self.controller.cadastrarProduto(codigo, descricao, preco)

        if resultado:
            produto = self.controller.getEstoque()[-1]
            codigo = produto.getCodigo
            desc = produto.getDesc
            preco = produto.getPreco
            self.main_tree.insert("", "end", values=(codigo, desc, preco))

        # Fechar a janela de cadastro após o cadastro do produto
        self.destroy()


class ListaProdutosView(tk.Toplevel):
    def __init__(self, master, controller, main_tree):
        super().__init__(master)
        self.controller = controller
        self.main_tree = main_tree
        self.produtos = controller.getEstoque()

        self.title("Lista de Produtos")
        self.geometry("640x360")
        self.resizable(False, False)

        # Bloqueia a interação com a janela principal enquanto a janela de lista estiver ativa
        self.grab_set()

        # Lista de Produtos
        self.produtos_frame = ttk.Frame(self)
        self.produtos_frame.pack(padx=10, pady=10)
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(padx=10, pady=10)

        self.produtos_columns = ["Código", "Descrição", "Preço por Quilo"]
        self.produtos_tree = ttk.Treeview(self.produtos_frame, columns=self.produtos_columns, show="headings", height=12)

        # Configuração da largura fixa das colunas
        col_width = 150  # Largura desejada para todas as colunas
        for col in self.produtos_columns:
            self.produtos_tree.heading(col, text=col)
            self.produtos_tree.column(col, width=col_width, anchor='center')  # Define a largura e o alinhamento

        self.produtos_tree.pack()

        # Preenche a lista de produtos
        for produto in self.produtos:
            codigo = produto.getCodigo
            desc = produto.getDesc
            preco = produto.getPreco

            self.produtos_tree.insert("", "end", values=(codigo, desc, preco))

        # Botões "Alterar dados do produto" e "Deletar Produto"
        self.alterar_button = ttk.Button(self.button_frame, text="Alterar Dados do Produto", command=self.alterar_produto)
        self.alterar_button.pack(side='left', pady=5)

        self.deletar_button = ttk.Button(self.button_frame, text="Deletar Produto", command=self.deletar_produto)
        self.deletar_button.pack(side='left', pady=5)


    def alterar_produto(self):
        # Lógica para alterar dados do produto (substituir por lógica real)
        selected_item = self.produtos_tree.selection()
        codigo = int(self.produtos_tree.item(selected_item, "values")[0])
        desc = str(self.produtos_tree.item(selected_item, "values")[1])
        preco = float(self.produtos_tree.item(selected_item, "values")[2])

        AlterarProdutoView(self, self.controller, codigo, desc, preco, self.main_tree, self.produtos_tree)


    def deletar_produto(self):
        # Lógica para deletar produto (substituir por lógica real)
        selected_item = self.produtos_tree.selection()
        codigo = int(self.produtos_tree.item(selected_item, "values")[0])
        resultado = self.controller.deletarProduto(codigo)

        if resultado:
            self.produtos_tree.delete(selected_item)
            self.main_tree.delete(selected_item)
        
        selected_item = None


class AlterarProdutoView(tk.Toplevel):
    def __init__(self, master, controller, codigo_produto, descricao_atual, preco_atual, main_tree, manage_tree):
        super().__init__(master)
        self.title("Alterar Produto")
        self.geometry("300x200")
        self.resizable(False, False)

        self.controller = controller
        self.codigo_produto = codigo_produto
        self.main_tree = main_tree
        self.manage_tree = manage_tree

        # Labels e Entry para a alteração de descrição e preço
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

        # Botão para confirmar a alteração
        self.confirmar_button = ttk.Button(self, text="Alterar", command=self.confirmar_alteracao)
        self.confirmar_button.grid(row=2, column=0, columnspan=2, pady=10)

    def confirmar_alteracao(self):
        nova_descricao = str(self.descricao_entry.get())
        novo_preco = float(self.preco_entry.get())

        # Chama a função no controlador para alterar o produto
        resultado = self.controller.alterarProduto(self.codigo_produto, nova_descricao, novo_preco)

        if resultado:
            # Fecha a janela de alteração após o resultado
            produto = self.controller.buscarProduto(self.codigo_produto)
            codigo = produto.getCodigo
            desc = produto.getDesc
            preco = produto.getPreco

            self.main_tree.update("", "end", values=(codigo, desc, preco))
            self.manage_tree.update("", "end", values=(codigo, desc, preco))

            self.destroy()
        else:
            # Pode adicionar lógica para lidar com falhas na alteração, se necessário
            print("Falha na alteração do produto")
