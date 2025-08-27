from funcionarios import Funcionario
from clientes import Clientes
from agendas import Agenda
from disponibilidade import Disponibilidade

agenda = Agenda()
funcionario = Funcionario()
cliente = Clientes()
disponibilidade = Disponibilidade()

#disponibilidade.cadastro_disponibilidade(6, 'quarta', '09:00', '17:00')
#print(disponibilidade.ler_disponibilidade())

#print(funcionario.ler_funcionario())

agenda.cadastrar_agenda('2024-12-25', '10:00', 6, 'Corte de Cabelo')