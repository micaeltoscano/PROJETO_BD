from crud import Crud

class Produto(Crud):

    tabela = 'produto'
    colunas_permitidas = ['valor', 'nome', 'tipo']
    coluna_id = 'idproduto'
    
    def cadastro_produto(self, valor, nome, tipo):
        super().cadastro(
            valor = valor, 
            nome = nome, 
            tipo = tipo
                         )
    
    def ler(self):
        return super().ler()
    
    def atualizar_produto(self, coluna, novo_valor, id):
        return super().atualizar(coluna, novo_valor, id)
    
    def deletar_produto(self, id):
        return super().deletar(id)