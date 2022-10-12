from django.shortcuts import render

# Create your views here.
def CitiSci(request):
    return render(request,'index.html',{})
def Cit(request):
    return render(request,'CitSci.html',{})

def tools(request):
    return render(request,'tools.html',{})
def projects(request):
    return render(request,'projects.html',{})
def training(request):
    return render(request,'training.html',{})
def bibliography(request):
    return render(request,'bibliography.html',{})    