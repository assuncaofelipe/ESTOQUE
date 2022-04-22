from pyexpat import model
from re import template
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from app.forms import ProdutoForm
from app.models import Produto
from django.core.paginator import Paginator
from django.db.models import Q

from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'index.html')

@login_required
def produtos(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Produto.objects.filter( Q(codigoProduto__icontains=search) | (Q(produto__icontains=search)) )
    else:
        data['db'] = Produto.objects.all()
    return render(request, 'produtos.html', data)

@login_required
def form(request):
    data = {}
    data['form'] = ProdutoForm()
    return render(request, 'form.html', data)

@login_required
def create(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('produtos')

@login_required
def view(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    return render(request, 'view.html', data)

@login_required
def edit(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    data['form'] = ProdutoForm(instance=data['db'])
    return render(request, 'form.html', data)

@login_required
def update(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    form = ProdutoForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('produtos')
        
@login_required
def delete(request, pk):
    db = Produto.objects.get(pk=pk)
    db.delete()
    return redirect('produtos')