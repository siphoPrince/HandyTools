from django.urls import path
from . import views


app_name='EmployerSignUp'
urlpatterns = [
    path("", views.index, name="index"),
]
