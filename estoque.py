from crud import Crud

class Estoque(Crud):
    
    tabela = 'estoque'
    colunas_permitidas = ['id_produto', 'quantidade_atual', 'quantidade_minima', 'quantidade_maxima']
    coluna_id = 'idestoque'

    def cadastro_estoque(self, id_produto, quantidade_atual, quantidade_minima, quantidade_maxima):
        
        super().cadastro(
            id_produto = id_produto, 
            quantidade_atual = quantidade_atual, 
            quantidade_minima = quantidade_minima, 
            quantidade_maxima = quantidade_maxima
        )
    
    def ler(self):
       return super().ler()
    
    def atualizar_estoque(self, coluna, novo_valor, id):
        return super().atualizar(coluna, novo_valor, id)
    
    def deletar_estoque(self, id):
        return super().deletar(id)