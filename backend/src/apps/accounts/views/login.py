from django.contrib import auth, messages
from django.shortcuts import render, redirect

def login(request):
    if request.user.is_authenticated:
        return redirect("accounts:index_page")

    if request.method != "POST":
        return render(request, "accounts/login.html")

    phone_number = request.POST["phone_number"]
    password = request.POST["password"]
    if user := auth.authenticate(request, phone_number= phone_number, password=password):
        auth.login(request, user)
        messages.success(request, "You are now logged in")
        return redirect("accounts:index_page")
    messages.warning(request, "Invalid credentials")
    return redirect("accounts:login")
