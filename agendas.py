from crud import Crud

class Agenda(Crud):
    
    tabela = 'agenda'
    colunas_permitidas = ['dia', 'horario', 'idfuncionario', 'idservico', 'status'] 
    coluna_id = 'idagenda'

    def cadastrar_agenda(self, dia, horario, idfuncionario, idservico, idcliente, status='agendado'):
        # Verifica se o funcionário está disponível no dia
        disponibilidade_dia = self.processar(
            """ SELECT 1 
                FROM disponibilidade 
                WHERE funcionario_id = %s AND %s BETWEEN hora_inicio AND hora_fim""",
            (idfuncionario, horario),
            fetch=True
        )

        if not disponibilidade_dia:
            raise ValueError(f"O funcionário de ID {idfuncionario} não está disponível no dia {dia} no horário {horario}")

        # Verifica se já há um agendamento
        jaagendado = self.processar(
            """ SELECT 1 
                FROM agenda 
                WHERE dia = %s AND horario = %s AND idfuncionario = %s""",
            (dia, horario, idfuncionario),
            fetch=True
        )
        if jaagendado:
            raise ValueError(f"O funcionário de ID {idfuncionario} já tem um agendamento no dia {dia} no horário {horario}")

        # Pega a duração do serviço pelo ID
        resultado = self.processar(
            """ SELECT DURACAO
                FROM SERVICO
                WHERE IDSERVICO = %s """,
            (idservico,), fetch=True
        )

        if not resultado:
            raise ValueError(f"Serviço de ID {idservico} não encontrado.")

        duracao_servico = resultado[0][0]

        # Verifica conflitos de horário com outros agendamentos
        indisponibilidade_horario = self.processar(
            """ SELECT 1
                FROM agenda a
                JOIN servico s ON a.idservico = s.idservico
                WHERE a.idfuncionario = %s
                AND a.dia = %s
                AND NOT (
                    %s + interval '%s minute' <= a.horario
                    OR %s >= a.horario + s.duracao * interval '1 minute'
                )""",
            (idfuncionario, dia, horario, duracao_servico, horario),
            fetch=True
        )

        if indisponibilidade_horario:
            raise ValueError("Horário indisponível, por haver conflito com outro agendamento.")

        # Cadastro do agendamento
        super().cadastro(
        dia=dia,
        horario=horario,
        idfuncionario=idfuncionario,
        idservico=idservico,
        idcliente=idcliente,
        status=status
    )

    def ler_agenda(self):
        registros = super().ler()
        colunas = ['idagenda', 'idcliente', 'idfuncionario', 'idservico', 'dia', 'horario', 'status']
        return [dict(zip(colunas, r)) for r in registros]

    def atualizar_agenda(self, coluna, novo_valor, id):
        return super().atualizar(coluna, novo_valor, id)

    def deletar(self, id):
        return super().deletar(id)

    def confirmar_servico(self, id_agenda):
        buscar_valor = self.processar(
            """ SELECT S.VALOR
                FROM AGENDA A
                INNER JOIN SERVICO S ON A.IDSERVICO = S.IDSERVICO
                WHERE A.IDAGENDA = %s """,
            (id_agenda,), fetch=True
        )

        self.atualizar_agenda("status", "concluido", id_agenda)
