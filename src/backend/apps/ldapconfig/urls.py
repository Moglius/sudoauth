from django.urls import include, path

urlpatterns = [
    path("", include("apps.ldapconfig.routers")),
]
