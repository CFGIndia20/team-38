from django.urls import path,re_path
from home import views

from django.conf.urls import url

urlpatterns = [

    path('signup/', views.register, name='signup'),


    # path('password_reset/',auth_views.password_reset, name='password_reset'),
    # path('password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    # re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # path('reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),


    ]