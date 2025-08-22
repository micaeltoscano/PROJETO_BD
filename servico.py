from banco import Banco

class Servico(Banco):
    colunas_permitidas = ['nome', 'valor', 'categoria', 'duracao']

    def cadastrar_servico(self, idservico, nome, valor, categoria, duracao):
        jacadastrado = self.processar("SELECT 1 FROM servico WHERE idservico = %s", (idservico,), fetch = True)
        if not jacadastrado:
            self.processar("INSERT INTO servico(nome, valor, categoria, duracao) VALUES(%%s,%s,%s,%s)", 
                    (nome, valor, categoria, duracao))
            
            print("servico cadastrado com sucesso!")
        else:
            print("servico já cadastrado!")

    def ler_servico(self):
        leitura = self.processar("SELECT * FROM servico ORDER BY idservico", fetch = True)
        return leitura
    
    def atualizar_servico(self, coluna, novo_valor, idservico): 
        if coluna not in self.colunas_permitidas:
            print(f"Não é possível alterar a coluna: {coluna}")
            return
    
        alteracao = self.processar(
        f"UPDATE servico SET {coluna} = %s WHERE idservico = %s",
        (novo_valor, idservico)
    )

        if alteracao == 0:
            print("serviconão encontrado, nenhum servico atualizado.")
        else:
            print("servico atualizado com sucesso!")

    def deletar_servico(self, idservico):
        deletar = self.processar("DELETE FROM servico WHERE idservico = %s", (idservico,))

        if deletar == 0:
            print("servico não encontrado, nenhum servico removido.")
        else:
            print("servico removido com sucesso!") 