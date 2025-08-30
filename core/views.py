from django.http import JsonResponse
#from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
#from .forms import ClienteForm  
from django.shortcuts import render, redirect

from funcoes.clientes import Clientes
from funcoes.funcionarios import Funcionario
from funcoes.produto import Produto
from funcoes.servico import Servico
from funcoes.agendas import Agenda
from funcoes.categoria import Categoria
from funcoes.disponibilidade import Disponibilidade
from funcoes.estoque import Estoque
from funcoes.pagamentos import Pagamento
from funcoes.compra import Compra
from funcoes.itens_compra import Itens_compra
from funcoes.utiliza import Utiliza


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
            # Cadastrar cliente
            c = Clientes()
            if c.cadastrar_cliente(nome, email, cpf, endereco, numero_celular):
                messages.success(request, 'Cliente cadastrado com sucesso!')
            else:
                 messages.success(request, 'erro')
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





def home(request):
    return render(request, 'core/home.html')

