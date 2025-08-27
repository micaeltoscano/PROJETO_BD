from funcionarios import Funcionario
from clientes import Clientes
from agendas import Agenda
from disponibilidade import Disponibilidade
from categoria import Categoria
from servico import Servico

agenda = Agenda()
funcionario = Funcionario()
cliente = Clientes()
disponibilidade = Disponibilidade()
categoria = Categoria()
servico = Servico()

#---------------------serviço---------------------
#servico.cadastro_servico('Corte de Cabelo', 50.0, 1, 60)
#print(servico.ler_servico())

#servico.atualizar_servico('valor', 60.0, 1)
#print(servico.ler_servico())

#---------------------categoria---------------------
#categoria.cadastro_categoria('cabelo')
#print(categoria.ler())

#categoria.atualizar_categoria('nome_categoria', 'barba', 1)
#print(categoria.ler())

#---------------------disponibilidade---------------------
#disponibilidade.cadastro_disponibilidade(6, 'quarta', '09:00', '17:00')
#print(disponibilidade.ler_disponibilidade())

#disponibilidade.atualizar_disponibilidade('hora_fim', '18:00', 1)
#print(disponibilidade.ler_disponibilidade())
 
#---------------------cliente---------------------
#cliente.cadastrar_cliente('Micael', 'micael.toscano@gmail.com', '12345678900', 'Rua A', '11999999999')
#print(cliente.ler_cliente())

#cliente.atualizar_cliente('numero_celular', '11988888888', 1)
#print(cliente.ler_cliente())

#---------------------agenda---------------------
#agenda.cadastrar_agenda('2024-12-25', '10:00', 6, 1, 1)
#print(agenda.ler_agenda())

#agenda.atualizar_agenda('status', 'concluido', 1)
#print(agenda.ler_agenda())

#agenda.deletar(3)
#print(agenda.ler_agenda())
