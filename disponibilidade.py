from banco import Banco

class Disponibilidade(Banco):
    colunas_permitidas = ['dia', 'hora_inicio', 'hora_fim', 'id_funcionario']

    def cadastrar_disponibilidade(self, dia, hora_inicio, hora_fim, id_funcionario):
        jacadastrado = self.processar("SELECT 1 FROM disponibilidade WHERE id_funcionario= %s", (id_funcionario,), fetch = True)
        if not jacadastrado:
            self.processar("INSERT INTO disponibilidade(dia, hora_inicio, hora_fim, id_funcionario) VALUES(%s,%s,%s,%s)", 
                    (dia, hora_inicio, hora_fim, id_funcionario))
            
            print("Funcionario cadastrado com sucesso!")
        else:
            print("Funcionario já cadastrado no horário!")

#FALTA IMPLEMENTAR O RESTO AQUI