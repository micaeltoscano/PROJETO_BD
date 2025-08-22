from banco import Banco

class Clientes(Banco):
    colunas_permitidas = ['nome', 'email', 'endereco', 'numero_celular']  

    def cadastrar_cliente(self, nome, email, cpf, endereco, numero_celular):
        jacadastrado = self.processar("SELECT 1 FROM CLIENTE WHERE CPF = %s", (cpf,), fetch = True)
        if not jacadastrado:
            self.processar("INSERT INTO cliente(nome, email, cpf, endereco, numero_celular) VALUES(%s,%s,%s,%s,%s)", 
                    (nome,email, cpf, endereco, numero_celular))
            
            print("Cliente cadastrado com sucesso!")
        else:
            print("Cliente já cadastrado!")

    def ler_clientes(self):
        leitura = self.processar("SELECT * FROM cliente ORDER BY idcliente", fetch = True)
        return leitura
    
    def atualizar_cliente(self, coluna, novo_valor, cpf):
        if coluna not in self.colunas_permitidas:
            print(f"Não é possível alterar a coluna: {coluna}")
            return
    
        alteracao = self.processar(
        f"UPDATE cliente SET {coluna} = %s WHERE cpf = %s",
        (novo_valor, cpf))

        if alteracao == 0:
            print("CPF não encontrado, nenhum cliente atualizado.")
        else:
            print("Cliente atualizado com sucesso!")

    def deletar_cliente(self, cpf):
        deletar = self.processar("DELETE FROM cliente where cpf = %s", (cpf,))

        if deletar == 0:
            print("CPF não encontrado, nenhum cliente removido.")
        else:
            print("cliente removido com sucesso!")