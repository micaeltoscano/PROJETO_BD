import crud
import clientes
import funcionarios
import servico
import categoria
import agendas

#agenda = Agenda()
#disponibilidade = Disponibilidade()
#compra = Compra()

class Interface:
    def __init__(self):
        pass

    def display_menu(self):
        input_opcao = 0

        while input_opcao != 5:
            print("==============================")
            print("   Bem-vindo ao sistema!  ")
            print("==============================")
            print("1 - Clientes")
            print("2 - Funcionários")
            print("3 - Serviços")
            print("4 - Agendas")
            print("5 - Sair")
            print("==============================")

            #Corrige a entrada do usuário:
            try:
                input_opcao = int(input("Escolha uma opção (1-5): "))
            except ValueError:
                print("Entrada inválida. Por favor, insira um número entre 1 e 5.")
                continue
            
            match input_opcao:
                case 1:
                    self.display_opcao_clientes()
                case 2:
                    self.display_opcao_funcionarios()
                case 3:
                    self.display_opcao_servicos()
                case 4:
                    self.display_opcao_agendas()
                case 5:
                    print("Saindo do sistema. Até logo!")
                case _:
                    print("Opção inválida. Tente novamente.")

    def display_opcao_clientes(self):
        input_opcao = 0
        cliente = clientes.Clientes()

        while input_opcao != 7:
            print("==============================")
            print("--- Menu Clientes ---")
            print("1 - Listar clientes")
            print("2 - Adicionar cliente")
            print("3 - Pesquisar_nome")
            print("4 - Ver um cliente (id)")
            print("5 - Atualizar cliente")
            print("6 - Deletar cliente")
            print("7 - Voltar")
            print("==============================")

            try:
                input_opcao = int(input("Escolha uma opção (1-7): "))
            except ValueError:
                print("Entrada inválida. Por favor, insira um número entre 1 e 7.")
                continue

            match input_opcao:
                case 1:
                    print("Listando clientes...")
                    print(cliente.ler_todos_clientes())
                    
                case 2:
                    print("Adicionando cliente...")

                    #Caso o usuário deseje adicionar um novo cliente, pra previnir as entradas inválidas
                    try:
                        nome = input("Nome: ")
                        email = input("Email: ")
                        cpf = input("CPF: ")
                        endereco = input("Endereço: ")
                        numero_celular = input("Número de celular: ")
                        clientes.Clientes().cadastrar_cliente(nome, email, cpf, endereco, numero_celular)

                    except Exception as e:
                        print(f"Erro ao adicionar cliente: \n{e}")
                    
                case 3:
                    nome = input("Nome para pesquisa: ")
                    resultados = cliente.pesquisar_nome(nome)
                    print(resultados)
                            
                case 4:
                    id_cliente = input("ID do cliente: ")
                    resultado = cliente.ler_um_cliente(id_cliente)
                    if len(resultado) == 0:
                        print("Cliente não encontrado.")
                    else:
                        print(resultado)

                case 5:
                    try:
                        coluna = input("Coluna a ser atualizada (nome, email, cpf, endereco, numero_celular): ")
                        novo_valor = input("Novo valor: ")
                        id_cliente = input("ID do cliente a ser atualizado: ")
                        cliente.atualizar_cliente(coluna, novo_valor, id_cliente)

                    except Exception as e:
                        print(f"Erro ao atualizar cliente: {e}")

                case 6:
                    id_cliente = input("ID do cliente a ser deletado: ")
                    cliente.deletar_cliente(id_cliente)

                case 7:
                    input("Pressione Enter para voltar ao menu principal...")
                    continue
                    
                case _:
                    print("Opção inválida. Tente novamente.")

    def display_opcao_funcionarios(self):
        input_opcao = 0
        funcionario = funcionarios.Funcionario()

        while input_opcao != 7:
            print("==============================")
            print("--- Menu Funcionários ---")
            print("1 - Listar Funcionários")
            print("2 - Adicionar Funcionário")
            print("3 - Pesquisar_nome")
            print("4 - Ver um Funcionário (id)")
            print("5 - Atualizar Funcionário")
            print("6 - Deletar Funcionário")
            print("7 - Voltar")
            print("==============================")

            try:
                input_opcao = int(input("Escolha uma opção (1-7): "))
            except ValueError:
                print("Entrada inválida. Por favor, insira um número entre 1 e 7.")
                continue
            
            match input_opcao:
                case 1:
                    print("Listando Funcionários...")
                    print(funcionario.ler_todos_funcionarios())

                case 2:
                    print("Adicionando Funcionário...")

                    # Caso o usuário deseje adicionar um novo funcionário, pra previnir as entradas inválidas
                    try:
                        nome = input("Nome: ")
                        email = input("Email: ")
                        cpf = input("CPF: ")
                        endereco = input("Endereço: ")
                        numero_celular = input("Número de celular: ")
                        salario = input("Salário: ")
                        especialidade = input("Especialidade: ")
                        funcionario.cadastrar_funcionario(nome, email, cpf, endereco, numero_celular, salario, especialidade)

                    except Exception as e:
                        print(f"Erro ao adicionar funcionário: {e}")

                case 3:
                    nome = input("Nome para pesquisa: ")
                    resultados = funcionario.pesquisar_nome(nome)
                    print(resultados)

                case 4:
                    id_funcionario = input("ID do funcionário: ")
                    resultado = funcionario.ler_um_funcionario(id_funcionario)
                    if len(resultado) == 0:
                        print("Funcionário não encontrado.")
                    else:
                        print(resultado)

                case 5:
                    try:
                        coluna = input("Coluna a ser atualizada (nome, email, cpf, endereco, numero_celular, salario, especialidade): ")
                        novo_valor = input("Novo valor: ")
                        id_funcionario = input("ID do funcionário a ser atualizado: ")
                        funcionario.atualizar_funcionario(coluna, novo_valor, id_funcionario)

                    except Exception as e:
                        print(f"Erro ao atualizar funcionário: {e}")

                case 6:
                    id_funcionario = input("ID do funcionário a ser deletado: ")
                    funcionario.deletar_funcionario(id_funcionario)

                case 7:
                    input("Pressione Enter para voltar ao menu principal...")
                    continue

                case _:
                    print("Opção inválida. Tente novamente.")


    def display_opcao_servicos(self):
        input_opcao = 0
        servicos = servico.Servico()
        categorias = categoria.Categoria()

        while input_opcao != 7:
            print("==============================")
            print("1 - Listar serviços")
            print("2 - Adicionar serviço")
            print("3 - Pesquisar nome do serviço")
            print("4 - Ver um serviço")
            print("5 - Atualizar serviço")
            print("6 - Deletar serviço")
            print("7 - Voltar")
            print("==============================")

            try:
                input_opcao = int(input("Escolha uma opção (1-7): "))
            except ValueError:
                print("Entrada inválida. Por favor, insira um número entre 1 e 7.")
                continue

            match input_opcao:
                case 1:
                    print("Listando Serviços...")
                    servicos.ler_todos_servicos()

                case 2:
                    try:
                        nome_servico  = input("Digite o nome do serviço:")
                        valor = input("Digite o valor do serviço:")
                        resposta = input("A categoria já foi cadastrada? (1 ou 0): ")

                        #Verifica se a categoria já existe
                        if resposta == 1 :
                            categorias.ler_todas_categorias()
                            id_categoria = input("Digite o id da categoria do serviço:")

                        else:
                            categoria_nome = input("Digite o nome da categoria:")
                            categorias.cadastro_categoria(categoria_nome)
                            categorias.ler_todas_categorias()
                            id_categoria = input("Digite o id da categoria do serviço:")

                        duracao = input("Digite a duração do serviço:")

                        servicos.cadastro_servico(nome_servico, valor, id_categoria, duracao)
                    
                    except Exception as e:
                        print(f"Erro ao adicionar serviço: {e}")

                case 3:
                    nome = input("Digite o nome do serviço: ")
                    resultados = servicos.pesquisar_nome(nome)
                    print(resultados)

                case 4:
                    id_servico = input("ID do serviço: ")
                    resultado = servicos.ler_um_servico(id_servico)
                    if len(resultado) == 0:
                        print("Serviço não encontrado.")
                    else:
                        print(resultado)

                case 5:
                    try:
                        coluna = input("Coluna a ser atualizada (nome, valor, id_categoria, duracao): ")
                        novo_valor = input("Novo valor: ")
                        id_servico = input("ID do serviço a ser atualizado: ")
                        servicos.atualizar_servico(coluna, novo_valor, id_servico)

                    except Exception as e:
                        print(f"Erro ao atualizar serviço: {e}")

                case 6:
                    id_servico = input("ID do serviço a ser deletado: ")
                    servicos.deletar_servico(id_servico)

                case 7:
                    input("Pressione Enter para voltar ao menu principal...")
                    continue

                case _:
                    print("Opção inválida. Tente novamente.")

    def display_opcao_agendas(self):
        input_opcao = 0
        agenda = agendas.Agenda()
        
        while input_opcao != 7:
            print("==============================" \
                  "1 - Listar agendas" \
                  "2 - Cadastrar agenda" \
                  "3 - Pesquisar agenda" \
                  "4 - Ver uma agenda" \
                  "5 - Atualizar agenda" \
                  "6 - Deletar agenda" \
                  "7 - Voltar")

            try:
                input_opcao = int(input("Escolha uma opção (1-7): "))
            except ValueError:
                print("Entrada inválida. Por favor, insira um número entre 1 e 7.")
                continue

            match input_opcao:
                case 1:
                    print("Listando Agendas...")
                    agenda.ler_toda_agenda()

                case 2:
                    try:
                        dia = input("Digite o dia da agenda:")
                        horario = input("Digite o horario da agenda:")
                        id_funcionario = input("Digite o id do funcionário:")
                        id_servico = input("Digite o id de servico")
                        agenda.cadastro_agenda(dia, horario, id_funcionario, id_servico, id_cliente, status='agendado')

                    except Exception as e:
                        print(f"Erro ao adicionar agenda: {e}")

                case 3:
                    nome = input("Digite o nome da agenda: ")
                    resultados = agenda.pesquisar_nome(nome)
                    print(resultados)

                case 4:
                    id_agenda = input("ID da agenda: ")
                    resultado = agenda.ler_uma_agenda(id_agenda)
                    if len(resultado) == 0:
                        print("Agenda não encontrada.")
                    else:
                        print(resultado)

                case 5:
                    try:
                        coluna = input("Coluna a ser atualizada (nome, data, hora): ")
                        novo_valor = input("Novo valor: ")
                        id_agenda = input("ID da agenda a ser atualizada: ")
                        agenda.atualizar_agenda(coluna, novo_valor, id_agenda)

                    except Exception as e:
                        print(f"Erro ao atualizar agenda: {e}")

                case 6:
                    id_agenda = input("ID da agenda a ser deletada: ")
                    agenda.deletar_agenda(id_agenda)

                case 7:
                    input("Pressione Enter para voltar ao menu principal...")
                    continue

                case _:
                    print("Opção inválida. Tente novamente.")

interface = Interface()
interface.display_menu()
