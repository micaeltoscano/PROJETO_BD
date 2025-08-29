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
categoria.cadastro_categoria('cabelo')
print(categoria.ler_todas_categorias())


#---------------------serviço---------------------
servico.cadastro_servico('Corte de Cabelo', 50.0, 1, 60)
print(servico.ler_todos_servicos())

#---------------------funcionarios---------------------
funcionario.cadastrar_funcionario('Hugostoso', 'hugostoso@gmail.com', '12345678900', 'Rua B', '11999999999', 10, 'barbeiro')
print(funcionario.ler_todos_funcionarios())

#---------------------disponibilidade---------------------
disponibilidade.cadastro_disponibilidade(1, 'quarta', '09:00', '17:00')
print(disponibilidade.ler_todas_disponibilidades())

#---------------------produto---------------------
produto.cadastro_produto(5, 'Navalha', 'acessorios')
produto.cadastro_produto(50, 'Shampoo', 'higiene')
print(produto.ler_todos_produtos())

#---------------------UTILIZA---------------------
#PROBLEMA: CADASTRO DUPLICADO DE SERVICO QUE USA O MESMO PRODUTO

utiliza.cadastro_utiliza(1, 2, 1)
print(utiliza.ler_todos_utiliza())

#--------------------ESTOQUE---------------------
estoque.cadastro_estoque(1,100,0)
estoque.cadastro_estoque(2,50,0)
print(estoque.ler_todo_estoque())

#---------------------agenda---------------------
agenda.cadastrar_agenda('2024-12-25', '10:00', 1, 1, 1)
print(agenda.ler_agenda())

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

#print(estoque.ler_todo_estoque())

#--------------------- TESTES COM CLIENTES ---------------------

# cliente.cadastrar_cliente('Ana Silva', 'ana.silva@hotmail.com', '98765432100', 'Av. Paulista', '11988887777')
# cliente.cadastrar_cliente('Carlos Santos', 'carlos.santos@yahoo.com', '45678912300', 'Rua das Flores', '11977776666')
# cliente.cadastrar_cliente('Maria Oliveira', 'maria.oliveira@gmail.com', '32165498700', 'Travessa da Paz', '11966665555')

#TESTE DA LEITURA DE TODOS OS CLIENTES:

    # for n in (cliente.ler_todos_clientes()): 
    #     print(n)

    #RETORNO DA EXECUÇÃO:

    # {'idcliente': 1, 'nome': 'Micael', 'email': 'micael.toscano@gmail.com', 'cpf': '12345678900', 'endereco': 'Rua A', 'numero_celular': '11999999999'}
    # {'idcliente': 3, 'nome': 'Ana Silva', 'email': 'ana.silva@hotmail.com', 'cpf': '98765432100', 'endereco': 'Av. Paulista', 'numero_celular': '11988887777'}
    # {'idcliente': 4, 'nome': 'Carlos Santos', 'email': 'carlos.santos@yahoo.com', 'cpf': '45678912300', 'endereco': 'Rua das Flores', 'numero_celular': '11977776666'}
    # {'idcliente': 5, 'nome': 'Maria Oliveira', 'email': 'maria.oliveira@gmail.com', 'cpf': '32165498700', 'endereco': 'Travessa da Paz', 'numero_celular': '11966665555'}

#TESTE DA PESQUISA PELO NOME DO CLIENTE:

    #print(cliente.pesquisar_nome('Micael'))

    #RETORNO DA EXECUÇÃO:
    #[(1, 'Micael', 'micael.toscano@gmail.com', '12345678900', 'Rua A', '11999999999')]

#TESTE DE LEITURA DE UM CLIENTE PELO ID:

    #print(cliente.ler_um_cliente(3))

    #RETORNO DA EXECUÇÃO:

    #[(3, 'Ana Silva', 'ana.silva@hotmail.com', '98765432100', 'Av. Paulista', '11988887777')]

#TESTE DE ATUALIZAÇÃO DE UM CLIENTE:

    # cliente.atualizar_cliente('nome', 'hugostoso', 3)
    # print(cliente.ler_um_cliente(3))

    #RETORNO DA EXECUÇÃO:

    #[(3, 'hugostoso', 'ana.silva@hotmail.com', '98765432100', 'Av. Paulista', '11988887777')]

#TESTE DE DELEÇÃO DE UM CLIENTE:

    #cliente.deletar_cliente(3)
    #print(cliente.ler_um_cliente(3))

    #RETORNO DA EXECUÇÃO:
    #[]

#--------------------- TESTES COM PRODUTOS ---------------------

