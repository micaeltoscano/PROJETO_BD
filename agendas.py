from crud import Crud

class Agenda(Crud):

    def cadastrar_agenda(self, dia, horario, idfuncionario, nome_servico, status ='agendado'):
         #VERIFICA SE O FUNCIONARIO ESTA DISPONIVEL NO DIA
        disponibilidade_dia = self.processar(
                                                """ SELECT 1 
                                                    FROM disponibilidade 
                                                    WHERE funcionario_id = %s AND %s BETWEEN hora_inicio AND hora_fim""",
                                                    (idfuncionario, horario),
                                                    fetch=True)
        
        if not disponibilidade_dia:
            raise ValueError(f"O funcionário de ID {idfuncionario} não está disponível no dia {dia} no horário {horario}")

        # VERIFICA SE JÁ HÁ UM AGENDAMENTO
        jaagendado = self.processar(
                                    """ SELECT 1 
                                        FROM agenda 
                                        WHERE dia = %s AND horario = %s AND idfuncionario = %s""",
                                    (dia, horario,idfuncionario),
                                    fetch=True
                                )
        if jaagendado:
            raise ValueError(f"O funcionário de ID {idfuncionario} já tem um agendamento no dia {dia} no horário {horario}")

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
                                                    WHERE a.idfuncionario = %s
                                                    AND a.dia = %s
                                                    AND NOT (
                                                            %s + interval '%s minute' <= a.horario
                                                        OR %s >= a.horario + s.duracao * interval '1 minute'
                                                    )""", 
                                                    (idfuncionario, dia, horario, duracao_servico, horario),
                                                    fetch=True)
                                                                                                
        if indisponibilidade_horario:
            raise ValueError(f"horario indisponível, por haver conflito com outro agendamento")
        
        super().cadastro(
                    dia=dia,
                    horario=horario,
                    idfuncionario=idfuncionario,
                    nome_servico=nome_servico,
                    status=status)

    def ler_agenda(self):
        return super().ler()
    
    def atualizar_agenda(self, coluna, novo_valor, id):
        return super().atualizar(coluna, novo_valor, id)
    
    def deletar(self, id):
        return super().deletar(id)
    
    def confirmar_servico(self, id_agenda):
        
        buscar_valor = self.processar(""" SELECT S.VALOR
                                          FROM AGENDA A
                                          INNER JOIN SERVICO S ON A.IDSERVICO = S.IDSERVICO
                                          WHERE A.IDAGENDA = %s """, 
                                          (id_agenda), fetch=True)
        
        self.atualizar_agenda("status", "concluido", id_agenda)




        
