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
    
    def atualizar_quantidade(self, origem, id_origem): 
        
        #DICIONARIO COM AS OPERAÇÕES POSSÍVEIS PARA ATUALIZAÇÃO DO ESTOQUE
        config = {
            'servico': {
                'tabela_origem': 'utiliza', 
                'coluna_origem': 'id_servico',
                'operacao': -1  
                },
            'venda': {                                  #A VENDA É A COMPRA DE PRODUTOS PELO CLIENTE
                'tabela_origem': 'itens_compra',
                'coluna_origem': 'id_compra',
                'operacao': -1   
                },
            'compra': {                                 #A COMPRA É A COMPRA DE PRODUTOS PELA BARBEARIA
                'tabela_origem': 'itens_compra',
                'coluna_origem': 'id_compra',
                'operacao': 1    
                }
            }

        if origem not in config:
            raise ValueError("Origem inválida. Use 'servico', 'venda' ou 'compra'.")
        
        tabela_origem = config[origem]['tabela_origem'] #RETORNA A TABELA DE ONDE VAI BUSCAR OS DADOS
        coluna_origem = config[origem]['coluna_origem'] #RETORNA A COLUNA DE ONDE VAI BUSCAR OS DADOS
        operacao = config[origem]['operacao']           #RETORNA A OPERAÇÃO A SER REALIZADA 


        #FAZ UMA CONSULTA NAS TABELAS DE ORIGEM PARA PEGAR A QUANTIDADE E O ID DO PRODUTO
        pesquisa = self.processar(f"""SELECT QUANTIDADE, ID_PRODUTO 
                                     FROM {tabela_origem}
                                     WHERE {coluna_origem} = %s""", (id_origem,), fetch=True)
        
                
        if not pesquisa:
            raise ValueError("Serviço não encontrado ou não utiliza produtos.")

        #ATUALIZA O ESTOQUE DE CADA PRODUTO UTILIZADO NO SERVIÇO
        for quantidade, id_produto in pesquisa: #É NECESSÁRIO O FOR, POIS UMA OPERACAO PODE USAR MAIS DE UM PRODUTO

            estoque = self.processar(f"SELECT quantidade_atual FROM {self.tabela} WHERE {self.coluna_id} = %s",
                                            (id_produto,),fetch=True)
            if not estoque:
                raise ValueError("Produto não encontrado no estoque.")
                
            estoque_atual = estoque[0][0] + (quantidade * operacao)
                
            self.atualizar_estoque('quantidade_atual', estoque_atual, id_produto)




#VERSAO ANTIGA DA FUNÇÃO DE ATUALIZAR QUANTIDADE, COM A LOGICA DE IF (MUITO RUIM):

#def atualizar_quantidade(self, id_servico = None, id_compra = None)
    #     try:
    #         if id_servico:
    #             pesquisa = self.processar("""SELECT QUANTIDADE, ID_PRODUTO 
    #                                         FROM UTILIZA
    #                                         WHERE ID_SERVICO = %s""", (id_servico), fetch=True)
                
    #             if not pesquisa:
    #                 raise ValueError("Serviço não encontrado ou não utiliza produtos.")
                
    #             quantidade = pesquisa[0][0]
    #             id_produto = pesquisa[0][1]

    #             estoque = self.processar(f"SELECT quantidade_atual FROM {self.tabela} WHERE {self.coluna_id} = %s",
    #                                             (id_produto,),fetch=True)
    #             if not estoque_atual:
    #                 raise ValueError("Produto não encontrado no estoque.")
                
    #             estoque_atual = estoque[0][0] - quantidade
                
    #             self.atualizar_estoque('quantidade_atual', estoque_atual, id_produto)

    #         elif id_compra:
    #             pesquisa = self.processar("""SELECT QUANTIDADE, ID_PRODUTO 
    #                                         FROM ITENS_COMPRA
    #                                         WHERE ID_COMPRA = %s""", (id_compra,), fetch=True)
                
    #             if not pesquisa:
    #                 raise ValueError("Compra não encontrada ou não possui itens.")
                
    #             for item in pesquisa:
    #                 quantidade = item[0]
    #                 id_produto = item[1]

    #                 estoque = self.processar(f"SELECT quantidade_atual FROM {self.tabela} WHERE {self.coluna_id} = %s",
    #                                                 (id_produto,),fetch=True)
    #                 if not estoque:
    #                     raise ValueError(f"Produto com ID {id_produto} não encontrado no estoque.")
                    
    #                 estoque_atual = estoque[0][0] + quantidade
                    
    #                 self.atualizar_estoque('quantidade_atual', estoque_atual, id_produto)
            
    #     except Exception as e:
    #         raise ValueError(f"Erro ao atualizar estoque: {e}")
            
