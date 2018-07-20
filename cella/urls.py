from django.conf.urls import include
from django.urls import path

from cella import views

urlpatterns = [
    path('', views.HomePageView.as_view()),
    path('about/', views.AboutPageView.as_view()), # Add this /about/ route
]