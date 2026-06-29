from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            
            if user.is_superuser:
                return redirect("/admin/")

            if user.groups.filter(name="Admin").exists():
                return redirect("/admin/")

            elif user.groups.filter(name="Manager").exists():
                return redirect("/reports/")

            elif user.groups.filter(name="Staff").exists():
                return redirect("/sales/")

            else:
                return redirect("/")

        return render(
            request,
            "accounts/login.html",
            {"error": "Invalid Username or Password"}
        )

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("/login/")