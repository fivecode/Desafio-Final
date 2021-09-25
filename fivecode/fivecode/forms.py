from django.forms import ModelForm
from fivecode.models import Empresa
from fivecode.models import Produto


class EmpresaForm(ModelForm):
     class Meta:
         model = Empresa
         fields = ['cnpj', 'nomeDaEmpresa', 'email', 'telefone']

class ProdutoForm(ModelForm):
     class Meta:
         model = Produto
         fields = ['nome', 'marca', 'preco', 'estoque']