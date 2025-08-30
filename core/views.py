from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, redirect

from funcoes.clientes import Clientes
from funcoes.funcionarios import Funcionario
from funcoes.servico import Servico
from funcoes.agendas import Agenda
from funcoes.estoque import Estoque

def cliente_list_view(request):
    """View para template HTML que lista clientes do banco"""
    # Busca os clientes usando sua classe Clientes
    c = Clientes()
    clientes = c.ler_todos_clientes()
    
    # Passa os clientes para o template
    context = {
        'clientes': clientes
    }
    return render(request, 'core/cliente_list.html', context)

def listar_clientes(request):
    c = Clientes()
    dados = c.ler_todos_clientes()
    return JsonResponse(dados, safe=False)

def cadastrar_cliente(request):
    if request.method == 'POST':

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        endereco = request.POST.get('endereco')
        numero_celular = request.POST.get('numero_celular')
        
        if not nome:
            messages.error(request, 'Nome é obrigatório')
            return render(request, 'core/cadastrar_cliente.html')
        
        try:
            c = Clientes()

            c.cadastrar_cliente(nome, email, cpf, endereco, numero_celular)
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('cliente_list')
            
        except Exception as e:
            messages.error(request, f'Erro ao cadastrar: {str(e)}')
    
    return render(request, 'core/cadastro_cliente.html')

def atualizar_cliente(request):
    if request.method == 'POST':

        coluna = request.POST.get('coluna')
        novo_valor = request.POST.get('novo_valor')
        id = request.POST.get('id')
        
        try:
            c = Clientes()
            c.atualizar_cliente(coluna, novo_valor, id)
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect('cliente_list')
            
        except Exception as e:
            messages.error(request, f'Erro ao atualizar: {str(e)}')
    
    return render(request, 'core/atualizar_cliente.html')

def deletar_cliente(request):
    if request.method == 'POST':

        id = request.POST.get('id')
        
        try:
            c = Clientes()
            c.deletar_cliente(id)
            messages.success(request, 'Cliente deletado com sucesso!')
            return redirect('cliente_list')
            
        except Exception as e:
            messages.error(request, f'Erro ao deletar: {str(e)}')
    
    return render(request, 'core/deletar_cliente.html')

def cadastrar_funcionario(request):
    if request.method == 'POST':

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        endereco = request.POST.get('endereco')
        numero_celular = request.POST.get('numero_celular')
        salario = request.POST.get('salario')
        especialidade = request.POST.get('especialidade')
        
        if not nome:
            messages.error(request, 'Nome é obrigatório')
            return render(request, 'core/cadastro_funcionario.html')
            
        try:
            c = Funcionario()
            c.cadastrar_funcionario(nome, email, cpf, endereco, numero_celular, salario, especialidade)
            messages.success(request, 'Funcionario cadastrado com sucesso!')
            return redirect('home')
        
        except Exception as e:
            messages.error(request, f'Erro ao cadastrar: {str(e)}')
    
    return render(request, 'core/cadastro_funcionario.html')

def funcionario_list_view(request):

    """View para template HTML que lista clientes do banco"""
    # Busca os clientes usando sua classe Clientes
    f = Funcionario()
    funcionarios = f.ler_todos_funcionarios()
    
    # Passa os clientes para o template
    context = {
        'funcionarios': funcionarios
    }
    return render(request, 'core/funcionario_list.html', context)

def listar_funcionarios(request):
    f = Funcionario()
    dados = f.ler_todos_funcionarios()
    return JsonResponse(dados, safe=False)

def atualizar_funcionario(request):
    if request.method == 'POST':

        coluna = request.POST.get('coluna')
        novo_valor = request.POST.get('novo_valor')
        id = request.POST.get('id')
        
        try:
            c = Funcionario()
            c.atualizar_funcionario(coluna, novo_valor, id)
            messages.success(request, 'Funcionario atualizado com sucesso!')
            return redirect('listar_funcionarios')
            
        except Exception as e:
            messages.error(request, f'Erro ao atualizar: {str(e)}')
    
    return render(request, 'core/funcionario_atualizar.html')

