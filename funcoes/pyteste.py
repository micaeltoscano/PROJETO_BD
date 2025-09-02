from funcionarios import Funcionario
from clientes import Clientes
from agendas import Agenda
from disponibilidade import Disponibilidade
from categoria import Categoria
from servico import Servico
from compra import Compra
from utiliza import Utiliza
from produto import Produto
from estoque import Estoque
from pagamentos import Pagamento
from compra import Compra
from itens_compra import Itens_compra

agenda = Agenda()
funcionario = Funcionario()
cliente = Clientes()
disponibilidade = Disponibilidade()
categoria = Categoria()
servico = Servico()
compra = Compra()
utiliza = Utiliza()
produto = Produto()
estoque = Estoque()
pagamento = Pagamento()
compra = Compra()
itenscompra = Itens_compra()

print(produto.pesquisar_nome_produto('navalha de caneco'))
#produto.atualizar_produto('status', 'INATIVO', 1)
#print(produto.ler_todos_produtos())