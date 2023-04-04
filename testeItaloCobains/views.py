from django.shortcuts import render, redirect, get_object_or_404
from .models import Sofa
from .forms import SofaForm

def produto_list(request):
    sofas = Sofa.objects.all()
    return render(request, 'testeItaloCobains/sofa_list.html', {'sofas': sofas})

def edit_sofa(request, produto_id):
    produto = get_object_or_404(Sofa, pk=produto_id)
    if request.method == 'POST':
        form = SofaForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('teste:produto_list')
    else:
        form = SofaForm(instance=produto)
    return render(request, 'testeItaloCobains/edit_produto.html', {'form': form})

def create_sofa(request):
    if request.method == 'POST':
        form = SofaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teste:produto_list')
    else:
        form = SofaForm()
    return render(request, 'testeItaloCobains/create_sofa.html', {'form': form})

def delete_sofa(request, produto_id):
    produto = get_object_or_404(Sofa, pk=produto_id)
    produto.delete()
    return redirect('teste:produto_list')