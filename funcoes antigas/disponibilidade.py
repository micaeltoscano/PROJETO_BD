from banco import Banco

class Disponibilidade(Banco):
    colunas_permitidas = ['dia', 'hora_inicio', 'hora_fim', 'id_funcionario']

    def cadastrar_disponibilidade(self, dia, hora_inicio, hora_fim, id_funcionario):

        try:
            jacadastrado = self.processar(
                                            """SELECT 1 
                                               FROM disponibilidade 
                                               WHERE funcionario_id = %s AND dia = %s AND hora_inicio = %s AND hora_fim = %s""",
                                               (id_funcionario, dia, hora_inicio, hora_fim), fetch=True)
            if jacadastrado:
                print("Disponibilidade já cadastrada para esse funcionário nesse horário.")
                return
            
            self.processar("INSERT INTO disponibilidade(dia, hora_inicio, hora_fim, id_funcionario) VALUES(%s,%s,%s,%s)", 
                          (dia, hora_inicio, hora_fim, id_funcionario))
                
            print("disponibilidade cadastrada.")

        except Exception as e:
            print(f"Erro ao cadastrar disponibilidade: {e}")
        

    def ler_disponibilidade(self):

        leitura = self.processar("SELECT * FROM disponibilidade ORDER BY id", fetch = True)
        return leitura

    def atualizar_disponibilidade(self, coluna, novo_valor, id):

        if coluna not in self.colunas_permitidas:
            print(f"Não é possível alterar a coluna: {coluna}")
            return

        try:
            alteracao = self.processar(
            f"UPDATE disponibilidade SET {coluna} = %s WHERE id = %s",
            (novo_valor, id))

            if alteracao == 0:
                print("ID da disponibilidad não encontrado, nenhuma disponibilidade atualizada.")
            else:
                print("disponibilidade atualizada com sucesso!")

        except Exception as e:
            print(f"Erro ao atualizar disponibilidade: {e}")

    def deletar_disponibilidade(self, id):

        try:
            deletar = self.processar("DELETE FROM disponibilidade WHERE id = %s", (id,))

            if deletar == 0:
                print("ID da disponibilidad não encontrado, nenhuma disponibilidade deletada.")
            else:
                print("disponibilidade deletada com sucesso!")

        except Exception as e:
            print(f"Erro ao deletar disponibilidade: {e}")