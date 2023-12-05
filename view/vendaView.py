import tkinter as tk
from tkinter import ttk
from model import produtos


class CriarItemVendaView(tk.Toplevel):
    def __init__(self, master, main_view, vendas_controller, estoque_controller, codigo_produto):
        super().__init__(master)

        self.title("Criar Item de Venda")
        self.geometry("300x150")
        self.resizable(False, False)
        self.grab_set()

        self.main_view = main_view
        self.controller = vendas_controller
        self.estoque_controller = estoque_controller
        self.codigo_produto = codigo_produto

        # Labels e Entry para inserir o peso do produto
        self.peso_label = ttk.Label(self, text="Peso (em quilos):")
        self.peso_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.peso_entry = ttk.Entry(self)
        self.peso_entry.grid(row=0, column=1, padx=5, pady=5)

        # Botão para confirmar a criação do ItemVenda
        self.confirmar_button = ttk.Button(self, text="Confirmar", command=self.adicionar_item_venda)
        self.confirmar_button.grid(row=1, column=0, columnspan=2, pady=10)

    def adicionar_item_venda(self):
        try:
            peso = float(self.peso_entry.get())
            produto = self.estoque_controller.buscarProduto(self.codigo_produto)
            resultado = self.controller.adicionarProduto(produto, peso)

            if resultado:
                self.main_view.atualizar_lista_venda()
                self.destroy()
            else:
                print("Falha na criação do ItemVenda")
        except ValueError:
            print("Peso inválido. Certifique-se de inserir um número válido.")
