from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def register(request):
    if request.method == "POST":
        data = UserCreationForm(request.POST)

        if data.is_valid():
            data.save()
            return redirect("home:home_view")
        else:
            return redirect("home:about_view")
    context = {
        "name":"olaVicky",
        "emails":"olavicky@gmail.com",
        "gender":"female",
        "form": UserCreationForm()
    }
    return render(request, "account/register.html", context)


def login(request):
    if request.method == "POST":
        data = UserCreationForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect("home:home_view")
        else:

            return redirect("home:about_view")
    context = {
        "name": "olaVicky",
        "emails": "olavicky@gmail.com",
        "gender": "female",
        "form": UserCreationForm()
    }
    return render(request, "accounts/login.html", context)

