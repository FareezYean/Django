from django.shortcuts import render

# Create your views here.

def santri_home(request):
    return render(request, "profile_home.html")

def biodata(request):
    return render(request, "biodata.html")

def jadwal(request):
    return render(request, "jadwal.html")

def galeri(request):
    return render(request, "galeri.html")

def feedback(request):
    return render(request, "feedback.html")