from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomUserRegister, CustomUserLogin
from django.contrib.auth import login, authenticate


def home(request):
    context = {
        'title': 'Головна сторінка',
        'header': 'Привіт! Авторизуйтесь або пройдіть реєстрацію.',
        'button_login': 'Залогінитись',
        'button_register': 'Зареєструватись',
    }
    return render(request, 'home.html', context)


def login_user(request):
    if request.method == 'POST':
        form = CustomUserLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home.html')
            else:
                form.add_error('Невірний логін або пароль!')
    else:
        form = CustomUserLogin()

    return render(request, 'login.html', {'form': form})


def register_user(request):
    if request.method == 'POST':
        form = CustomUserRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form.add_error('Якесь з полів заповнене невірно!')
    else:
        form = CustomUserRegister()

    return render(request,'register.html', {'form': form})


def logout(request):
    return render(request, 'logout.html')

