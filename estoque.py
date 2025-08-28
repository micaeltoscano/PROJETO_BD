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
    
    def ler_todo_estoque(self):
       return super().ler_todos()
    
    def pesquisar_nome_estoque(self, nome):
        return super().pesquisar_nome(nome)
    
    def ler_um_estoque(self, id):
        return super().listar_um(id)
    
    def atualizar_estoque(self, coluna, novo_valor, id):
        return super().atualizar(coluna, novo_valor, id)
    
    def deletar_estoque(self, id):
        return super().deletar(id)
    
    def atualizar_quantidade(self, id_servico):
        try:
            pesquisa = self.processar("""SELECT QUANTIDADE, ID_PRODUTO 
                                        FROM UTILIZA
                                        WHERE ID_SERVICO = %s""", (id_servico), fetch=True)
            
            if not pesquisa:
                raise ValueError("Serviço não encontrado ou não utiliza produtos.")
            
            quantidade = pesquisa[0][0]
            id_produto = pesquisa[0][1]

            estoque = self.processar(f"SELECT quantidade_atual FROM {self.tabela} WHERE {self.coluna_id} = %s",
                                            (id_produto,),fetch=True)
            if not estoque_atual:
                raise ValueError("Produto não encontrado no estoque.")
            
            estoque_atual = estoque[0][0] - quantidade
            
            self.atualizar_estoque('quantidade_atual', estoque_atual, id_produto)
            
        except Exception as e:
            raise ValueError(f"Erro ao atualizar estoque: {e}")