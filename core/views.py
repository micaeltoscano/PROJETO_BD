from django.http import JsonResponse
#from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
#from django.contrib import messages
#from .forms import ClienteForm  
from django.shortcuts import render

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



# =============================================================================
# CLASS-BASED VIEWS (CBVs) - RECOMENDADO PARA TEMPLATES
# =============================================================================

# class ClienteListView(ListView):
#     model = Cliente
#     template_name = 'core/cliente_list.html'
#     context_object_name = 'clientes'
#     ordering = ['nome']




# =============================================================================
# CLIENTES
# =============================================================================
def listar_clientes(request):
    c = Clientes()
    dados = c.ler_todos_clientes()
    return JsonResponse(dados, safe=False)

def cadastrar_cliente(request):
    nome = request.GET.get('nome')
    email = request.GET.get('email')
    cpf = request.GET.get('cpf')
    endereco = request.GET.get('endereco')
    numero_celular = request.GET.get('numero_celular')

    c = Clientes()
    c.cadastrar_cliente(nome, email, cpf, endereco, numero_celular)
    return JsonResponse({"status": "sucesso"})

def atualizar_cliente(request):
    idcliente = request.GET.get('id')
    coluna = request.GET.get('coluna')
    valor = request.GET.get('valor')

    c = Clientes()
    c.atualizar_cliente(coluna, valor, idcliente)
    return JsonResponse({"status": "sucesso"})

def deletar_cliente(request):
    idcliente = request.GET.get('id')
    c = Clientes()
    c.deletar_cliente(idcliente)
    return JsonResponse({"status": "sucesso"})

# =============================================================================
# FUNCIONÁRIOS
# =============================================================================
def listar_funcionarios(request):
    f = Funcionario()
    dados = f.ler_todos_funcionarios()
    return JsonResponse(dados, safe=False)

def cadastrar_funcionario(request):
    nome = request.GET.get('nome')
    email = request.GET.get('email')
    cpf = request.GET.get('cpf')
    endereco = request.GET.get('endereco')
    numero_celular = request.GET.get('numero_celular')
    salario = request.GET.get('salario')
    especialidade = request.GET.get('especialidade')

    f = Funcionario()
    f.cadastrar_funcionario(nome, email, cpf, endereco, numero_celular, salario, especialidade)
    return JsonResponse({"status": "sucesso"})

def atualizar_funcionario(request):
    idfuncionario = request.GET.get('id')
    coluna = request.GET.get('coluna')
    valor = request.GET.get('valor')

    f = Funcionario()
    f.atualizar_funcionario(coluna, valor, idfuncionario)
    return JsonResponse({"status": "sucesso"})

def deletar_funcionario(request):
    idfuncionario = request.GET.get('id')
    f = Funcionario()
    f.deletar_funcionario(idfuncionario)
    return JsonResponse({"status": "sucesso"})

# =============================================================================
# PRODUTOS
# =============================================================================
def listar_produtos(request):
    p = Produto()
    dados = p.ler_todos_produtos()
    return JsonResponse(dados, safe=False)

def cadastrar_produto(request):
    valor = request.GET.get('valor')
    nome = request.GET.get('nome')
    tipo = request.GET.get('tipo')

    p = Produto()
    p.cadastro_produto(valor, nome, tipo)
    return JsonResponse({"status": "sucesso"})

def atualizar_produto(request):
    idproduto = request.GET.get('id')
    coluna = request.GET.get('coluna')
    valor = request.GET.get('valor')

    p = Produto()
    p.atualizar_produto(coluna, valor, idproduto)
    return JsonResponse({"status": "sucesso"})

def deletar_produto(request):
    idproduto = request.GET.get('id')
    p = Produto()
    p.deletar_produto(idproduto)
    return JsonResponse({"status": "sucesso"})

# =============================================================================
# SERVIÇOS
# =============================================================================
def listar_servicos(request):
    s = Servico()
    dados = s.ler_todos_servicos()
    return JsonResponse(dados, safe=False)

