from crud import Crud

class Funcionario(Crud):

    tabela = 'funcionario'
    colunas_permitidas = ['nome', 'email', 'endereco', 'numero_celular', 'salario', 'especialidade', 'comissao']
    coluna_id = 'idfuncionario'

    def cadastrar_funcionario(self, nome, email, cpf, endereco, numero_celular, salario, especialidade, comissao):
        super().cadastro(
            nome = nome,
            email = email, 
            cpf = cpf, 
            endereco = endereco,
            numero_celular = numero_celular,
            salario = salario,
            especialidade = especialidade,
            comissao = comissao
        )
    
    def ler_funcionario(self):
        return super().ler()
    
    def atualizar_funcionario(self, coluna, novo_valor, id):
        return super().atualizar(coluna, novo_valor, id)
    
    def deletar_funcionario(self, id):
        return super().deletar(id)