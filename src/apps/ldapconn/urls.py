from django.urls import path, include

from .views import LDAPUserView

urlpatterns = [
    path('', LDAPUserView.as_view(), name='ldapusers')
]