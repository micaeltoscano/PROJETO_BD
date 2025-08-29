from crud import Crud
from itens_compra import Itens_compra
from estoque import Estoque
from pagamentos import Pagamento

class Compra(Crud):
    tabela = 'compra'
    colunas_permitidas = ['data_compra', 'valor_total']
    coluna_id = 'idcompra'
    
    def ler_todas_compras(self):
        return super().ler_todos()
    
    def atualizar_compra(self, coluna, novo_valor, id):
        return super().atualizar(coluna, novo_valor, id)
    
    def deletar_compra(self, id):
        return super().deletar(id)
    

    def registrar_compra(self, metodo_pagamento):
        
        estoque = Estoque()
        pagamento = Pagamento()
        
        #FALTA COLOCAR NO SCRIPT DO BD OS ATRIBUTOS METODO_PAGAMENTO E IDCLIENTE NA TABELA COMPRA
        super().cadastro(valor_total=0)
        print(self.ler_todas_compras())
        #PEGA O ULTIMO ID INSERIDO
        id_compra = self.processar("SELECT MAX(idcompra) FROM compra", fetch=True)[0][0]

        itens = Itens_compra()
        itens.receber_produtos(id_compra)

        total_compra = self.processar(
                                    "SELECT SUM(valor_total_item) FROM itens_compra WHERE id_compra = %s",
                                    (id_compra,), fetch=True)[0][0]

        self.atualizar_compra('valor_total', total_compra, id_compra)

        pagamento.registrar_pagamento_produto(id_compra, metodo_pagamento)
    
        estoque.atualizar_quantidade('venda', id_compra)

        print(f"Compra {id_compra} registrada com sucesso! Total: {total_compra}")
