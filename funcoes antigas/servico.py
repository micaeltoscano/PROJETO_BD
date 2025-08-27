from banco import Banco

class Servico(Banco):

    #COLUNAS QUE PODEM SER ALTERADAS (FUTURAMENTE PODE SER ATUALIZADO PARA UMA FORMA MAIS PROFISSIONAL(?))
    colunas_permitidas = ['nome', 'valor', 'duracao']
    
    def cadastrar_servico(self, nome_servico, valor, nome_categoria, duracao):

        #VERIFICAÇÃO SE A CATEGORIA EXISTE
        categoria_existe = False

        if self.processar(
                            """
                                SELECT 1
                                FROM categoria
                                WHERE nome_categoria = %s
                            """,
                                (nome_categoria,), 
                                fetch=True):

            categoria_existe = True
        
        if not categoria_existe:
            raise ValueError (f"Categoria '{nome_categoria}' não é válida")
        
        #NA TABELA DE SERVICO, NÃO TEMOS O NOME DA CATEGORIA, APENAS O ID, ENTÃO ESSA CONSULTA SERVE PARA PEGAR O ID REFERENTE AO NOME DAQUELA CATEGORIA
        id_categoria = self.processar(
                                    """ SELECT IDCATEGORIA
                                        FROM CATEGORIA
                                        WHERE NOME_CATEGORIA = %s
                                        """,
                                        (nome_categoria,),
                                        fetch=True)[0][0] #ESSE [0][0] É PARA RETORNAR O PRIMEIRO RESULTADO
        
        #INSERÇÃO NA TABELA
        try:
            self.processar(
                            "INSERT INTO servico(NOME_SERVICO, VALOR, ID_CATEGORIA, DURACAO)" \
                            "VALUES(%s,%s,%s,%s)", 
                            (nome_servico, valor, id_categoria, duracao))
            
            print("servico cadastrado com sucesso!")
            
        except Exception as e:

            print(f"Erro ao cadastrar serviço: {e}")
       
    def ler_servico(self):

        leitura = self.processar(
                                """ SELECT * 
                                    FROM servico 
                                    ORDER BY idservico """, 
                                fetch = True)
        
        return leitura
    
    def atualizar_servico(self, coluna, novo_valor, idservico): 
        
        #VERIFICACAO SE AQUELA COLUNA PODE SER ALTERADA
        if coluna not in self.colunas_permitidas:

            print(f"Não é possível alterar a coluna: {coluna}")
            return
        
        #ALTERACAO BASEADA NO ID DO SERVICO
        try:
            alteracao = self.processar(
            f"UPDATE servico SET {coluna} = %s WHERE idservico = %s",
            (novo_valor, idservico)
        )   
            #VERIFICAÇÃO SE O SERVIÇO SOFREU ALTERAÇÃO
            if alteracao == 0:
                print("servico não encontrado, nenhum servico atualizado.")

            else:
                print("servico atualizado com sucesso!")

        except Exception as e:
            print(f"Erro ao atualizar serviço: {e}")

    def deletar_servico(self, idservico):

        try:
        
            deletar = self.processar("DELETE FROM servico WHERE idservico = %s", 
                                    (idservico,))

            if deletar == 0:
                print("servico não encontrado, nenhum servico removido.")

            else:
                print("servico removido com sucesso!") 

        except Exception as e:
            print(f"Erro ao deletar serviço: {e}")