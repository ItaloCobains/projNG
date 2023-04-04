from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.http import Http404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'authors/pages/register_view.html', {
        'form': form,
        'form_action': reverse('ng:criar_registro')
    })


def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Seu usuário foi criado, faça o login.')
        del(request.session['register_form_data'])
        return redirect(reverse('ng:login'))
    return redirect('ng:registro')


def login_view(request):
    form = LoginForm()
    return render(request, 'authors/pages/login_view.html', {
        'form': form,
        'form_action': reverse('ng:criar_login'),
    })


def login_create(request):
    if not request.POST:
        raise Http404()
    form = LoginForm(request.POST)

    if form.is_valid():
        is_authenticated = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if is_authenticated is not None:
            if not request.user.is_authenticated:
                messages.success(request, 'Você está logado.')
            login(request, is_authenticated)
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
            return redirect(reverse('ng:login'))

    else:
        messages.error(request, 'Erro ao validar dados do formulário.')
        return redirect(reverse('ng:registro'))
    return redirect(reverse('link:home'))


@login_required(login_url='ng:login', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        return redirect(reverse('ng:login'))
        
    if request.POST.get('username') != request.user.username:
        return redirect(reverse('ng:login'))

    logout(request)
    return redirect(reverse('link:home'))