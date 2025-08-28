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
    
    def ler_todos_produtos(self):
        return super().ler_todos()
    
    def pesquisar_nome_produto(self, nome):
        return super().pesquisar_nome(nome)
    
    def ler_um_produto(self, id):
        return super().listar_um(id)
    
    def atualizar_produto(self, coluna, novo_valor, id):
        return super().atualizar(coluna, novo_valor, id)
    
    def deletar_produto(self, id):
        return super().deletar(id)
    

