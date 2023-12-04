from produtos import Carne

class ItemVenda:
    def __init__(self, produto: Carne, peso: float) -> None:
        self.__produto = produto
        self.__peso = peso
    
    
    @property
    def produto(self) -> Carne:
        return self.__produto
    

    @property
    def peso(self) -> float:
        return self.__peso
    

    def getValor(self) -> float:
        return self.__produto.preco * self.__peso
    

    def __str__(self):
        return f"Produto: {self.produto.desc} - Valor: {self.produto.preco} - Qtd: {self.__peso}Kg - Total: {self.getValor()}"