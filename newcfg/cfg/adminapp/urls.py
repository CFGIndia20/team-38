from django.contrib import admin
from django.urls import path, re_path
from adminapp import views
app_name='adm'
urlpatterns = [
	
	path('session/',views.sessionadd,name='sessionadd'),
	path('task/',views.taskadd,name='taskadd'),
	path('progress/',views.progress,name="progress"),
	path('attendance/',views.attendance,name="attendance")
	
]