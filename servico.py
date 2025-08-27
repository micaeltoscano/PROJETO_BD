from crud import Crud

class Servico(Crud):

    def cadastro_servico(self, nome_servico, valor, nome_categoria, duracao):
        super().cadastro(
            nome_servico = nome_servico, 
            valor = valor, 
            nome_categoria = nome_categoria, 
            duracao = duracao
        )

    def ler_servico(self):
        return super().ler()
    
    def atualizar_servico(self, coluna, novo_valor, id):
        return super().atualizar(coluna, novo_valor, id)
    
    def deletar_servico(self, id):
        return super().deletar(id)