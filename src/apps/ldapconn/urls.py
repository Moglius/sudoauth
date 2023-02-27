from django.urls import path, include

from .views import LDAPUserView, LDAPGroupView, create_sudo_rule_view

urlpatterns = [
    path('users/', LDAPUserView.as_view(), name='ldapusers'),
    path('groups/', LDAPGroupView.as_view(), name='ldapgroups'),
    path('add/', create_sudo_rule_view, name='ldapgroups'),
]