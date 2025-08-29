from crud import Crud
from pagamentos import Pagamento
from estoque import Estoque

class Agenda(Crud):
    
    tabela = 'agenda'
    colunas_permitidas = ['id_cliente', 'id_funcionario', 'id_servico', 'dia', 'horario', 'status'] 
    coluna_id = 'idagenda'

    def cadastrar_agenda(self, dia, horario, id_funcionario, id_servico, id_cliente, status='agendado'):

        # Verifica se o funcionário está disponível no dia
        disponibilidade_dia = self.processar(
                                            """ SELECT 1 
                                                FROM disponibilidade 
                                                WHERE id_funcionario = %s AND %s BETWEEN hora_inicio AND hora_fim""",
                                            (id_funcionario, horario),
                                            fetch=True
                                        )

        if not disponibilidade_dia:
            raise ValueError(f"O funcionário de ID {id_funcionario} não está disponível no dia {dia} no horário {horario}")

        # Verifica se já há um agendamento
        jaagendado = self.processar(
                                    """ SELECT 1 
                                        FROM agenda 
                                        WHERE dia = %s AND horario = %s AND id_funcionario = %s""",
                                    (dia, horario, id_funcionario),
                                    fetch=True
                                )
        if jaagendado:
            raise ValueError(f"O funcionário de ID {id_funcionario} já tem um agendamento no dia {dia} no horário {horario}")

        # Pega a duração do serviço pelo ID
        resultado = self.processar(
                                    """ SELECT DURACAO
                                        FROM SERVICO
                                        WHERE IDSERVICO = %s """,
                                    (id_servico,), fetch=True
                                )

        if not resultado:
            raise ValueError(f"Serviço de ID {id_servico} não encontrado.")

        duracao_servico = resultado[0][0]

        # Verifica conflitos de horário com outros agendamentos
        indisponibilidade_horario = self.processar(
                                                    """ SELECT 1
                                                        FROM agenda a
                                                        JOIN servico s ON a.id_servico = s.idservico
                                                        WHERE a.id_funcionario = %s
                                                        AND a.dia = %s
                                                        AND NOT (
                                                            %s + interval '%s minute' <= a.horario
                                                            OR %s >= a.horario + s.duracao * interval '1 minute'
                                                        )""",
                                                    (id_funcionario, dia, horario, duracao_servico, horario),
                                                    fetch=True
                                                )

        if indisponibilidade_horario:
            raise ValueError("Horário indisponível, por haver conflito com outro agendamento.")

        # Cadastro do agendamento
        super().cadastro(
        dia=dia,
        horario=horario,
        id_funcionario=id_funcionario,
        id_servico=id_servico,
        id_cliente=id_cliente,
        status=status
    )

    def ler_toda_agenda(self):
        return super().ler_todos()
    
    def pesquisar_id(self, nome):
        return super().pesquisar_nome(nome)
    
    def ler_um_agenda(self, id):
        return super().listar_um(id)

    def atualizar_agenda(self, coluna, novo_valor, id):
        return super().atualizar(coluna, novo_valor, id)

    def deletar(self, id):
        return super().deletar(id)

    def confirmar_servico(self, id_agenda, metodo_pagamento, idcliente):
        try:     
            self.atualizar_agenda("status", "concluido", id_agenda)

            pagamento = Pagamento()
            pagamento.registrar_pagamento_servico(id_agenda, metodo_pagamento, idcliente)

            #CONSULTA PARA BUSCAR O ID DO SERVIÇO ASSOCIADO AO AGENDAMENTO
            consulta = self.processar(
                                        """ SELECT ID_SERVICO
                                            FROM AGENDA
                                            WHERE IDAGENDA = %s """,
                                            (id_agenda,), fetch=True)
            if not consulta:
                raise ValueError(f"Serviço não encontrado para o agendamento ID {id_agenda}.")
            
            id_servico = consulta[0][0] 

            estoque = Estoque()
            estoque.atualizar_quantidade(origem='servico', id_origem=id_servico) 

            print(f"Serviço {id_agenda} confirmado com sucesso!")

        except Exception as e:
            raise ValueError(f"Erro ao confirmar serviço e registrar pagamento: {e}")

            


