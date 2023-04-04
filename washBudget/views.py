from django.shortcuts import render
from .forms import SofaForm



def home(request):
    return render(request, 'washBudget/pages/home.html', context={    
    })


def orcamento_sofa(request):
    form = SofaForm()
    return render(request, 'washBudget/pages/home.html', {'form': form})
