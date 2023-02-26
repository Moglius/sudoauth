from django.urls import path, include

from .views import LDAPUserView, LDAPGroupView

urlpatterns = [
    path('users/', LDAPUserView.as_view(), name='ldapusers'),
    path('groups/', LDAPGroupView.as_view(), name='ldapgroups')
]