def cadastrar_servico(request):
    nome_servico = request.GET.get('nome_servico')
    valor = request.GET.get('valor')
    id_categoria = request.GET.get('id_categoria')
    duracao = request.GET.get('duracao')

    s = Servico()
    s.cadastro_servico(nome_servico, valor, id_categoria, duracao)
    return JsonResponse({"status": "sucesso"})

def atualizar_servico(request):
    idservico = request.GET.get('id')
    coluna = request.GET.get('coluna')
    valor = request.GET.get('valor')

    s = Servico()
    s.atualizar_servico(coluna, valor, idservico)
    return JsonResponse({"status": "sucesso"})

def deletar_servico(request):
    idservico = request.GET.get('id')
    s = Servico()
    s.deletar_servico(idservico)
    return JsonResponse({"status": "sucesso"})

# =============================================================================
# CATEGORIAS
# =============================================================================
def listar_categorias(request):
    cat = Categoria()
    dados = cat.ler_todas_categorias()
    return JsonResponse(dados, safe=False)

def cadastrar_categoria(request):
    nome_categoria = request.GET.get('nome_categoria')

    cat = Categoria()
    cat.cadastro_categoria(nome_categoria)
    return JsonResponse({"status": "sucesso"})

def atualizar_categoria(request):
    idcategoria = request.GET.get('id')
    coluna = request.GET.get('coluna')
    valor = request.GET.get('valor')

    cat = Categoria()
    cat.atualizar_categoria(coluna, valor, idcategoria)
    return JsonResponse({"status": "sucesso"})

def deletar_categoria(request):
    idcategoria = request.GET.get('id')
    cat = Categoria()
    cat.deletar_categoria(idcategoria)
    return JsonResponse({"status": "sucesso"})

# =============================================================================
# AGENDA
# =============================================================================
def listar_agendas(request):
    a = Agenda()
    dados = a.ler_toda_agenda()
    return JsonResponse(dados, safe=False)

def cadastrar_agenda(request):
    dia = request.GET.get('dia')
    horario = request.GET.get('horario')
    id_funcionario = request.GET.get('id_funcionario')
    id_servico = request.GET.get('id_servico')
    id_cliente = request.GET.get('id_cliente')
    status = request.GET.get('status', 'agendado')

    a = Agenda()
    a.cadastrar_agenda(dia, horario, id_funcionario, id_servico, id_cliente, status)
    return JsonResponse({"status": "sucesso"})

def atualizar_agenda(request):
    idagenda = request.GET.get('id')
    coluna = request.GET.get('coluna')
    valor = request.GET.get('valor')

    a = Agenda()
    a.atualizar_agenda(coluna, valor, idagenda)
    return JsonResponse({"status": "sucesso"})

def deletar_agenda(request):
    idagenda = request.GET.get('id')
    a = Agenda()
    a.deletar(idagenda)
    return JsonResponse({"status": "sucesso"})

# =============================================================================
# DISPONIBILIDADE
# =============================================================================
def listar_disponibilidades(request):
    d = Disponibilidade()
    dados = d.ler_todas_disponibilidades()
    return JsonResponse(dados, safe=False)

def cadastrar_disponibilidade(request):
    id_funcionario = request.GET.get('id_funcionario')
    dia_semana = request.GET.get('dia_semana')
    hora_inicio = request.GET.get('hora_inicio')
    hora_fim = request.GET.get('hora_fim')

    d = Disponibilidade()
    d.cadastro_disponibilidade(id_funcionario, dia_semana, hora_inicio, hora_fim)
    return JsonResponse({"status": "sucesso"})

def atualizar_disponibilidade(request):
    iddisponibilidade = request.GET.get('id')
    coluna = request.GET.get('coluna')
    valor = request.GET.get('valor')

    d = Disponibilidade()
    d.atualizar_disponibilidade(coluna, valor, iddisponibilidade)
    return JsonResponse({"status": "sucesso"})

