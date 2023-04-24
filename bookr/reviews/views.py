from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    name = "world"
    return render(request, "base.html", {"name": name})


