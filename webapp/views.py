from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect



"""

1. Landing
2. Login
3. Dashboard
4. Logout
5. SetPassword
6. AddInfo
7. More

"""

def landing(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello")


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse("login")


def dashboard(request: HttpRequest) -> HttpResponse:
    return HttpResponse("dashboard")


