from django.urls import path

from .views import CustomAuthToken

urlpatterns = [path("auth/", CustomAuthToken.as_view())]
