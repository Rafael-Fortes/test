from model import produtos


class EstoqueController:
    def __init__(self):
        self.estoque = []
        self.estoque.append(produtos.Carne(123, 'Carne', 123))
        self.estoque.append(produtos.Carne(124, 'Carne', 123))
        self.estoque.append(produtos.Carne(125, 'Carne', 123))
        self.estoque.append(produtos.Carne(126, 'Carne', 123))
    

    def cadastrarProduto(self, codigo: int, desc: str, preco: float) -> bool:
        try:
            if (not codigo) or (not desc) or (not preco):
                raise ValueError("Dados Incompleto")

            for produto in self.estoque:
                if produto.getCodigo == codigo:
                    raise ValueError("Código de produto já cadastrado")

            novo_produto = produtos.Carne(codigo, desc, preco)
            self.estoque.append(novo_produto)
            
            return True
        except Exception as e:
            print(f"Erro ao cadastrar produto: {e}.")
            return False


    def buscarProduto(self, codigo: int) -> produtos.Carne:
        try:
            for produto in self.estoque:
                if produto.codigo == codigo:
                    return produto

            raise ValueError("Produto não encontrado")
        except Exception as e:
            print(f"Erro ao buscar produto: {e}")
            return None


    def deletarProduto(self, codigo: int) -> bool:
        try:
            produto = self.buscarProduto(codigo)

            if produto is not None:
                self.estoque.remove(produto)
                return True
            else:
                raise ValueError("Produto não encontrado")
        except Exception as e:
            print(f"Erro ao deletar produto: {e}")
            return False
    

    def alterarProduto(self, codigo: int, nova_descricao: str, novo_preco: float) -> bool:
        try:
            produto = self.buscarProduto(codigo)

            if produto is not None:
                produto.setDesc = nova_descricao
                produto.setPreco = novo_preco
                return True
            else:
                raise ValueError("Produto não encontrado para alteração")
        except Exception as e:
            print(f"Erro ao alterar produto: {e}")
            return False


    def getEstoque(self) -> list:
        return self.estoque
