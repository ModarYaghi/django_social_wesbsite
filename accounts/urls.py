from django.urls import path

from .views import user_login

urlpatterns = [
    path("login/", viws.user_login, name="login"),
]
