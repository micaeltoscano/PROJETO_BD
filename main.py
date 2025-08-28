from funcionarios import Funcionario
from clientes import Clientes
from agendas import Agenda
from disponibilidade import Disponibilidade
from categoria import Categoria
from servico import Servico
from compra import Compra

agenda = Agenda()
funcionario = Funcionario()
cliente = Clientes()
disponibilidade = Disponibilidade()
categoria = Categoria()
servico = Servico()
compra = Compra()

#---------------------categoria---------------------
# categoria.cadastro_categoria('cabelo')
# print(categoria.ler_todas_categorias())

#categoria.atualizar_categoria('nome_categoria', 'barba', 1)
#print(categoria.ler())

#---------------------serviço---------------------
# servico.cadastro_servico('Corte de Cabelo', 50.0, 1, 60)
print(servico.ler_todos_servicos())

#servico.atualizar_servico('valor', 60.0, 1)
#print(servico.ler_servico())

#---------------------funcionarios---------------------
#funcionario.cadastrar_funcionario('Hugostoso', 'hugostoso@gmail.com', '12345678900', 'Rua B', '11999999999', 10, 'barbeiro', 0.5)
print(funcionario.ler_todos_funcionarios())

#---------------------disponibilidade---------------------
# disponibilidade.cadastro_disponibilidade(3, 'quarta', '09:00', '17:00')
# print(disponibilidade.ler_todas_disponibilidades())

#disponibilidade.atualizar_disponibilidade('hora_fim', '18:00', 1)
#print(disponibilidade.ler_disponibilidade())
 
#---------------------cliente---------------------
# cliente.cadastrar_cliente('Micael', 'micael.toscano@gmail.com', '12345678900', 'Rua A', '11999999999')
print(cliente.ler_todos_clientes())

#cliente.atualizar_cliente('numero_celular', '11988888888', 1)

#print(cliente.ler_cliente())

#---------------------agenda---------------------
#agenda.cadastrar_agenda('2024-12-25', '10:00', 3, 8, 1)
print(agenda.ler_agenda())

#agenda.atualizar_agenda('status', 'concluido', 1)
#print(agenda.ler_agenda())

#agenda.deletar(3)
#print(agenda.ler_agenda())

# 30 requisições de cadastro de clientes
# cliente.cadastrar_cliente('Micael', 'micael.toscano@gmail.com', '12345678900', 'Rua A', '11999999999')
# cliente.cadastrar_cliente('Ana Silva', 'ana.silva@hotmail.com', '98765432100', 'Av. Paulista', '11988887777')
# cliente.cadastrar_cliente('Carlos Santos', 'carlos.santos@yahoo.com', '45678912300', 'Rua das Flores', '11977776666')
# cliente.cadastrar_cliente('Maria Oliveira', 'maria.oliveira@gmail.com', '32165498700', 'Travessa da Paz', '11966665555')
# cliente.cadastrar_cliente('João Pereira', 'joao.pereira@outlook.com', '78912345600', 'Alameda Santos', '11955554444')
# cliente.cadastrar_cliente('Fernanda Costa', 'fernanda.costa@gmail.com', '65498732100', 'Praça da Sé', '11944443333')
# cliente.cadastrar_cliente('Ricardo Almeida', 'ricardo.almeida@hotmail.com', '15975348600', 'Rua Augusta', '11933332222')
# cliente.cadastrar_cliente('Juliana Martins', 'juliana.martins@yahoo.com', '35795148600', 'Av. Brigadeiro', '11922221111')
# cliente.cadastrar_cliente('Pedro Souza', 'pedro.souza@gmail.com', '25836914700', 'Rua XV de Novembro', '11911110000')
# cliente.cadastrar_cliente('Amanda Rodrigues', 'amanda.rodrigues@outlook.com', '14725836900', 'Alameda Campinas', '11900009999')
# cliente.cadastrar_cliente('Bruno Lima', 'bruno.lima@gmail.com', '36925814700', 'Av. Faria Lima', '11999998888')
# cliente.cadastrar_cliente('Camila Ferreira', 'camila.ferreira@hotmail.com', '48627315900', 'Rua Oscar Freire', '11988887776')
# cliente.cadastrar_cliente('Diego Santos', 'diego.santos@yahoo.com', '58263917400', 'Praça da República', '11977776665')
# cliente.cadastrar_cliente('Eduarda Silva', 'eduarda.silva@gmail.com', '69317428500', 'Av. Rebouças', '11966665554')
# cliente.cadastrar_cliente('Fábio Costa', 'fabio.costa@outlook.com', '17428539600', 'Rua da Consolação', '11955554443')
# cliente.cadastrar_cliente('Gabriela Oliveira', 'gabriela.oliveira@gmail.com', '28539641700', 'Alameda Jaú', '11944443332')
# cliente.cadastrar_cliente('Henrique Pereira', 'henrique.pereira@hotmail.com', '39641752800', 'Av. Europa', '11933332221')
# cliente.cadastrar_cliente('Isabela Martins', 'isabela.martins@yahoo.com', '41752863900', 'Rua Haddock Lobo', '11922221110')
# cliente.cadastrar_cliente('Lucas Souza', 'lucas.souza@gmail.com', '52863974100', 'Praça Charles Miller', '11911110009')
# cliente.cadastrar_cliente('Mariana Rodrigues', 'mariana.rodrigues@outlook.com', '63974185200', 'Av. São João', '11900009998')
# cliente.cadastrar_cliente('Nathan Lima', 'nathan.lima@gmail.com', '74185296300', 'Rua 25 de Março', '11999998887')
# cliente.cadastrar_cliente('Olivia Ferreira', 'olivia.ferreira@hotmail.com', '85296317400', 'Av. Ipiranga', '11988887775')
# cliente.cadastrar_cliente('Paulo Santos', 'paulo.santos@yahoo.com', '96317428500', 'Rua Xavier de Toledo', '11977776664')
# cliente.cadastrar_cliente('Quintino Silva', 'quintino.silva@gmail.com', '17428539610', 'Praça da Árvore', '11966665553')
# cliente.cadastrar_cliente('Rafaela Costa', 'rafaela.costa@outlook.com', '28539641720', 'Av. Pacaembu', '11955554442')
# cliente.cadastrar_cliente('Sérgio Oliveira', 'sergio.oliveira@gmail.com', '39641752830', 'Rua Maria Antônia', '11944443331')
# cliente.cadastrar_cliente('Tatiane Pereira', 'tatiane.pereira@hotmail.com', '41752863940', 'Alameda Lorena', '11933332220')
# cliente.cadastrar_cliente('Ubirajara Martins', 'ubirajara.martins@yahoo.com', '52863974150', 'Av. Morumbi', '11922221119')
# cliente.cadastrar_cliente('Vanessa Souza', 'vanessa.souza@gmail.com', '63974185260', 'Rua Vergueiro', '11911110008')
# cliente.cadastrar_cliente('William Rodrigues', 'william.rodrigues@outlook.com', '74185296370', 'Praça Roosevelt', '11900009997')

#agenda.confirmar_servico(1, 'cartao', 1)

