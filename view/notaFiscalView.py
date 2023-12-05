import tkinter as tk
from tkinter import ttk


class ListaNotasFiscas(tk.Toplevel):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller

        self.title("Lista de Clientes")
        self.geometry("700x360")
        self.resizable(False, False)
        self.grab_set()

        self.notasFiscais_frame = ttk.Frame(self)
        self.notasFiscais_frame.pack(padx=10, pady=10)

        self.columns = ["Id", "Data", "Cliente", "Valor Total"]
        self.lista_tree = ttk.Treeview(self.notasFiscais_frame, columns=self.columns, show="headings", height=12)
        for col in self.columns:
            self.lista_tree.heading(col, text=col)
        self.lista_tree.pack()

        col_width = 150  # Largura desejada para todas as colunas
        for col in self.columns:
            self.lista_tree.heading(col, text=col)
            self.lista_tree.column(col, width=col_width, anchor='center')  # Define a largura e o alinhamento

        # Preenche a lista de clientes

        for nota in self.controller.getNotasFiscais():
            Id = nota.Id
            data = nota.data
            cliente = nota.cliente.getNome
            valorTotal = nota.valorTotal
            self.lista_tree.insert("", "end", text=cliente, values=(Id, data, cliente, valorTotal))
