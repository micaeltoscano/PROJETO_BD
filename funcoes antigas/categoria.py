from banco import Banco

class Categoria(Banco):
    colunas_permitidas = ['nome_categoria']

    def cadastrar_categoria(self, nome_categoria):
        try:
            self.processar(
                            "INSERT INTO categoria(nome_categoria) VALUES(%s)",
                            (nome_categoria,))
            
            print(f"Categoria '{nome_categoria}' cadastrada com sucesso!")

        except Exception as e:
            print(f"Erro ao cadastrar categoria: {e}")

    def ler_categoria(self):
        try:
            leitura = self.processar(
                "SELECT * FROM categoria ORDER BY idcategoria",
                fetch=True
            )
            return leitura
        
        except Exception as e:
            print(f"Erro ao listar categorias: {e}")
            return []

    def atualizar_categoria(self, coluna, novo_valor, idcategoria):

        if coluna not in self.colunas_permitidas:
            print(f"Não é possível alterar a coluna: {coluna}")
            return

        try:
            alteracao = self.processar(
                f"UPDATE categoria SET {coluna} = %s WHERE idcategoria = %s",
                (novo_valor, idcategoria)
            )
            if alteracao == 0:
                print("Categoria não encontrada, nenhuma atualização realizada.")
            else:
                print("Categoria atualizada com sucesso!")

        except Exception as e:
            print(f"Erro ao atualizar categoria: {e}")

    def deletar_categoria(self, idcategoria):
        
        try:
            deletar = self.processar(
                "DELETE FROM categoria WHERE idcategoria = %s",
                (idcategoria,)
            )
            if deletar == 0:
                print("Categoria não encontrada, nenhum registro removido.")
            else:
                print("Categoria removida com sucesso!")

        except Exception as e:
            print(f"Erro ao deletar categoria: {e}")
