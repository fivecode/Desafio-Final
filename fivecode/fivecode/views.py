from django.shortcuts import render, redirect
from fivecode.forms import EmpresaForm
from fivecode.forms import ProdutoForm
from fivecode.models import Empresa
from fivecode.models import Produto

def home(request):
    data = {}
    data['db'] = Empresa.objects.all()
    return render (request, 'index.html', data)

def form (request):
    data = {}
    data["form"] = EmpresaForm()
    return render (request, "form.html", data)

def create (request):
    form = EmpresaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home") 

def view (request, pk_empresa):
    produtos = Produto.objects.filter(empresa=pk_empresa)
    pk_empresa = 1
    return render (request, 'listaprodutos.html', {'produtos' : produtos, ' pk_empresa' : pk_empresa})

def edit (request, pk):
    data = {}
    data ['db'] = Empresa.objects.get(pk=pk)
    data['form'] = EmpresaForm(instance=data['db'])  
    return render (request, 'form.html', data)      

def update (request, pk):
    data = {}
    data['db'] = Empresa.objects.get(pk=pk)
    form = EmpresaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('home')
  
def delete (request, pk):
    db = Empresa.objects.get(pk=pk)
    db.delete()
    return redirect ('home')

def formproduto(request, pk_empresa):
    data = {}
    data["formproduto"] = ProdutoForm()
    return render (request, "formproduto.html", data)

def createproduto (request, pk_empresa):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        produto = form.save(commit=False)
        produto.empresa.id = pk_empresa
        produto.save()
        return redirect("home") 

      
