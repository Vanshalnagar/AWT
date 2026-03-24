from . import views

from django.urls import path

urlpatterns = [
    path('home', views.homepage),
    path('about', views.aboutpage),
    path('cake', views.aboutpage),
    path('cake/surat', views.aboutpage),
    path('cake/<int:id>', views.aboutpage),

]