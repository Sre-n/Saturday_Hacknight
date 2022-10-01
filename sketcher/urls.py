from django.urls import path

from sketcher.views import home


urlpatterns = [
    path('',home,name="home")
]
