from crud import Crud

class Pagamento(Crud):

    tabela = 'pagamento'
    colunas_permitidas = ['idcliente', 'idagenda', 'valor', 'data_pagamento', 'metodo_pagamento']
    coluna_id = 'idpagamento'
    
    def ler_todos_pagamentos(self):
        return super().ler_todos()
    
    def atualizar_pagamento(self, coluna, novo_valor, id):
        return super().atualizar(coluna, novo_valor, id)
    
    def deletar_pagamento(self, id):
        return super().deletar(id)
    
    def registrar_pagamento(self, idagenda, metodo_pagamento, idcliente):
        try:
            buscar_valor = self.processar(
                                        """ SELECT S.VALOR
                                            FROM AGENDA A
                                            INNER JOIN SERVICO S ON A.IDSERVICO = S.IDSERVICO
                                            WHERE A.IDAGENDA = %s """,
                                            (idagenda,), fetch=True)
            
        except Exception as e:
            raise ValueError(f"Erro ao buscar valor do serviço: {e}")
        
        super().cadastro(
            idagenda = idagenda,
            valor = buscar_valor[0][0],
            forma_pagamento = metodo_pagamento
        )

        print("Pagamento registrado com sucesso.")

    
