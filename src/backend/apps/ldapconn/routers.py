from rest_framework.routers import DefaultRouter
from .views import LDAPUserViewSet, LDAPGroupViewSet, LDAPSudoRuleViewSet


router = DefaultRouter()
router.register('ldapusers', LDAPUserViewSet, basename="ldapusers")
router.register('ldapgroups', LDAPGroupViewSet, basename="ldapgroups")
router.register('rules', LDAPSudoRuleViewSet, basename="rules")

urlpatterns = router.urls
