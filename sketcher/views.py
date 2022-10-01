from django.shortcuts import render

from sketcher.forms import ImageForm

def home(request):
    form = ImageForm()
    return render(request,'home.html',{'form':form})