#TESTE DE CADASTRO DE PRODUTOS:

    # produto.cadastro_produto(50,'condicionador', 'higiene')
    # for n in produto.ler_todos_produtos():
    #     print(n)

    #RETORNO DA EXECUÇÃO:
    # {'idproduto': 1, 'valor': 'Navalha', 'nome': Decimal('5.00'), 'tipo': 'acessorios'}
    # {'idproduto': 2, 'valor': 'Shampoo', 'nome': Decimal('50.00'), 'tipo': 'higiene'}
    # {'idproduto': 6, 'valor': 'condicionador', 'nome': Decimal('50.00'), 'tipo': 'higiene'}

    #PROBLEMAS:
    # produto.cadastro_produto(50,'Condicionador', 'higiene')
    # for n in produto.ler_todos_produtos():
    #     print(n)
    # {'idproduto': 1, 'valor': 'Navalha', 'nome': Decimal('5.00'), 'tipo': 'acessorios'}
    # {'idproduto': 2, 'valor': 'Shampoo', 'nome': Decimal('50.00'), 'tipo': 'higiene'}
    # {'idproduto': 6, 'valor': 'condicionador', 'nome': Decimal('50.00'), 'tipo': 'higiene'}
    # {'idproduto': 10, 'valor': 'Condicionador', 'nome': Decimal('50.00'), 'tipo': 'higiene'}

#TESTE DE ATUALIZAÇÃO DE UM PRODUTO:

    # produto.atualizar_produto('nome', 'Condicionador Plus', 6)

    # for n in produto.ler_todos_produtos():
    #     print(n)

    # #RETORNO DA EXECUÇÃO:
    # {'idproduto': 1, 'valor': 'Navalha', 'nome': Decimal('5.00'), 'tipo': 'acessorios'}
    # {'idproduto': 2, 'valor': 'Shampoo', 'nome': Decimal('50.00'), 'tipo': 'higiene'}
    # {'idproduto': 6, 'valor': 'Condicionador Plus', 'nome': Decimal('50.00'), 'tipo': 'higiene'}
    # {'idproduto': 10, 'valor': 'Condicionador', 'nome': Decimal('50.00'), 'tipo': 'higiene'}

#TESTE DE DELEÇÃO DE UM PRODUTO:

    # produto.deletar_produto(10)
    # for n in produto.ler_todos_produtos():
    #     print(n)

    # #RETORNO DA EXECUÇÃO:
    # {'idproduto': 1, 'valor': 'Navalha', 'nome': Decimal('5.00'), 'tipo': 'acessorios'}
    # {'idproduto': 2, 'valor': 'Shampoo', 'nome': Decimal('50.00'), 'tipo': 'higiene'}
    # {'idproduto': 6, 'valor': 'Condicionador Plus', 'nome': Decimal('50.00'), 'tipo': 'higiene'}

#TESTE DE PESQUISA PELO NOME DO PRODUTO:

    # print(produto.pesquisar_nome_produto('Shampoo'))

    # #RETORNO DA EXECUÇÃO:
    # [(2, 'Shampoo', Decimal('50.00'), 'higiene')]

#TESTE DE LEITURA DE UM PRODUTO PELO ID:
    # print(produto.ler_um_produto(2))

    # #RETORNO DA EXECUÇÃO:
    # [(2, 'Shampoo', Decimal('50.00'), 'higiene')]

#--------------------- TESTES COM ESTOQUE ---------------------

#TESTE DE CADASTRO DE ESTOQUE:

    # estoque.cadastro_estoque(6,200,0)

    # for n in estoque.ler_todo_estoque():
    #     print(n)

    # #RETORNO DA EXECUÇÃO:
    # {'id_estoque': 1, 'id_produto': 1, 'quantidade_atual': 90, 'quantidade_minima': 0, 'ultima_atualizacao': datetime.datetime(2025, 8, 28, 23, 3, 7, 146886)}
    # {'id_estoque': 2, 'id_produto': 2, 'quantidade_atual': 49, 'quantidade_minima': 0, 'ultima_atualizacao': datetime.datetime(2025, 8, 28, 23, 3, 7, 162436)}
    # {'id_estoque': 7, 'id_produto': 6, 'quantidade_atual': 200, 'quantidade_minima': 0, 'ultima_atualizacao': datetime.datetime(2025, 8, 29, 0, 45, 52, 783755)}

#TESTE DE ATUALIZAÇÃO DE UM ESTOQUE:

    # #estoque.atualizar_estoque('quantidade_atual', 180, 7)
    # print(estoque.ler_um_estoque(7))

    # # #RETORNO DA EXECUÇÃO:
    # [(7, 6, 180, 0, datetime.datetime(2025, 8, 29, 0, 45, 52, 783755))]

# TESTE DE DELEÇÃO DE UM ESTOQUE:

    # estoque.deletar_estoque(7)
    # print(estoque.ler_um_estoque(7))

    # #RETORNO DA EXECUÇÃO:
    # []

