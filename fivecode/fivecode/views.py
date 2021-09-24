from django.shortcuts import render, redirect
from fivecode.forms import EmpresaForm
from fivecode.models import Empresa

def home(request):
    data = {}
    data["db"] = Empresa.objects.all()
    return render (request, 'index.html', data)

def form (request):
    data = {}
    data["form"] = EmpresaForm()
    return render (request, "cadastroempresa.html", data)

def create (request):
    form = EmpresaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")    
