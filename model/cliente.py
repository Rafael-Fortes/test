class Cliente:
    def __init__(self, nome: str, cpf: str, endereco: str, email: str) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__email = email
    

    @property
    def nome(self) -> str:
        return self.__nome
    

    @property
    def cpf(self) -> str:
        return self.__cpf
    

    @property
    def endereco(self) -> str:
        return self.__endereco
    

    @property
    def email(self) -> str:
        return self.__endereco
    

    @nome.getter
    def getNome(self) -> str:
        return self.__nome
    

    @cpf.getter
    def getCpf(self) -> str:
        return self.__cpf
    

    @endereco.getter
    def getEndereco(self) -> str:
        return self.__endereco

    
    @email.getter
    def getEmail(self) -> str:
        return self.__email
    
    
    def __str__(self):
        return f'Nome: {self.__nome} - CPF: {self.__cpf} - Endereco: {self.__endereco} - Email: {self.email}'
