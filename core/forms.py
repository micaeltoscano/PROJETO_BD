from django import forms
# from clientes import Clientes
# from funcoes.funcionarios import Funcionario
# from funcoes.produto import Produto
# from funcoes.servico import Servico
# from funcoes.agendas import Agenda
# from funcoes.categoria import Categoria
# from funcoes.disponibilidade import Disponibilidade
# from funcoes.estoque import Estoque
# from funcoes.pagamentos import Pagamento
# from funcoes.compra import Compra
# from funcoes.itens_compra import Itens_compra
# from funcoes.utiliza import Utiliza


# class ClienteForm(forms.ModelForm):
#     class Meta:
#         model = Clientes
#         fields = ['nome', 'email', 'cpf', 'endereco', 'numero_celular']
#         widgets = {
#             'nome': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Nome completo'
#             }),
#             'email': forms.EmailInput(attrs={
#                 'class': 'form-control', 
#                 'placeholder': 'email@exemplo.com'
#             }),
#             'cpf': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': '000.000.000-00'
#             }),
#             'endereco': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'rows': 3,
#                 'placeholder': 'Endereço completo'
#             }),
#             'numero_celular': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': '(11) 99999-9999'
#             }),
#         }
#         labels = {
#             'numero_celular': 'Número de Celular',
#         }

# class FuncionarioForm(forms.ModelForm):
#     class Meta:
#         model = Funcionario
#         fields = ['nome', 'email', 'cpf', 'endereco', 'numero_celular', 'salario', 'especialidade']
#         widgets = {
#             'nome': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'cpf': forms.TextInput(attrs={'class': 'form-control'}),
#             'endereco': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
#             'numero_celular': forms.TextInput(attrs={'class': 'form-control'}),
#             'salario': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
#             'especialidade': forms.TextInput(attrs={'class': 'form-control'}),
#         }

# class ServicoForm(forms.ModelForm):
#     class Meta:
#         model = Servico
#         fields = ['nome', 'valor', 'duracao', 'categoria']
#         widgets = {
#             'nome': forms.TextInput(attrs={'class': 'form-control'}),
#             'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
#             'duracao': forms.NumberInput(attrs={'class': 'form-control'}),
#             'categoria': forms.Select(attrs={'class': 'form-control'}),
#         }

# class AgendaForm(forms.ModelForm):
#     class Meta:
#         model = Agenda
#         fields = ['cliente', 'funcionario', 'servico', 'dia', 'horario', 'status']
#         widgets = {
#             'cliente': forms.Select(attrs={'class': 'form-control'}),
#             'funcionario': forms.Select(attrs={'class': 'form-control'}),
#             'servico': forms.Select(attrs={'class': 'form-control'}),
#             'dia': forms.DateInput(attrs={
#                 'class': 'form-control',
#                 'type': 'date'
#             }),
#             'horario': forms.TimeInput(attrs={
#                 'class': 'form-control', 
#                 'type': 'time'
#             }),
#             'status': forms.Select(attrs={'class': 'form-control'}),
#         }

# class ProdutoForm(forms.ModelForm):
#     class Meta:
#         model = Produto
#         fields = ['nome', 'valor', 'tipo']
#         widgets = {
#             'nome': forms.TextInput(attrs={'class': 'form-control'}),
#             'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
#             'tipo': forms.Select(attrs={'class': 'form-control'}),
#         }

# class CategoriaForm(forms.ModelForm):
#     class Meta:
#         model = Categoria
#         fields = ['nome_categoria']
#         widgets = {
#             'nome_categoria': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Nome da categoria'
#             }),
#         }