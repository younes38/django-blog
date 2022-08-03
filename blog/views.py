from django.http import HttpResponse
from django.shortcuts import render


def articles_list(request):
    return render(request, "home_page.html")


def home(request):
    return render(request, "home_page.html")


def about(request):
    return render(request, "about_page.html")
