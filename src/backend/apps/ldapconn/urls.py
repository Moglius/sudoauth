from django.urls import include, path

urlpatterns = [
    path("", include("apps.ldapconn.routers")),
]
