from model import vendas, produtos, cliente, notaFiscal


class VendasController:
    def __init__(self):
        self.listaNotasFiscas = []
        self.listaVendaAtual = []
        self.qtdId = 0
    

    def emitirNota(self, cliente: cliente.Cliente, data:str, main_view) -> bool:
        valorTotal = 0

        for item_venda in self.listaVendaAtual:
            valorTotal += item_venda.getValor()

        notaFiscal.NotaFiscal(Id=self.qtdId, cliente=cliente, itens=self.listaVendaAtual, valorTotal=valorTotal, data=data)

        self.qtdId += 1
        self.listaNotasFiscas.append(notaFiscal)
        self.listaVendaAtual.clear()
        print(notaFiscal)
        print(f"Notas: {self.listaNotasFiscas}")
        print(f"Venta: {self.listaVendaAtual}")
        main_view.atualizar_lista_venda()
        return True


    def adicionarProduto(self, produto: produtos.Carne, peso: float) -> bool:
        if produto and peso:
            item = vendas.ItemVenda(produto=produto, peso=peso)
            self.listaVendaAtual.append(item)
            print(item)

            return True
        else:
            return False
    

    def getNotasFiscais(self) -> list:
        return self.listaNotasFiscas


    def getVendaAtual(self) -> list:
        return self.listaVendaAtual