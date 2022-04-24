from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from .models import achieve
from rest_framework import viewsets
from .serializer import achieveSerializer


class achieveAPI(viewsets.ModelViewSet):
    queryset = achieve.objects.all().order_by('name')
    serializer_class = achieveSerializer


def MainView(request):
    return render(request, 'main.html')


def profile(request):
    achieves = achieve.objects.all()
    return render(request, 'profile.html', context= {'achievements': achieves})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Вы успешно зарегистрировались!')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'registration.html', {'form': form})


def add_achieve(request):
    return render(request, 'add_achievements.html')