import cliente, notaFiscal, produtos, vendas


class Sistema:
    def __init__(self) -> None:
        self.__listaProdutos = []
        self.__listaClientes = []
        self.__listaNotasFiscais = []

    
    @property
    def listaProdutos(self) -> list:
        return self.__listaProdutos
    

    @property
    def listaClientes(self) -> list:
        return self.__listaClientes

    
    @property
    def listaNotasFiscais(self) -> list:
        return self.__listaNotasFiscais
    

    @listaProdutos.getter
    def getListaProdutos(self):
        for produto in self.__listaProdutos:
            print(produto)
    

    @listaClientes.getter
    def getListaClientes(self):
        for cliente in self.__listaClientes:
            print(cliente)
    

    @listaNotasFiscais.getter
    def getNotasFiscais(self):
        for nota in self.__listaNotasFiscais:
            print(nota)
    

    def cadastrarProduto(self, produto: produtos.Carne) -> None:
        self.__listaProdutos.append(produto)

    
    def alterarProduto(self, codigo: int, novoProduto: produtos.Carne) -> None:
        for produto in self.__listaProdutos:
            if produto.codigo == codigo:
                produto.setCodigo = novoProduto.codigo
                produto.setDesc = novoProduto.desc
                produto.setPreco = novoProduto.preco
    

    def removerProduto(self, codigo: int):
        for i, produto in enumerate(self.__listaProdutos):
            if produto.codigo == codigo:
                self.__listaProdutos.pop(i)
                break
    

    def getProduto(self, codigo: int) -> produtos.Carne:
        for produto in self.__listaProdutos:
            if produto.codigo == codigo:
                return produto


    def cadastrarCliente(self, cliente: cliente.Cliente) -> None:
        self.__listaClientes.append(cliente)
    

    def consultarCliente(self, cpf: str) -> cliente.Cliente:
        for cliente in self.__listaClientes:
            if cliente.cpf == cpf:
                return cliente
    

    def criarVenda(self, cliente: cliente.Cliente, itensVenda: list) -> None:
        valorTotal = 0

        print(cliente)
        print(f'*' * 30)
        for produto in itensVenda:
            print(produto)
            valorTotal += produto.getValor()
        print(f'*' * 30)
        print(f'Valor total da compra: {valorTotal}')
        

if __name__ == "__main__":
    sis = Sistema()

    # Criando um novo produto
    sis.cadastrarProduto(produto=produtos.Carne(101, 'Patinho', 10))
    sis.cadastrarProduto(produto=produtos.Carne(102, 'Picanha', 20))
    sis.cadastrarProduto(produto=produtos.Carne(103, 'Asinha', 5))
    sis.getListaProdutos
    print(f'\n{"-" * 30}\n')

    # Removendo produto
    sis.removerProduto(codigo=103)
    sis.getListaProdutos
    print(f'\n{"-" * 30}\n')

    # Alterando produto
    sis.alterarProduto(codigo=101, novoProduto=produtos.Carne(101, 'Patinho Bovino', 40.90))
    sis.alterarProduto(codigo=102, novoProduto=produtos.Carne(102, 'Picanha', 57.99))
    sis.getListaProdutos
    print(f'\n{"-" * 30}\n')

    # Cadastro de clientes
    sis.cadastrarCliente(cliente=cliente.Cliente('Rafael', '1234567890', 'Rua CDB, 1000', 'rafael@email.com'))
    sis.cadastrarCliente(cliente=cliente.Cliente('Joao', '0987654321', 'Rua THC, 1073', 'joao@email.com'))
    sis.cadastrarCliente(cliente=cliente.Cliente('Mike', '1112223334', 'Rua do Mike, 107', 'mike@email.com'))
    sis.getListaClientes
    print(f'\n{"-" * 30}\n')

    print(sis.consultarCliente(cpf='0987654321'))
    print(sis.consultarCliente(cpf='1234567890'))
    print(f'\n{"-" * 30}\n')


    # Criando umva venda
    listaVenda = []
    listaVenda.append(vendas.ItemVenda(sis.getProduto(codigo=101), peso=1.3))
    listaVenda.append(vendas.ItemVenda(sis.getProduto(codigo=102), peso=0.5))
    sis.criarVenda(
        cliente=sis.consultarCliente(cpf='1234567890'),
        itensVenda=listaVenda
    )
