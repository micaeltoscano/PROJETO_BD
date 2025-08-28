from crud import Crud

class Itens_compra(Crud):

    tabela = 'itens_compra'
    colunas_permitidas = ['idproduto', 'quantidade', 'valor_unitario', 'valor_total_item']
    coluna_id = 'iditens_compra'

    def receber_produtos(self):
        condicao = True

        while condicao:
            try:
                idproduto = int(input("Digite o ID do produto que está recebendo (ou 0 para sair): "))
                if idproduto == 0:
                    condicao = False

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
                                idproduto = idproduto,
                                quantidade = quantidade,
                                valor_unitario = valor_unitario,
                                valortotal = valor_total_item)
                
            except ValueError:
                print("Por favor, digite um número válido.")