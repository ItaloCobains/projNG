from django.shortcuts import render
from .models import Sofa

def home(request):
    return render(request, 'washBudget/pages/home.html', context={    
    })


def enviarFormSofa(request):
    if request.method == 'POST':
        num_pessoas = request.POST.get('num-pessoas')
        modelo = request.POST.get('modelo')
        material = request.POST.get('material')
        servicos = request.POST.get('servicos')

        formsofa = Sofa(num_pessoas=num_pessoas, modelo=modelo, material=material, servicos=servicos)
        formsofa.save()

        return render(request, 'sucesso.html')