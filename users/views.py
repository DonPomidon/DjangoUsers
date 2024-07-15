from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserRegister, CustomUserLogin
from django.contrib.auth import login, logout as auth_logout
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from .decorators import department_required


@login_required
@department_required('IT', 'Marketing', 'Sales')
def user_check(request):
    user = request.user
    allowed_groups = ['IT', 'Marketing', 'Sales']
    is_allowed_group = user.groups.filter(name__in=allowed_groups).exists()

    context = {
        'user': user,
        'is_allowed_group': is_allowed_group,
    }
    return render(request, 'product_list.html', context)


def home(request):
    return render(request, 'home.html')


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


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


@login_required
@department_required('IT', 'Marketing', 'Sales')
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})


@login_required
@department_required('IT', 'Marketing', 'Sales')
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})


@login_required
@department_required('IT', 'Marketing', 'Sales')
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})



