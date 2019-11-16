from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import (
    UtilizadorRegistoForm,
    UtilizadorUpdateForm,
    PerfilUpdateForm
)


def registo(request):
    if request.method == 'POST':
        form = UtilizadorRegistoForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'A sua conta foi criada com sucesso. Pode começar a utilizar o mySchool!')
            return redirect('app-login')
    else:
        form = UtilizadorRegistoForm()
    return render(request, 'utilizadores/registo.html', {'form': form})


@login_required
def perfil(request):
    if request.method == 'POST':
        u_form = UtilizadorUpdateForm(request.POST, instance=request.user)
        p_form = PerfilUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, f'A sua conta foi atualizada!')
            return redirect('app-perfil')
    else:
        u_form = UtilizadorUpdateForm(instance=request.user)
        p_form = PerfilUpdateForm(instance=request.user.perfil)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'utilizadores/perfil.html', context)
