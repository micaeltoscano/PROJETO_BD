from crud import Crud

class Clientes(Crud):

    tabela = 'cliente'
    colunas_permitidas = ['nome', 'email', 'cpf', 'endereco', 'numero_celular']  
    coluna_id = 'idcliente'

    def cadastrar_cliente(self, nome, email, cpf, endereco, numero_celular):
        
        super().cadastro(
            nome = nome,
            email = email,
            cpf = cpf,
            endereco = endereco, 
            numero_celular = numero_celular
        )
    
    def ler_todos_clientes(self):
        return super().ler_todos()
    
    def pesquisar_nome(self, nome):
        return super().pesquisar_nome(nome) 
    
    def ler_um_cliente(self, id):
        return super().listar_um(id)
    
    def atualizar_cliente(self, coluna, novo_valor, id):
        return super().atualizar(coluna, novo_valor, id)

    def deletar_cliente(self, id):
        return super().deletar(id)