from django.shortcuts import render
from app_registration.forms import CarsForm

def home(request):
    return render(request, 'index.html')

def form(request):
    data = {}
    data['form'] = CarsForm
    return render(request, 'form.html', data)
