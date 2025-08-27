from banco import Banco

class Funcionarios(Banco):
    colunas_permitidas = ['nome', 'email', 'endereco', 'numero_celular', 'salario', 'especialidade', 'comissao']

    def cadastrar_funcionario(self, nome, email, cpf, endereco, numero_celular, salario, especialidade, comissao):
       
        try:
            self.processar("INSERT INTO FUNCIONARIO(nome, email, cpf, endereco, numero_celular, salario, especialidade, comissao) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)", 
                            (nome,email, cpf, endereco, numero_celular, salario, especialidade, comissao))
                
            print("Funcionario cadastrado com sucesso!")

        except Exception as e:
            print(f"Erro ao cadastrar funcionário: {e}")
           

    def ler_funcionarios(self):
        leitura = self.processar("SELECT * FROM funcionario ORDER BY idfuncionario", fetch = True)
        return leitura
    
    def atualizar_funcionario(self, coluna, novo_valor, cpf):

        if coluna not in self.colunas_permitidas:
            print(f"Não é possível alterar a coluna: {coluna}")
            return

        try:
            alteracao = self.processar(
            f"UPDATE funcionario SET {coluna} = %s WHERE cpf = %s",
            (novo_valor, cpf))

            if alteracao == 0:
                print("CPF não encontrado, nenhum funcionario atualizado.")

            else:
                print("funcionario atualizado com sucesso!")

        except Exception as e:
             print(f"Erro ao atualizar funcionário: {e}")
            
    def deletar_funcionario(self, cpf):

        try:
            deletar = self.processar("DELETE FROM funcionario WHERE cpf = %s", (cpf,))

            if deletar == 0:
                print("CPF não encontrado, nenhum funcionario removido.")
            else:
                print("funcionario removido com sucesso!") 

        except Exception as e:
             print(f"Erro ao deletar funcionário: {e}")