def deletar_funcionario(request):
    if request.method == 'POST':

        id = request.POST.get('id')
        
        try:
            c = Funcionario()
            c.deletar_funcionario(id)
            messages.success(request, 'Funcionario deletado com sucesso!')
            return redirect('listar_funcionarios')
            
        except Exception as e:
            messages.error(request, f'Erro ao deletar: {str(e)}')
    
    return render(request, 'core/funcionario_deletar.html')

def cadastrar_agenda(request):
    if request.method == 'POST':
        dia = request.POST.get('dia')
        horario = request.POST.get('horario')
        id_funcionario = request.POST.get('id_funcionario')
        id_servico = request.POST.get('id_servico')
        id_cliente = request.POST.get('id_cliente')
        status = request.POST.get('status', 'agendado')  
        
        if not dia or not horario or not id_funcionario or not id_servico or not id_cliente:
            messages.error(request, 'Data, horário, ID do funcionário, ID do serviço e ID do cliente são obrigatórios!')
            return render(request, 'core/cadastrar_agenda.html')
        
        try:
            a = Agenda()
            a.cadastrar_agenda(
                dia=dia,
                horario=horario,
                id_funcionario=id_funcionario,
                id_servico=id_servico,
                id_cliente=id_cliente,
                status=status
            )
            messages.success(request, 'Agendamento cadastrado com sucesso!')
            return redirect('home')
            
        except Exception as e:
            messages.error(request, f'Erro ao agendar: {str(e)}')
            return render(request, 'core/agenda_cadastrar.html')
    
    return render(request, 'core/agenda_cadastrar.html')

def agenda_list_view(request):
    """View para template HTML que lista agendamentos do banco"""
    a = Agenda()
    agendas = a.ler_toda_agenda()
    
    # Passa os agendamentos para o template
    context = {
        'agendas': agendas
    }
    return render(request, 'core/agenda_list.html', context)

def atualizar_agenda(request):
    if request.method == 'POST':
        idagenda = request.POST.get('idagenda')
        coluna = request.POST.get('coluna')
        novo_valor = request.POST.get('novo_valor')
        
        if not idagenda or not coluna or not novo_valor:
            messages.error(request, 'Todos os campos são obrigatórios!')
            return render(request, 'core/agenda_atualizar.html')
        
        try:
            a = Agenda()
            a.atualizar_agenda(coluna, novo_valor, idagenda)
            messages.success(request, f'Agendamento {idagenda} atualizado com sucesso!')
            return redirect('lista_agenda')
            
        except Exception as e:
            messages.error(request, f'Erro ao atualizar agendamento: {str(e)}')
    
    return render(request, 'core/agenda_atualizar.html')

def deletar_agenda(request):
    if request.method == 'POST':
        idagenda = request.POST.get('idagenda')
        
        if not idagenda:
            messages.error(request, 'ID do agendamento é obrigatório!')
            return render(request, 'core/agenda_deletar.html')
        
        try:
            a = Agenda()
            a.deletar_agenda(idagenda)
            messages.success(request, f'Agendamento {idagenda} deletado com sucesso!')
            return redirect('lista_agenda')
            
        except Exception as e:
            messages.error(request, f'Erro ao deletar agendamento: {str(e)}')
    
    return render(request, 'core/agenda_deletar.html')

def servico_list_view(request):
    """View para listar serviços"""
    s = Servico()
    servicos = s.ler_todos_servicos()
    
    context = {
        'servicos': servicos
    }
    return render(request, 'core/servico_list.html', context)

def cadastrar_servico(request):
    if request.method == 'POST':
        nome_servico = request.POST.get('nome_servico')
        valor = request.POST.get('valor')
        id_categoria = request.POST.get('id_categoria')
        duracao = request.POST.get('duracao')
        
        if not nome_servico or not valor or not id_categoria or not duracao:
            messages.error(request, 'Todos os campos são obrigatórios!')
            return render(request, 'core/servico_cadastrar.html')
        
        try:
            s = Servico()
            s.cadastro_servico(nome_servico, valor, id_categoria, duracao)
            messages.success(request, 'Serviço cadastrado com sucesso!')
            return redirect('lista_servico')
            
        except Exception as e:
            messages.error(request, f'Erro ao cadastrar serviço: {str(e)}')
    
    return render(request, 'core/servico_cadastrar.html')

