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

#---------------------categoria---------------------
# categoria.cadastro_categoria('cabelo')
# print(categoria.ler_todas_categorias())

# categoria.atualizar_categoria('nome_categoria', 'barba', 1)
# print(categoria.ler())

#---------------------serviço---------------------
# servico.cadastro_servico('Corte de Cabelo', 50.0, 1, 60)
# print(servico.ler_todos_servicos())

#servico.atualizar_servico('valor', 60.0, 1)
#print(servico.ler_servico())

#---------------------funcionarios---------------------
# funcionario.cadastrar_funcionario('Hugostoso', 'hugostoso@gmail.com', '12345678900', 'Rua B', '11999999999', 10, 'barbeiro', 0.5)
# print(funcionario.ler_todos_funcionarios())

#---------------------disponibilidade---------------------
# disponibilidade.cadastro_disponibilidade(1, 'quarta', '09:00', '17:00')
# print(disponibilidade.ler_todas_disponibilidades())

#disponibilidade.atualizar_disponibilidade('hora_fim', '18:00', 1)
#print(disponibilidade.ler_disponibilidade())
 
#---------------------cliente---------------------
# cliente.cadastrar_cliente('Micael', 'micael.toscano@gmail.com', '12345678900', 'Rua A', '11999999999')
# print(cliente.ler_todos_clientes())

#cliente.atualizar_cliente('numero_celular', '11988888888', 1)

#print(cliente.ler_cliente())

#---------------------produto---------------------
# produto.cadastro_produto(5, 'Navalha', 'acessorios')
# produto.cadastro_produto(50, 'Shampoo', 'higiene')
# print(produto.ler_todos_produtos())

#---------------------UTILIZA---------------------
#PROBLEMA: CADASTRO DUPLICADO DE SERVICO QUE USA O MESMO PRODUTO

# utiliza.cadastro_utiliza(1, 2, 1)
# print(utiliza.ler_todos_utiliza())

#--------------------ESTOQUE---------------------
# estoque.cadastro_estoque(1,100,0)
# estoque.cadastro_estoque(2,50,0)
# print(estoque.ler_todo_estoque())

#---------------------agenda---------------------
# agenda.cadastrar_agenda('2024-12-25', '10:00', 1, 1, 1)
# print(agenda.ler_agenda())

#agenda.atualizar_agenda('status', 'concluido', 1)
#print(agenda.ler_agenda())

#agenda.deletar(3)
#print(agenda.ler_agenda())

#agenda.confirmar_servico(1, 'cartao', 1)

#---------------------pagamento---------------------
# print(pagamento.ler_todos_pagamentos())
# print(estoque.ler_todo_estoque())

#---------------------compra---------------------


#print(estoque.ler_todo_estoque())
#print(itenscompra.ler_todos_itens_compra())
#compra.registrar_compra()

#print(estoque.ler_todo_estoque())
#print(utiliza.ler_todos_utiliza())

#agenda.cadastrar_agenda('2024-12-25', '11:00', 1, 1, 1)
#print(agenda.ler_agenda())

#print(utiliza.ler_todos_utiliza())
#agenda.confirmar_servico(2, 'cartao', 1)
#print(estoque.ler_todo_estoque())

# agenda.cadastrar_agenda('2024-12-25', '13:00', 1, 1, 1)
# agenda.confirmar_servico(2, 'cartao', 1)
# print(estoque.ler_todo_estoque())

#print(utiliza.ler_todos_utiliza())

#print(estoque.ler_todo_estoque())

#compra.registrar_compra()

print(estoque.ler_todo_estoque())