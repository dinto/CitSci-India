from django.shortcuts import render

# Create your views here.
def CitiSci(request):
    return render(request,'index.html',{})