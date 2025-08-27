from crud import Crud

class Clientes(Crud):

    tabela = 'cliente'
    colunas_permitidas = ['nome', 'email', 'endereco', 'numero_celular']  
    coluna_id = 'idcliente'

    def cadastrar_cliente(self, nome, email, cpf, endereco, numero_celular):

        #SUPER() É TIPO AQUELE :: DO C++, QUE ACESSA ATRIBUTOS E METODOS DA CLASSE MAE A PARTIR DE UMA CLASSE FILHA
        super().cadastro(
            nome = nome,
            email = email,
            cpf = cpf,
            endereco = endereco, 
            numero_celular = numero_celular
        )
    
    def ler_cliente(self):
        return super().ler()
    
    def atualizar_cliente(self, coluna, novo_valor, id):
        return super().atualizar(coluna, novo_valor, id)

    def deletar_cliente(self, id):
        return super().deletar_servico(id)