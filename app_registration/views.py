from django.shortcuts import render, redirect
from app_registration.forms import CarsForm
from app_registration.models import Cars
from django.core.paginator import Paginator

def home(request):
    data = {}
    search = request.GET.get('search') #ainda está sendoimplementado a busca
    if search:
        data['db'] = Cars.objects.filter(modelo__icontains=search)
    else:
        data['db'] = Cars.objects.all()
    #data['db'] = Cars.objects.all()
    '''all = Cars.objects.all() #Está sendo implementado a paginação
    paginator = Paginator(all, 10)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)'''
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = CarsForm
    return render(request, 'form.html', data)


def create(request):
    form = CarsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    
def view(request, pk):
    data = {}
    data['db'] = Cars.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Cars.objects.get(pk=pk)
    data['form'] = CarsForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Cars.objects.get(pk=pk)
    form = CarsForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('home')


def delete(request, pk):
    db = Cars.objects.get(pk=pk)
    db.delete()
    return redirect('home')