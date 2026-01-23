from django.shortcuts import render, redirect
from login_users.decorators import login_required
from .models import Cadastroclientes
# Create your views here.


@login_required  # ← Adicione este decorator
def system_view(request):
    usuario_nome = request.session.get('usuario_nome')
    token = request.session.get('token')

    return render(request, 'system.html', {
        'clients': Cadastroclientes.objects.all(),

        'usuario_nome': usuario_nome,
        'token': token

    })
