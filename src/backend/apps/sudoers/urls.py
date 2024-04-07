from django.urls import include, path

urlpatterns = [
    path("", include("apps.sudoers.routers")),
]