def deletar_disponibilidade(request):
    iddisponibilidade = request.GET.get('id')
    d = Disponibilidade()
    d.deletar_disponibilidade(iddisponibilidade)
    return JsonResponse({"status": "sucesso"})

# =============================================================================
# ESTOQUE
# =============================================================================
def listar_estoques(request):
    e = Estoque()
    dados = e.ler_todo_estoque()
    return JsonResponse(dados, safe=False)

def cadastrar_estoque(request):
    id_produto = request.GET.get('id_produto')
    quantidade_atual = request.GET.get('quantidade_atual')
    quantidade_minima = request.GET.get('quantidade_minima')

    e = Estoque()
    e.cadastro_estoque(id_produto, quantidade_atual, quantidade_minima)
    return JsonResponse({"status": "sucesso"})

def atualizar_estoque(request):
    idestoque = request.GET.get('id')
    coluna = request.GET.get('coluna')
    valor = request.GET.get('valor')

    e = Estoque()
    e.atualizar_estoque(coluna, valor, idestoque)
    return JsonResponse({"status": "sucesso"})

def deletar_estoque(request):
    idestoque = request.GET.get('id')
    e = Estoque()
    e.deletar_estoque(idestoque)
    return JsonResponse({"status": "sucesso"})

# =============================================================================
# PAGAMENTOS
# =============================================================================
def listar_pagamentos(request):
    pag = Pagamento()
    dados = pag.ler_todos_pagamentos()
    return JsonResponse(dados, safe=False)

def atualizar_pagamento(request):
    idpagamento = request.GET.get('id')
    coluna = request.GET.get('coluna')
    valor = request.GET.get('valor')

    pag = Pagamento()
    pag.atualizar_pagamento(coluna, valor, idpagamento)
    return JsonResponse({"status": "sucesso"})

def deletar_pagamento(request):
    idpagamento = request.GET.get('id')
    pag = Pagamento()
    pag.deletar_pagamento(idpagamento)
    return JsonResponse({"status": "sucesso"})

# =============================================================================
# COMPRAS
# =============================================================================
def listar_compras(request):
    comp = Compra()
    dados = comp.ler_todas_compras()
    return JsonResponse(dados, safe=False)

def atualizar_compra(request):
    idcompra = request.GET.get('id')
    coluna = request.GET.get('coluna')
    valor = request.GET.get('valor')

    comp = Compra()
    comp.atualizar_compra(coluna, valor, idcompra)
    return JsonResponse({"status": "sucesso"})

def deletar_compra(request):
    idcompra = request.GET.get('id')
    comp = Compra()
    comp.deletar_compra(idcompra)
    return JsonResponse({"status": "sucesso"})

# =============================================================================
# ITENS COMPRA
# =============================================================================
def listar_itens_compra(request):
    ic = Itens_compra()
    dados = ic.ler_todos_itens_compra()
    return JsonResponse(dados, safe=False)

# =============================================================================
# UTILIZA
# =============================================================================
def listar_utiliza(request):
    u = Utiliza()
    dados = u.ler_todos_utiliza()
    return JsonResponse(dados, safe=False)

def cadastrar_utiliza(request):
    id_servico = request.GET.get('id_servico')
    id_produto = request.GET.get('id_produto')
    quantidade = request.GET.get('quantidade')

    u = Utiliza()
    u.cadastro_utiliza(id_servico, id_produto, quantidade)
    return JsonResponse({"status": "sucesso"})

def atualizar_utiliza(request):
    idutiliza = request.GET.get('id')
    coluna = request.GET.get('coluna')
    valor = request.GET.get('valor')

    u = Utiliza()
    u.atualizar_utiliza(coluna, valor, idutiliza)
    return JsonResponse({"status": "sucesso"})

def deletar_utiliza(request):
    idutiliza = request.GET.get('id')
    u = Utiliza()
    u.deletar_utiliza(idutiliza)
    return JsonResponse({"status": "sucesso"})

def home(request):
    return render(request, 'core/home.html')

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