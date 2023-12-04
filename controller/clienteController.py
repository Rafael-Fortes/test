from model import cliente


class ClienteController:
    def __init__(self):
        self.clientes = []
        self.clientes.append(cliente.Cliente('Rafael', '1234567890', 'Rua CDB, 1000', 'rafael@email.com'))
        self.clientes.append(cliente.Cliente('Joao', '0987654321', 'Rua THC, 1073', 'joao@email.com'))
        self.clientes.append(cliente.Cliente('Mike', '1112223334', 'Rua do Mike, 107', 'mike@email.com'))


    def cadastrarCliente(self, nome: str, cpf: str, endereco: str, email: str) -> bool:
        try:
            # Verifica se já existe um cliente com o mesmo CPF
            if (not nome) or (not cpf) or (not endereco) or (not email):
                raise ValueError("Dados incompleto")
            if any(cliente.cpf == cpf for cliente in self.clientes):
                raise ValueError("CPF já cadastrado")

            # Cria um novo cliente e adiciona à lista
            novo_cliente = cliente.Cliente(nome, cpf, endereco, email)
            self.clientes.append(novo_cliente)
            return True

        except Exception as e:
            print(f"Erro ao cadastrar cliente: {e}.")
            return False

    def buscarCliente(self, cpf: str) -> cliente.Cliente:
        try:
            # Encontra o índice do cliente com o CPF fornecido
            for cliente in self.clientes:
                if cliente.getCpf == cpf:
                    return cliente
                
            raise ValueError("Cliente não encontrado")
        except Exception as e:
            print(f"Erro ao deletar cliente: {e}")
            return None


    def deletarCliente(self, cpf: str) -> bool:
        try:
            # Encontra o índice do cliente com o CPF fornecido
            for cliente in self.clientes:
                if cliente.getCpf == cpf:
                    self.clientes.remove(cliente)
                    return True
                
            raise ValueError("Cliente não encontrado")
        except Exception as e:
            print(f"Erro ao deletar cliente: {e}")
            return False


    def getClientes(self) -> list:
        return self.clientes