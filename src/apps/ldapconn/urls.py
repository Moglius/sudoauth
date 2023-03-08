from django.urls import path, include

from .views import create_sudo_rule_view, get_notused_id

urlpatterns = [
    path('getid/', get_notused_id, name='get_notused_id'),
    path('add/', create_sudo_rule_view, name='ldapgroups'),
    path('', include('apps.ldapconn.routers')),
]
