import tkinter as tk
from tkinter import ttk, messagebox

class CadastroClienteView(tk.Toplevel):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.title("Cadastro de Cliente")
        self.geometry("300x200")
        self.resizable(False, False)

        # Bloqueia a interação com a janela principal enquanto a janela de cadastro estiver ativa
        self.grab_set()

        # Formulário para cadastro de novo cliente
        self.form_frame = ttk.Frame(self)
        self.form_frame.pack(padx=10, pady=10)

        self.nome_label = ttk.Label(self.form_frame, text="Nome:")
        self.nome_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.nome_entry = ttk.Entry(self.form_frame)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=5)

        self.cpf_label = ttk.Label(self.form_frame, text="CPF:")
        self.cpf_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.cpf_entry = ttk.Entry(self.form_frame)
        self.cpf_entry.grid(row=1, column=1, padx=5, pady=5)

        self.endereco_label = ttk.Label(self.form_frame, text="Endereço:")
        self.endereco_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.endereco_entry = ttk.Entry(self.form_frame)
        self.endereco_entry.grid(row=2, column=1, padx=5, pady=5)

        self.email_label = ttk.Label(self.form_frame, text="Email:")
        self.email_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.email_entry = ttk.Entry(self.form_frame)
        self.email_entry.grid(row=3, column=1, padx=5, pady=5)

        # Botão "Cadastrar Cliente"
        self.cadastrar_button = ttk.Button(self, text="Cadastrar Cliente", command=self.cadastrar_cliente)
        self.cadastrar_button.pack(pady=10)


    def cadastrar_cliente(self):
        # Lógica para cadastrar o cliente
        nome = self.nome_entry.get()
        cpf = self.cpf_entry.get()
        endereco = self.endereco_entry.get()
        email = self.email_entry.get()

        resultado = self.controller.cadastrarCliente(nome, cpf, endereco, email)

        # Fechar a janela de cadastro após o cadastro do cliente
        self.destroy()


class ListaClientesView(tk.Toplevel):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.title("Lista de Clientes")
        self.geometry("700x360")
        self.resizable(False, False)

        # Bloqueia a interação com a janela principal enquanto a janela de lista estiver ativa
        self.grab_set()

        # Lista de Clientes
        self.clientes_frame = ttk.Frame(self)
        self.clientes_frame.pack(padx=10, pady=10)
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(padx=10, pady=10)

        self.clientes_columns = ["Nome", "CPF", "Endereço", "Email"]
        self.clientes_tree = ttk.Treeview(self.clientes_frame, columns=self.clientes_columns, show="headings", height=12)
        for col in self.clientes_columns:
            self.clientes_tree.heading(col, text=col)
        self.clientes_tree.pack()

        col_width = 150  # Largura desejada para todas as colunas
        for col in self.clientes_columns:
            self.clientes_tree.heading(col, text=col)
            self.clientes_tree.column(col, width=col_width, anchor='center')  # Define a largura e o alinhamento

        # Preenche a lista de clientes
        for cliente in self.controller.getClientes():
            nome = cliente.getNome
            cpf = cliente.getCpf
            endereco = cliente.getEndereco
            email = cliente.getEmail
            self.clientes_tree.insert("", "end", text=cliente, values=(nome, cpf, endereco, email))

        # Botão "Deletar Cliente"
        self.deletar_button = ttk.Button(self.button_frame, text="Deletar Cliente", command=self.deletar_cliente)
        self.deletar_button.pack(pady=5)


    def deletar_cliente(self):
        selected_item = self.clientes_tree.selection()
        cpf = str(self.clientes_tree.item(selected_item, "values")[1])
        resultado = self.controller.deletarCliente(cpf)

        if resultado:
            self.clientes_tree.delete(selected_item)
