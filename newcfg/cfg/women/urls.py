from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.womendetail),
    path('progression/',views.progressiondetail),
    path('show/',views.progressionshow)
]