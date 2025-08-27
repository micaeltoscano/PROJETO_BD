from crud import Crud

class Pagamento(Crud):

    def cadastro_pagamento(self, IDPAGAMENTO, IDAGENDA, VALOR, FORMA_PAGAMENTO, DATA_PAGAMENTO, ID_COMPRA, TIPO_PAGAMENTO):
        super().cadastro(
            IDPAGAMENTO = IDPAGAMENTO, 
            IDAGENDA = IDAGENDA, 
            VALOR = VALOR, 
            FORMA_PAGAMENTO = FORMA_PAGAMENTO, 
            DATA_PAGAMENTO = DATA_PAGAMENTO, 
            ID_COMPRA = ID_COMPRA, 
            TIPO_PAGAMENTO = TIPO_PAGAMENTO
        )
    
    def ler(self):
        return super().ler()
    
    def atualizar_pagamento(self, coluna, novo_valor, id):
        return super().atualizar(coluna, novo_valor, id)
    
    def deletar_pagamento(self, id):
        return super().deletar(id)