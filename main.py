import tkinter as tk
from tkinter import ttk
from view import clienteView, estoqueView
from controller import clienteController, estoqueController


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gerenciamento de Açougue")

        self.clienteController = clienteController.ClienteController()
        self.estoqueController = estoqueController.EstoqueController()

        self.notebook = ttk.Notebook(self)

        # Aba de Clientes
        self.cliente_main_view = clienteView.MainView(self, controller=self.clienteController)
        self.notebook.add(self.cliente_main_view, text="Clientes")
        
        # Aba de Estoque
        self.estoque_main_view = estoqueView.EstoqueMainView(self, controller=self.estoqueController)
        self.notebook.add(self.estoque_main_view, text="Estoque")

        self.notebook.pack(expand=True, fill=tk.BOTH)

# Exemplo de uso
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()