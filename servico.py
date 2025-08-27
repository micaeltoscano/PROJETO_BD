from crud import Crud

class Servico(Crud):

    tabela = "servico"
    colunas_permitidas = ['nome', 'valor', 'duracao']
    coluna_id = 'idservico'

    def cadastro_servico(self, nome_servico, valor, id_categoria, duracao):

        super().cadastro(
            nome_servico = nome_servico, 
            valor = valor, 
            id_categoria = id_categoria, 
            duracao = duracao
        )

    def ler_servico(self):
        return super().ler()
    
    def atualizar_servico(self, coluna, novo_valor, id):
        return super().atualizar(coluna, novo_valor, id)
    
    def deletar_servico(self, id):
        return super().deletar(id)
    
    