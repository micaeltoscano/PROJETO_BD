from banco import Banco

class Agenda(Banco):
    colunas_permitidas = ['dia', 'horario', 'status', 'id_funcionario']

    def cadastrar_agendamento(self, dia, horario, id_funcionario, status ='agendado'):
        jaagendado = self.processar("SELECT 1 FROM agenda WHERE dia = %s AND horario = %s AND id_funcionario = %s",
            (dia, horario, id_funcionario), 
            fetch=True
        )
        if not jaagendado:
            #VERIFICAR SE O HORARIO ESCOLHIDO ESTA DENTRO DO QUE O FUNCIONARIO PODE ATENDER
            indisponivel = self.processar("SELECT 1 FROM DISPONIBILIDADE WHERE ID_FUNCIONARIO = %s AND %s BETWEEN HORA_INICIO AND HORA_FIM", (id_funcionario, horario), fetch= True)
            if not indisponivel:
            #VERIFICAR A DURAÇÃO DOS SERVICOS AGENDADOS PARA ELE (vou ficar devendo, mas tem que pegar a duração do serviço e ver se o horario ta no intervalo. novidades em breve!)
                self.processar(
                    "INSERT INTO agenda(dia, horario, status, id_funcionario) VALUES (%s, %s, %s, %s)", 
                    (dia, horario, status, id_funcionario)
                )
                print("Agendamento cadastrado com sucesso!")
            else:
                print("Já existe um agendamento nesse horário!")

        else:
            print("Já existe um agendamento nesse horário!")

    def ler_agendamentos(self):
        leitura = self.processar("SELECT * FROM agenda ORDER BY idagenda", fetch = True) 
        return leitura
    
    #PRECISO FAZER UMA IMPLEMENTAÇÃO AQUI PARA SABER SE PODE ALTUALIZAR O AGENDAMENTO PARA UM HORARIO LIVRE
    def atualizar_agendamento(self, coluna, novo_valor, idagenda): 
        if coluna not in self.colunas_permitidas:                       
            print(f"Não é possível alterar a coluna: {coluna}")
            return
    
        alteracao = self.processar(
        f"UPDATE agenda SET {coluna} = %s WHERE idagenda = %s",
        (novo_valor, idagenda)
    )

        if alteracao == 0:
            print("agendamento não encontrado, nenhum agendamento atualizado.")
        else:
            print("agendamento atualizado com sucesso!")

    def deletar_agendamento(self, idagenda):
        deletar = self.processar("DELETE FROM agenda WHERE idagenda = %s", (idagenda,))

        if deletar == 0:
            print("agendamento não encontrado, nenhum agendamento removido.")
        else:
            print("agendamento removido com sucesso!") 