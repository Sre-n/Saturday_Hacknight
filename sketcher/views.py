from django.shortcuts import render
from django.core.files.storage import default_storage
from django.contrib import messages

from sketcher.forms import ImageForm
from sketcher.sketch import sketch


def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get("image")
            image_name = default_storage.save(image.name.strip(), image)
            image_url = default_storage.url(image_name)
            try:
                sketch("media/"+image_name)
                messages.success(request,"Sketch successful!!")
                return render(request,'home.html',{'form':form,'image_url':image_url})
            except:
                pass
        else:
            messages.warning(request,"Sketch failed!!")
    
    form = ImageForm()
    return render(request,'home.html',{'form':form})