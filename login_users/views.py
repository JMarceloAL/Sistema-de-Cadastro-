# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Usuarios
import secrets


def auth_view(request):

    if request.method == 'POST':

        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        print(
            f"🔵 Nome: {nome}, Senha recebida: {'*' * len(senha) if senha else 'None'}")

        # REGISTER
        if 'register' in request.POST:

            if Usuarios.objects.filter(nome_usuario=nome).exists():
                return render(
                    request,
                    'login_users.html',
                    {'error': 'Usuário já existe! Escolha outro nome.'}
                )

            Usuarios.objects.create(
                nome_usuario=nome,
                senha_hash=make_password(senha)
            )

            return render(
                request,
                'login_users.html',
                {'success': f'Usuário "{nome}" criado com sucesso! Agora faça login.'}
            )

        # LOGIN
        if 'login' in request.POST:

            try:
                usuario = Usuarios.objects.get(nome_usuario=nome)
                print(f"🟢 Usuário encontrado: {usuario.nome_usuario}")
            except Usuarios.DoesNotExist:

                return render(
                    request,
                    'login_users.html',
                    {'error': 'Usuário não encontrado!'}
                )

            if check_password(senha, usuario.senha_hash):

                token = secrets.token_urlsafe(32)

                request.session['usuario_id'] = usuario.id
                request.session['usuario_nome'] = usuario.nome_usuario
                request.session['token'] = token

                return redirect('system')
            else:

                return render(
                    request,
                    'login_users.html',
                    {'error': 'Senha incorreta!'}
                )

    return render(request, 'login_users.html')


# logout view

def logout_view(request):
    request.session.flush()  # Limpa toda a sessão
    return redirect('login_users')
