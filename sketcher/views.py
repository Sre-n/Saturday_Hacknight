from django.shortcuts import render
from django.core.files.storage import default_storage
from django.contrib import messages

from sketcher.forms import ImageForm
from sketcher.sketch import sketch

import numpy as np
import cv2

from PIL import Image

def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get("image")
            file_name = default_storage.save(image.name, image)
            fh = default_storage.open(file_name, "w")
            img = cv2.imdecode(np.fromstring(fh.read(), np.uint8), cv2.IMREAD_UNCHANGED)
            sketched_img = sketch(img)
            final_img = Image.fromarray(sketched_img)
            fh = default_storage.save(file_name, final_img)
            fh.close()
            image_url = default_storage.url(file_name)
            print(image_url)
            try:
                messages.success(request,"Sketch successful!!")
                return render(request,'home.html',{'form':form,'image_url':image_url})
            except:
                pass
        else:
            messages.warning(request,"Sketch failed!!")
    
    form = ImageForm()
    return render(request,'home.html',{'form':form})
