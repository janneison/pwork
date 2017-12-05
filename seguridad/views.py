# Create your views here.
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect

from django.db import models

from seguridad.models import User, Trabajo

from .forms import PostForm

# Create your views here.
@login_required
def index_view(request):
    return render(request, 'usuario/index.html')

def login_view(request):
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    if request.user.is_authenticated:
        return redirect(reverse('seguridad.index'))

    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('seguridad.index'))
            else:
                mensaje = 'Cuenta inactiva'
        mensaje = 'Nombre de usuario o clave no valido'
    return render(request, 'usuario/login.html', {'mensaje': mensaje})


def logout_view(request):
	logout(request)
	messages.success(request, 'Te has desconectado con exito')
	return redirect(reverse('seguridad.login')) 

@login_required
def profile_view(request):
    return render(request, 'usuario/base_usuario.html')

@login_required
def trabajo_list(request):
    if request.user.cargo == "3":
        trabajos = Trabajo.objects.filter(creador=request.user).order_by('fecha')
    else:
        trabajos = Trabajo.objects.all().order_by('fecha')
    return render(request, 'usuario/trabajo_list.html', {'trabajos':trabajos})

def trabajo_detail(request, pk):
    trabajo = get_object_or_404(Trabajo, pk=pk)
    return render(request, 'usuario/trabajo_detail.html', {'trabajo': trabajo})

def trabajo_new(request):
    if request.method == "POST":
       form = PostForm(request.POST)
       if form.is_valid():
           trabajo = form.save(commit=False)
           trabajo.creador = request.user
           trabajo.save()
           return redirect('trabajo_detail', pk=trabajo.pk)
    else:
        form = PostForm()
    return render(request, 'usuario/trabajo_edit.html', {'form': form})

def trabajo_edit(request, pk):
    trabajo = get_object_or_404(Trabajo, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            trabajo = form.save(commit=False)
            trabajo.creador = request.user
            post.save()
            return redirect('trabajo_detail', pk=trabajo.pk)
    else:
        form = PostForm(instance=trabajo)
    return render(request, 'usuario/trabajo_edit.html', {'form': form})