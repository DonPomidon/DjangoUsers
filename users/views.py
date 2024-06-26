from django.shortcuts import render, redirect
from .forms import CustomUserRegister, CustomUserLogin
from django.contrib.auth import login, logout as auth_logout
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


@login_required
def user_check(request):
    user = request.user
    allowed_groups = ['IT', 'Marketing', 'Sales']
    in_allowed_groups = user.groups.filter(name__in=allowed_groups).exists()

    context = {
        'user': user,
        'in_allowed_groups': in_allowed_groups,
    }
    return render(request, 'product_list.html', context)


def home(request):
    context = {
        'title': 'Головна сторінка',
        'header': 'Вітаємо на нашому сайті!',
        'button_login': 'Залогінитись',
        'button_register': 'Зареєструватись',
        'button_logout': "Вийти",
        'product_list': "Продукти компанії",
    }
    return render(request, 'home.html', context)


def login_user(request):
    if request.method == 'POST':
        form = CustomUserLogin(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Невірний логін або пароль!')
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

    return render(request, 'register.html', {'form': form})


def logout_user(request):
    auth_logout(request)
    return redirect('home')


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


class ProductCreateView(CreateView):
    model = Product
    form_model = ProductForm
    fields = ('name', 'info', 'price')
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_model = ProductForm
    fields = ('name', 'info', 'price')
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    form_model = ProductForm
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

