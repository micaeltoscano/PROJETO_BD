from banco import Banco

class Crud(Banco):
    tabela = None
    colunas_permitidas = []
    coluna_id = 'id'

    def cadastro(self, **kwargs):
        try:
            #TRATAMENTO DE STRING PARA PASSAGEM DOS PARAMETROS DENTRO DA FUNCAO:

            #O KWARGS RETORNA UM DICIONARIO {'COLUNA1': 'PARAMETRO1', ... }, ENTÃO USAMOS KEY() PARA PEGAR O NOME DAS COLUNAS E UM ','.JOIN PARA TIRAR OS VALORES DA LISTA
            colunas = ','.join(kwargs.keys()) 

            #PRECISAMOS DOS PLACEHOLDERS %s PARA RECEBER A PASSAGEM DE VALORES, ENTAO MULTIPLICAMOS A %s * QUANTIDADE DE ARGUMENTOS PARA QUE FOSSEM GERADOS PLACEHOLDERS EQUIVALENTES 
            placeholder = ', '.join(['%s'] * len(kwargs))

            #RECEBER OS VALORES DA FUNCAO EM FORMATO DE TUPLA
            valores = tuple(kwargs.values())

            #FUNCAO PARA FAZER CADASTRO:
            self.processar(f"""
                            INSERT INTO {self.tabela} ({colunas}) VALUES ({placeholder})""",
                            valores)
            
            print(f"registro em {self.tabela} cadastrado com sucesso ")
        
        except Exception as e:
            raise ValueError(f"Ocorreu um erro durante o cadastro na tabela {self.tabela}: {e}")
        
    
    def ler(self):
        try:
            leitura = self.processar(f"SELECT * FROM {self.tabela} ORDER BY {self.coluna_id}", fetch = True)
            return leitura
        
        except Exception as e:
            print(f"Ocorreu um erro durante o leitura da tabela {self.tabela}: {e}")
            return []
        
    def atualizar(self, coluna, novo_valor, id):

        if coluna not in self.colunas_permitidas:
            print(f"Não é possível alterar a coluna: {coluna}")
            return

        try:
            alteracao = self.processar(
            f"UPDATE {self.tabela} SET {coluna} = %s WHERE {id} = %s",
            (novo_valor, id))

            if alteracao == 0:
                 print("Registro não encontrado, nenhuma atualização realizada.")
            else:
                print("Registro atualizado com sucesso!")

        except Exception as e:
            print(f"Erro ao atualizar {self.tabela}: {e}")

    def deletar(self, id):

        try:
        
            deletar = self.processar(f"DELETE FROM {self.tabela} WHERE {id} = %s", 
                                    (id,))

            if deletar == 0:
                print("Registro não encontrado, nenhum registro foi removido.")
            else:
                print("Registro foi removido com sucesso!")

        except Exception as e:
            print(f"Erro ao deletar registro da tabela {self.tabela}: {e}")

            