def atualizar_servico(request):
    if request.method == 'POST':
        idservico = request.POST.get('idservico')
        coluna = request.POST.get('coluna')
        novo_valor = request.POST.get('novo_valor')
        
        if not idservico or not coluna or not novo_valor:
            messages.error(request, 'Todos os campos são obrigatórios!')
            return render(request, 'core/servico_atualizar.html')
        
        try:
            s = Servico()
            s.atualizar_servico(coluna, novo_valor, idservico)
            messages.success(request, f'Serviço {idservico} atualizado com sucesso!')
            return redirect('lista_servico')
            
        except Exception as e:
            messages.error(request, f'Erro ao atualizar serviço: {str(e)}')
    
    return render(request, 'core/servico_atualizar.html')

def deletar_servico(request):
    if request.method == 'POST':
        idservico = request.POST.get('idservico')
        
        if not idservico:
            messages.error(request, 'ID do serviço é obrigatório!')
            return render(request, 'core/servico_deletar.html')
        
        try:
            s = Servico()
            s.deletar_servico(idservico)
            messages.success(request, f'Serviço {idservico} deletado com sucesso!')
            return redirect('lista_servico')
            
        except Exception as e:
            messages.error(request, f'Erro ao deletar serviço: {str(e)}')
    
    return render(request, 'core/servico_deletar.html')

def estoque_list_view(request):
    """View para listar estoque"""
    e = Estoque()
    estoques = e.ler_todo_estoque()
    
    context = {
        'estoques': estoques
    }
    return render(request, 'core/estoque_list.html', context)

def cadastrar_estoque(request):
    if request.method == 'POST':
        id_produto = request.POST.get('id_produto')
        quantidade_atual = request.POST.get('quantidade_atual')
        quantidade_minima = request.POST.get('quantidade_minima')
        
        if not id_produto or not quantidade_atual or not quantidade_minima:
            messages.error(request, 'Todos os campos são obrigatórios!')
            return render(request, 'core/estoque_cadastrar.html')
        
        try:
            e = Estoque()
            e.cadastro_estoque(id_produto, quantidade_atual, quantidade_minima)
            messages.success(request, 'Item adicionado ao estoque com sucesso!')
            return redirect('lista_estoque')
            
        except Exception as e:
            messages.error(request, f'Erro ao adicionar item: {str(e)}')
    
    return render(request, 'core/estoque_cadastrar.html')

def atualizar_estoque(request):
    if request.method == 'POST':
        idestoque = request.POST.get('idestoque')
        coluna = request.POST.get('coluna')
        novo_valor = request.POST.get('novo_valor')
        
        if not idestoque or not coluna or not novo_valor:
            messages.error(request, 'Todos os campos são obrigatórios!')
            return render(request, 'core/estoque_atualizar.html')
        
        try:
            e = Estoque()
            e.atualizar_estoque(coluna, novo_valor, idestoque)
            messages.success(request, f'Estoque {idestoque} atualizado com sucesso!')
            return redirect('lista_estoque')
            
        except Exception as e:
            messages.error(request, f'Erro ao atualizar estoque: {str(e)}')
    
    return render(request, 'core/estoque_atualizar.html')

def deletar_estoque(request):
    if request.method == 'POST':
        idestoque = request.POST.get('idestoque')
        
        if not idestoque:
            messages.error(request, 'ID do estoque é obrigatório!')
            return render(request, 'core/estoque_deletar.html')
        
        try:
            e = Estoque()
            e.deletar_estoque(idestoque)
            messages.success(request, f'Item {idestoque} removido do estoque com sucesso!')
            return redirect('lista_estoque')
            
        except Exception as e:
            messages.error(request, f'Erro ao remover item: {str(e)}')
    
    return render(request, 'core/estoque_deletar.html')

def home(request):
    return render(request, 'core/home.html')

