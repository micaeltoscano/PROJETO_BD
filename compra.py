from crud import Crud
from itens_compra import Itens_compra
from estoque import Estoque

class Compra(Crud):
    tabela = 'compra'
    colunas_permitidas = ['idproduto', 'data_compra', 'valor_total']
    coluna_id = 'id_compra'
    
    def ler_todas_compras(self):
        return super().ler_todos()
    
    def atualizar_compra(self, coluna, novo_valor, id):
        return super().atualizar(coluna, novo_valor, id)
    
    def deletar_compra(self, id):
        return super().deletar(id)
    

    def registrar_compra(self):
        
        estoque = Estoque()
        super().cadastro(valor_total=0)

        #Pega o último ID_COMPRA inserido
        id_compra = self.processar("SELECT MAX(id_compra) FROM compra", fetch=True)[0][0]

        itens = Itens_compra()
        itens.receber_produtos(id_compra)

        total_compra = self.processar(
                                    "SELECT SUM(valor_total_item) FROM itens_compra WHERE id_compra = %s",
                                    (id_compra,), fetch=True)[0][0]

        self.atualizar_compra('valor_total', total_compra, id_compra)
    
        estoque.atualizar_quantidade('venda', id_compra)

        print(f"Compra {id_compra} registrada com sucesso! Total: {total_compra}")
