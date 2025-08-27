from crud import Crud

class Pagamento(Crud):

    tabela = 'pagamento'
    colunas_permitidas = ['idcliente', 'idagenda', 'valor', 'data_pagamento', 'metodo_pagamento']
    coluna_id = 'idpagamento'
    
    def ler(self):
        return super().ler()
    
    def atualizar_pagamento(self, coluna, novo_valor, id):
        return super().atualizar(coluna, novo_valor, id)
    
    def deletar_pagamento(self, id):
        return super().deletar(id)