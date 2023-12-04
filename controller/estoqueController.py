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
            # Verifica se já existe um produto com o mesmo código
            if (not codigo) or (not desc) or (not preco):
                raise ValueError("Dados Incompleto")
            if any(produto.getCodigo == codigo for produto in self.estoque):
                raise ValueError("Código de produto já cadastrado")

            # Cria um novo produto e adiciona à lista
            novo_produto = produtos.Carne(codigo, desc, preco)
            self.estoque.append(novo_produto)
            return True
        except Exception as e:
            print(f"Erro ao cadastrar produto: {e}.")
            return False


    def buscarProduto(self, codigo: int) -> produtos.Carne:
        try:
            # Busca o produto pelo código
            produto = next((produto for produto in self.estoque if produto.getCodigo == codigo), None)

            if produto is not None:
                return produto
            else:
                raise ValueError("Produto não encontrado")
        except Exception as e:
            print(f"Erro ao buscar produto: {e}")
            return None


    def deletarProduto(self, codigo: int) -> bool:
        try:
            # Encontra o índice do produto com o código fornecido
            indice_produto = next((i for i, produto in enumerate(self.estoque) if produto.getCodigo == codigo), None)

            # Se o produto foi encontrado, remove-o da lista
            if indice_produto is not None:
                del self.estoque[indice_produto]
                return True
            else:
                raise ValueError("Produto não encontrado")
        except Exception as e:
            print(f"Erro ao deletar produto: {e}")
            return False
    

    def alterarProduto(codigo: int, voa_descricao, novo_preco) -> bool:
        try:
            # Busca o produto pelo código
            produto = self.buscarProduto(codigo)

            if produto is not None:
                # Atualiza a descrição e o preço do produto
                produto.setDesc(nova_descricao)
                produto.setPreco(novo_preco)
                return True
            else:
                raise ValueError("Produto não encontrado para alteração")
        except Exception as e:
            print(f"Erro ao alterar produto: {e}")
            return False


    def getEstoque(self) -> list:
        return self.estoque