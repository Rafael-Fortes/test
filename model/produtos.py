class Carne:
    def __init__(self, codigo: int, desc: str, preco: float) -> None:
        self.__codigo = codigo
        self.__desc = desc
        self.__preco = preco
    

    @property
    def codigo(self) -> int:
        return self.__codigo
    
    
    @property
    def desc(self) -> str:
        return self.__desc
    

    @property
    def preco(self) -> float:
        return self.__preco

    
    @codigo.getter
    def getCodigo(self) -> int:
        return self.__codigo
    

    @desc.getter
    def getDesc(self) -> str:
        return self.__desc

    
    @preco.getter
    def getPreco(self) -> float:
        return self.__preco
    

    @codigo.setter
    def setCodigo(self, codigo: int) -> None:
        self.__codigo = codigo
    

    @desc.setter
    def setDesc(self, desc: str) -> None:
        self.__desc = desc
    

    @preco.setter
    def setPreco(self, preco: float) -> None:
        self.__preco = preco


    def __str__(self):
        return f'Código: {self.__codigo} - Descrição: {self.__desc} - Preço: {self.__preco}'