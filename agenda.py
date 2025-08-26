from banco import Banco

class Agenda(Banco):

    #COLUNAS QUE PERMITEM ALTERAÇÃO
    colunas_permitidas = ['dia', 'horario', 'status', 'id_funcionario']
    #LEMBRETE: SO PODE CADASTRAR CLIENTE QUE TEM CADASTRO! FAZER VERIFICACAO!
    def cadastrar_agendamento(self, dia, horario, id_funcionario, nome_servico, status ='agendado'):

        #VERIFICA SE O FUNCIONARIO ESTA DISPONIVEL NO DIA
        disponibilidade_dia = self.processar(
                                                """ SELECT 1 
                                                    FROM disponibilidade 
                                                    WHERE id_funcionario = %s AND %s BETWEEN hora_inicio AND hora_fim""",
                                                    (id_funcionario, horario),
                                                    fetch=True)
        
        if not disponibilidade_dia:
            raise ValueError(f"O funcionário de ID {id_funcionario} não está disponível no dia {dia} no horário {horario}")

        # VERIFICA SE JÁ HÁ UM AGENDAMENTO
        jaagendado = self.processar(
                                    """ SELECT 1 
                                        FROM agenda 
                                        WHERE dia = %s AND horario = %s AND id_funcionario = %s""",
                                    (dia, horario, id_funcionario),
                                    fetch=True
                                )
        if jaagendado:
            raise ValueError(f"O funcionário de ID {id_funcionario} já tem um agendamento no dia {dia} no horário {horario}")

        #VALIDAÇÃO SE O FUNCIONÁRIO ESTÁ LIVRE NAQUELE HORÁRIO

        duracao_servico = self.processar(
                                        """ SELECT DURACAO
                                            FROM SERVICO
                                            WHERE NOME_SERVICO = %s """,
                                            (nome_servico,), fetch= True) [0][0]
        
        indisponibilidade_horario = self.processar(
                                                 """SELECT 1
                                                    FROM agenda a
                                                    JOIN servico s ON a.nome_servico = s.nome_servico
                                                    WHERE a.id_funcionario = %s
                                                    AND a.dia = %s
                                                    AND NOT (
                                                            %s + interval '%s minute' <= a.horario
                                                        OR %s >= a.horario + s.duracao * interval '1 minute'
                                                    )""", 
                                                    (id_funcionario, dia, horario, duracao_servico, horario),
                                                    fetch=True)
                                                                                                
        if indisponibilidade_horario:
            raise ValueError(f"horario indisponível, por haver conflito com outro agendamento")
        
        try:
            self.processar(
                            "INSERT INTO agenda(dia, horario, status, id_funcionario, nome_servico) "
                            "VALUES (%s, %s, %s, %s, %s)", 
                            (dia, horario, status, id_funcionario, nome_servico))
            print("Agendamento cadastrado com sucesso!")

        except Exception as e:
            print(f"Eerro ao cadastrar agendamento: {e}")
        
    def ler_agendamentos(self):

        leitura = self.processar("SELECT * FROM agenda ORDER BY idagenda", fetch = True) 
        return leitura
    
    #PRECISO FAZER UMA IMPLEMENTAÇÃO AQUI PARA SABER SE PODE ALTUALIZAR O AGENDAMENTO PARA UM HORARIO LIVRE
    def atualizar_agendamento(self, coluna, novo_valor, idagenda): 

        if coluna not in self.colunas_permitidas:                       
            print(f"Não é possível alterar a coluna: {coluna}")
            return

        try:
            alteracao = self.processar(
            f"UPDATE agenda SET {coluna} = %s WHERE idagenda = %s",
            (novo_valor, idagenda))

            if alteracao == 0:
                print("agendamento não encontrado, nenhum agendamento atualizado.")
            else:
                print("agendamento atualizado com sucesso!")

        except Exception as e:
            print(f"erro ao atualizar agendamento: {e}")
            

    def deletar_agendamento(self, idagenda):
        try:
            deletar = self.processar("DELETE FROM agenda WHERE idagenda = %s", (idagenda,))

            if deletar == 0:
                print("agendamento não encontrado, nenhum agendamento removido.")
            else:
                print("agendamento removido com sucesso!") 

        except Exception as e:
            print(f"erro ao deletar agendamento: {e}")