from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<center><h1>Hello World!</h1></center>")


def detail(request):
    return HttpResponse("<center><h1>Detail Page</h1><p>Ini halaman detail blog.</p></center>")