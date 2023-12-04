import tkinter as tk
from tkinter import ttk
from view import clienteView, estoqueView
from controller import clienteController, estoqueController

class AppView:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Gerenciamento de Açougue")
        self.master.geometry("1280x720")
        self.master.resizable(False, False)

        self.clienteController = clienteController.ClienteController()
        self.estoqueController = estoqueController.EstoqueController()

        # MenuBar
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        self.client_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Cliente", menu=self.client_menu)
        self.client_menu.add_command(label="Cadastrar Novo Cliente", command=self.cadastrar_novo_cliente)
        self.client_menu.add_command(label="Listar Clientes", command=self.lista_clientes)

        self.stock_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Estoque", menu=self.stock_menu)
        self.stock_menu.add_command(label="Cadastrar Novo Produto", command=self.cadastrar_novo_produto)
        self.stock_menu.add_command(label="Gerenciar Estoque", command=self.listar_produtos)

        self.sales_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Vendas", menu=self.sales_menu)
        self.sales_menu.add_command(label="Listar Notas Fiscais", command=self.master.destroy)

        # Frames
        self.left_frame = ttk.Frame(self.master)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.right_frame = ttk.Frame(self.master)
        self.right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.consumer_frame = ttk.Frame(self.right_frame)
        self.consumer_info_frame = ttk.Frame(self.right_frame)
        self.selected_products_frame = ttk.Frame(self.right_frame)
        self.buttons_frame = ttk.Frame(self.right_frame)
        self.consumer_frame.pack(side='top')
        self.consumer_info_frame.pack(side='top')
        self.selected_products_frame.pack(side='top')
        self.buttons_frame.pack(side='top')

        # Lista de Produtos
        self.products = self.estoqueController.getEstoque()

        self.product_columns = ["Código", "Descrição", "Preço"]
        self.product_tree = ttk.Treeview(self.left_frame, columns=self.product_columns, show="headings", height=30)
        for col in self.product_columns:
            self.product_tree.heading(col, text=col)
        self.product_tree.pack()

        col_width = 200  # Largura desejada para todas as colunas
        for col in self.product_columns:
            self.product_tree.heading(col, text=col)
            self.product_tree.column(col, width=col_width, anchor='center')  # Define a largura e o alinhamento

        for produto in self.products:
            codigo = produto.getCodigo
            desc = produto.getDesc
            preco = produto.getPreco
            self.product_tree.insert("", "end", values=(codigo, desc, preco))

        # Botão "Adicionar produto selecionado"
        self.add_product_button = ttk.Button(self.left_frame, text="Adicionar produto selecionado")
        self.add_product_button.pack(pady=5)

        # Campo para inserir CPF e botão "Consultar CPF"
        self.cpf_label = ttk.Label(self.consumer_frame, text="CPF:")
        self.cpf_label.pack(side='left')
        self.cpf_entry = ttk.Entry(self.consumer_frame)
        self.cpf_entry.pack(side='left')
        self.consult_cpf_button = ttk.Button(self.consumer_frame, text="Consultar CPF", command=self.consultar_cpf)
        self.consult_cpf_button.pack(side='left')

        # Labels para informações do cliente
        self.info_labels_text = ["Nome:", "CPF:", "Endereço:", "Email:"]

        self.label_nome = ttk.Label(self.consumer_info_frame, text=self.info_labels_text[0])
        self.label_cpf = ttk.Label(self.consumer_info_frame, text=self.info_labels_text[1])
        self.label_endereco = ttk.Label(self.consumer_info_frame, text=self.info_labels_text[2])
        self.label_email = ttk.Label(self.consumer_info_frame, text=self.info_labels_text[3])

        self.label_nome.pack(side='top')
        self.label_cpf.pack(side='top')
        self.label_endereco.pack(side='top')
        self.label_email.pack(side='top')

        # Lista de Produtos Selecionados
        self.selected_products_tree = ttk.Treeview(self.selected_products_frame, columns=self.product_columns, show="headings", height=21)
        for col in self.product_columns:
            self.selected_products_tree.heading(col, text=col)
        self.selected_products_tree.pack()

        # Botões "Cancelar Venda" e "Emitir Nota Fiscal"
        self.cancel_button = ttk.Button(self.buttons_frame, text="Cancelar Venda")
        self.cancel_button.pack(side='left', pady=5)
        self.emit_button = ttk.Button(self.buttons_frame, text="Emitir Nota Fiscal")
        self.emit_button.pack(side='left', pady=5)
    

    def cadastrar_novo_cliente(self):
        clienteView.CadastroClienteView(self.master, self.clienteController)
    

    def lista_clientes(self):
        clienteView.ListaClientesView(self.master, self.clienteController)
    

    def cadastrar_novo_produto(self):
        estoqueView.CadastroProdutoView(self.master, self.estoqueController, self.product_tree)
        

    def listar_produtos(self):
        estoqueView.ListaProdutosView(self.master, self.estoqueController, self.product_tree)

    
    def consultar_cpf(self):
        cliente = self.clienteController.buscarCliente(self.cpf_entry.get())
        if cliente:
            self.label_nome.configure(text=f"Nome: {cliente.getNome}")
            self.label_cpf.configure(text=f"CPF: {cliente.getCpf}")
            self.label_endereco.configure(text=f"Endereço: {cliente.getEndereco}")
            self.label_email.configure(text=f"Email: {cliente.getEmail}")
            
            print(self.info_labels_text)



# Exemplo de uso:
root = tk.Tk()
app = AppView(root)
root.mainloop()
