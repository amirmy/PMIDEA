from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserLoginForm, UserRegistrationForm, EditDashboardForm
from .models import User, Dashboard
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'logged in')
                return redirect('homed:home_index')
            else:
                messages.error(request, 'wrong username or password')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(email=cd['email'], password=cd['password'])
            user.save()
            login(request, user)
            messages.success(request, 'registered !!!')
            return redirect('home:home_index')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'logged out')
    return redirect('home:home_index')


def user_dashboard(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    dashboard = get_object_or_404(Dashboard, user=user)
    return render(request, 'accounts/user_dashboard.html', {'dashboard': dashboard})


def edit_dashboard(request, user_id):
    if request.user.id == user_id:
        dashboard = get_object_or_404(Dashboard, user__id=user_id)
        if request.method == 'POST':
            form = EditDashboardForm(request.POST, instance=dashboard)
            if form.is_valid():
                ed = form.save(commit=False)
                ed.user = request.user
                ed.save()
                messages.success(request, 'submitted successfully')
                return redirect('accounts:dashboard', request.user.id)
        else:
            form = EditDashboardForm(instance=dashboard)
        return render(request, 'accounts/edit_dashboard.html', {'form': form})
