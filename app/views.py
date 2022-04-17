from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from app.forms import ProdutoForm
from app.models import Produto
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, 'index.html')

def produtos(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Produto.objects.filter(produto__icontains=search)
    else:
        data['db'] = Produto.objects.all()
    return render(request, 'produtos.html', data)

def form(request):
    data = {}
    data['form'] = ProdutoForm()
    return render(request, 'form.html', data)

def create(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('produtos')

def view(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    data['form'] = ProdutoForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    form = ProdutoForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('produtos')

def delete(request, pk):
    db = Produto.objects.get(pk=pk)
    db.delete()
    return redirect('produtos')