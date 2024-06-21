from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomUserLogin, CustomUserRegister


def home(request):
    context = {
        'title': 'Головна сторінка',
        'header': 'Привіт! Авторизуйтесь або пройдіть верифікацію.',
        'button_login': 'Залогінитись',
        'button_register': 'Зареєструватись',
    }
    return render(request, 'home.html', context)


def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserRegister()

    return render(request,'register.html', {'form': form})


def logout(request):
    return render(request, 'logout.html')

