import cliente, produtos


class NotaFiscal:
    def __init__(self, id: int, cliente: cliente.Cliente, itens: list, valorTotal: float, data: str) -> None:
        self.__id = id
        self.__cliente = cliente
        self.__itens = itens
        self.__valorTotal = valorTotal
        self.__data = data
    

    @property
    def id(self) -> int:
        return self.__id
    
    
    @property
    def cliente(self) -> cliente.Cliente:
        return self.__cliente
    

    @property
    def itens(self) -> list:
        return self.__itens
    

    @property
    def valorTotal(self) -> float:
        return self.__valorTotal
    

    @property
    def data(self) -> str:
        return self.__data


    def __str__(self):
        return f"Id: {self.__id} - Cliente: {self.__cliente.nome} - Valor Total: {self.__valorTotal}"