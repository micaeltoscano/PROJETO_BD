from crud import Crud

class Estoque(Crud):
    
    tabela = 'estoque'
    colunas_permitidas = ['id_produto', 'quantidade_atual', 'quantidade_minima', 'ultima_atualizacao']
    coluna_id = 'idestoque'

    def cadastro_estoque(self, id_produto, quantidade_atual, quantidade_minima):
        
        super().cadastro(
            id_produto = id_produto, 
            quantidade_atual = quantidade_atual, 
            quantidade_minima = quantidade_minima, 
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
            
            #LOCALIZANDO O ID DO ESTOQUE PARA O PRODUTO
            estoque_info = self.processar(f"""SELECT {self.coluna_id} FROM {self.tabela} 
                                              WHERE id_produto = %s""", 
                                             (id_produto,), fetch=True)
        
            if not estoque_info:
                raise ValueError(f"Produto ID {id_produto} não encontrado no estoque.")
            
            #LOCALIZANDO O ID DO ESTOQUE PARA O PRODUTO
            id_estoque = estoque_info[0][0]  
            
            quantidade_atual_info = self.processar(f"""SELECT quantidade_atual FROM {self.tabela} 
                                                    WHERE {self.coluna_id} = %s""",
                                                (id_estoque,), fetch=True)
            
            if not quantidade_atual_info:
                raise ValueError(f"Estoque ID {id_estoque} não encontrado.")
            
            estoque_atual = quantidade_atual_info[0][0] + (quantidade * operacao)
            
            self.atualizar_estoque('quantidade_atual', estoque_atual, id_estoque)
