from django.urls import path
from . import views

app_name="LandingPage"
urlpatterns = [
    path("", views.LandingPage, name="LandingPage"),
]

