from django.urls import path 

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),  # Root URL mapped to HomeView
    path('home', views.HomeView.as_view()),
    path('authorization', views.AuthorizationView.as_view())
]