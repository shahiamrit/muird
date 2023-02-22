from django.shortcuts import render
from . models import Slider, Iru, Vmgo, About, Gallary
# Create your views here.

def home(request):
    data = Slider.objects.all()
    return render(request, 'index.html', {'data': data})


def IruView(request):
    data = Iru.objects.all()
    return render(request, 'iru.html', {'data': data})

def VmgoView(request):
    data = Vmgo.objects.all()
    return render(request, 'vmgo.html', {'data': data})

def aboutView(request):
    data = About.objects.all()
    return render(request, 'about.html', {'data': data})

def GallaryView(request):
    data = Gallary.objects.all()
    return render(request, 'gallery.html', {'data': data})