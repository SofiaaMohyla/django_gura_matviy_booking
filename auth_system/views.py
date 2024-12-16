from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from auth_system.forms import CustomUserCreationForm, CustomUserAuthenticationForm
from django.contrib.auth import login, authenticate, logout

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
        messages.error(request, "Some error")
    return render(request, "auth_system/register.html", {"form": form})

def login_user(request):
    if request.method == "POST":
        form = CustomUserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            phone_number = form.cleaned_data.get("phone_number")
            user = authenticate(request, username=username, password=password)
            if user is not None and user.phone_number == phone_number:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Неправильний логін та пароль")
    else:
        form = CustomUserAuthenticationForm()
    return render(request, "auth_system/login.html", {"form": form})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')