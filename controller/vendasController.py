from model import vendas, produtos, cliente, notaFiscal


class VendasController:
    def __init__(self):
        self.listaNotasFiscas = []
        self.listaVendaAtual = []
        self.qtdId = 0
    

    def emitirNota(self, cliente: cliente.Cliente, itensVenda: list, data:str) -> bool:
        valorTotal = 0

        for produto in itensVenda:
            print(produto)
            valorTotal += produto.getValor()

        notaFiscal.NotaFiscal(id=qtdId, cliente=cliente, itens=itensVenda, valorTotal=valorTotal, data=data)
        self.listaNotasFiscas.append(notaFiscal)
        self.listaVendaAtual.clear()
        print(notaFiscal)
        return True


    def adicionarProduto(self, produto: produtos.Carne, peso: float) -> vendas.ItemVenda:
        if produto and peso:
            item = vendas.ItemVenda(produto=produto, peso=peso)
            self.listaVendaAtual.append(item)
            print(item)

            return item
        else:
            return None
    

    def getNotasFiscais(self) -> list:
        return self.listaNotasFiscas


    def getVendaAtual(self) -> list:
        return self.listaVendaAtual