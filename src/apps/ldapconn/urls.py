from django.urls import path, include

from .views import create_sudo_rule_view

urlpatterns = [
    path('add/', create_sudo_rule_view, name='ldapgroups'),
    path('', include('apps.ldapconn.routers')),
]
