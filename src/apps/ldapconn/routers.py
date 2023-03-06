from rest_framework.routers import DefaultRouter
from .views import LDAPUserViewSet, LDAPGroupViewSet, LDAPSudoRuleViewSet


router = DefaultRouter()
router.register('ldapusers', LDAPUserViewSet, basename="ldapuser")
router.register('ldapgroups', LDAPGroupViewSet, basename="ldapgroups")
router.register('ldapsudorules', LDAPSudoRuleViewSet, basename="ldapsudorules")

urlpatterns = router.urls
