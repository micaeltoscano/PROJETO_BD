from banco import Banco

class Clientes(Banco):
    colunas_permitidas = ['nome', 'email', 'endereco', 'numero_celular']  

    #FUNCAO PARA CADASTRAR O CLIENTE. Ñ HÁ NECESSIDADE DE COLOCAR A VERIFICACAO AQUI, PQ NO SCRIPT DO BD O CPF E O EMAIL JÁ SAO UNIQUE
    def cadastrar_cliente(self, nome, email, cpf, endereco, numero_celular):
        
        try:
            self.processar("INSERT INTO cliente(nome, email, cpf, endereco, numero_celular) VALUES(%s,%s,%s,%s,%s)", 
                        (nome,email, cpf, endereco, numero_celular))
                
            print("Cliente cadastrado com sucesso!")

        except Exception as e:
            print(f"Erro ao cadastrar cliente: {e}")
        

    def ler_clientes(self):

        leitura = self.processar("SELECT * FROM cliente ORDER BY idcliente", fetch = True)
        return leitura
    
    def atualizar_cliente(self, coluna, novo_valor, cpf):

        if coluna not in self.colunas_permitidas:
            print(f"Não é possível alterar a coluna: {coluna}")
            return

        try:
            alteracao = self.processar(
            f"UPDATE cliente SET {coluna} = %s WHERE cpf = %s",
            (novo_valor, cpf))

            if alteracao == 0:
                print("CPF não encontrado, nenhum cliente atualizado.")
            else:
                print("Cliente atualizado com sucesso!")
        
        except Exception as e:
            print(f"Erro ao atualizar cliente: {e}")

    def deletar_cliente(self, cpf):

        try:
            deletar = self.processar("DELETE FROM cliente where cpf = %s", (cpf,))

            if deletar == 0:
                print("CPF não encontrado, nenhum cliente removido.")
            else:
                print("cliente removido com sucesso!")
        
        except Exception as e:
            print(f"Erro ao deletar cliente: {e}")