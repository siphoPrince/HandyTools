
from django.urls import path
from . import views

app_name = "EmployerSignIn"
urlpatterns = [
    path("", views.index, name="index")
]

