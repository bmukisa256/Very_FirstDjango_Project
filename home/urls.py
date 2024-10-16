from django.urls import path 

from . import views

urlpatterns = [
    path('home', views.HomeView.as_view()),
    path('authorization', views.AuthorizationView.as_view())
]