import tkinter as tk
from tkinter import ttk
from view import clienteView, estoqueView, vendaView, notaFiscalView
from controller import clienteController, estoqueController, vendasController

class AppView:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Gerenciamento de Açougue")
        self.master.geometry("1280x720")
        self.master.resizable(False, False)

        self.clienteController = clienteController.ClienteController()
        self.estoqueController = estoqueController.EstoqueController()
        self.vendasController = vendasController.VendasController()

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
        self.sales_menu.add_command(label="Mostrar Notas Fiscais", command=self.mostrar_notas_fiscais)

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
        self.add_product_button = ttk.Button(self.left_frame, text="Adicionar produto selecionado", command=self.adicionar_item_venda)
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
        self.vendas_col = ['Produto', 'Preço', 'Peso', 'Total']
        self.selected_products_tree = ttk.Treeview(self.selected_products_frame, columns=self.vendas_col, show="headings", height=25)
        for col in self.vendas_col:
            self.selected_products_tree.heading(col, text=col)
        self.selected_products_tree.pack()

        col_width = 150  # Largura desejada para todas as colunas
        for col in self.vendas_col:
            self.selected_products_tree.heading(col, text=col)
            self.selected_products_tree.column(col, width=col_width, anchor='center')

        self.venda_atual = self.vendasController.getVendaAtual()
        for item_venda in self.venda_atual:
            produto = item_venda.produto.getDesc
            preco = item_venda.produto.getPreco
            peso = self.item_venda.peso
            total = self.item_venda.getValor()
            self.product_tree.insert("", "end", values=(produto, preco, peso, total))
        

        # Botões "Cancelar Venda" e "Emitir Nota Fiscal"
        self.cancel_button = ttk.Button(self.buttons_frame, text="Cancelar Venda")
        self.cancel_button.pack(side='left', pady=5)
        self.emit_button = ttk.Button(self.buttons_frame, text="Emitir Nota Fiscal", command=self.emitir_nota_fiscal)
        self.emit_button.pack(side='left', pady=5)
    

    def atualizar_lista_produtos(self):
        for item in self.product_tree.get_children():
            self.product_tree.delete(item)

        self.products = self.estoqueController.getEstoque()

        for produto in self.products:
            codigo = produto.getCodigo
            desc = produto.getDesc
            preco = produto.getPreco
            self.product_tree.insert("", "end", values=(codigo, desc, preco))
    

    def atualizar_lista_venda(self):
        for item in self.selected_products_tree.get_children():
            self.selected_products_tree.delete(item)
        
        self.venda_atual = self.vendasController.getVendaAtual()

        for item_venda in self.venda_atual:
            produto = item_venda.produto.getDesc
            preco = item_venda.produto.getPreco
            peso = item_venda.peso
            total = item_venda.getValor()
            self.selected_products_tree.insert("", "end", values=(produto, preco, peso, total))


    def cadastrar_novo_cliente(self):
        clienteView.CadastroClienteView(self.master, self.clienteController)
    

    def lista_clientes(self):
        clienteView.ListaClientesView(self.master, self.clienteController)
    

    def cadastrar_novo_produto(self):
        estoqueView.CadastroProdutoView(self.master, self.estoqueController, self)
        

    def listar_produtos(self):
        estoqueView.ListaProdutosView(self.master, self.estoqueController, self)

    
    def consultar_cpf(self):
        self.cliente_selecionado = self.clienteController.buscarCliente(self.cpf_entry.get())
        if self.cliente_selecionado:
            self.label_nome.configure(text=f"Nome: {self.cliente_selecionado.getNome}")
            self.label_cpf.configure(text=f"CPF: {self.cliente_selecionado.getCpf}")
            self.label_endereco.configure(text=f"Endereço: {self.cliente_selecionado.getEndereco}")
            self.label_email.configure(text=f"Email: {self.cliente_selecionado.getEmail}")
            
            print(self.info_labels_text)
    

    def adicionar_item_venda(self):
        selected_item = self.product_tree.selection()
        codigo = int(self.product_tree.item(selected_item, "values")[0])

        vendaView.CriarItemVendaView(self.master, self, self.vendasController, self.estoqueController, codigo)
    

    def emitir_nota_fiscal(self):
        self.vendasController.emitirNota(cliente=self.cliente_selecionado, data='01/02/03', main_view=self)
    

    def mostrar_notas_fiscais(self):
        notaFiscalView.ListaNotasFiscas(self.master, controller=self.vendasController)



# Exemplo de uso:
root = tk.Tk()
app = AppView(root)
root.mainloop()
