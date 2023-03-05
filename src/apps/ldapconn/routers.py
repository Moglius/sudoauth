from rest_framework.routers import DefaultRouter
from .views import LDAPUserViewSet, LDAPGroupViewSet


router = DefaultRouter()
router.register('ldapusers', LDAPUserViewSet, basename="ldapuser")
router.register('ldapgroups', LDAPGroupViewSet, basename="ldapgroups")

urlpatterns = router.urls
