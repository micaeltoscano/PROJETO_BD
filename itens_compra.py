from crud import Crud

class Itens_compra(Crud):

    tabela = 'itens_compra'
    colunas_permitidas = ['id_compra', 'idproduto', 'quantidade', 'valor_unitario', 'valor_total_item']
    coluna_id = 'id_itens_compra'

    def receber_produtos(self, idcompra):
        condicao = True

        while condicao:
            try:
                idproduto = int(input("Digite o ID do produto que está recebendo (ou 0 para sair): "))
                if idproduto == 0:
                    break

                quantidade = int(input("Digite a quantidade recebida: "))
                if quantidade <= 0:
                    print("Quantidade deve ser maior que zero.")
                    continue

                consulta = self.processar(
                                            """ SELECT VALOR
                                                FROM PRODUTO 
                                                WHERE IDPRODUTO = %s """,
                                            (idproduto,), fetch=True)
                
                valor_unitario = consulta[0][0]
                valor_total_item = valor_unitario * quantidade
                
                super().cadastro(
                                id_compra = idcompra,
                                id_produto = idproduto,
                                quantidade = quantidade,
                                valor_unitario = valor_unitario,
                                valor_total_item = valor_total_item)
                
            except ValueError:
                print("Por favor, digite um número válido.")

    def ler_todos_itens_compra(self):
        return super().ler_todos()