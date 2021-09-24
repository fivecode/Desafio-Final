from django.forms import ModelForm
from fivecode.models import Empresa


class EmpresaForm(ModelForm):
     class Meta:
         model = Empresa
         fields = ['cnpj', 'nomeDaEmpresa', 'email', 'telefone']