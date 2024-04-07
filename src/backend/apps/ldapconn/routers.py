from rest_framework.routers import DefaultRouter

from .views import (
    LDAPGroupViewSet,
    LDAPNisNetgroupViewSet,
    LDAPSudoRuleViewSet,
    LDAPUserViewSet,
)

router = DefaultRouter()
router.register("ldapusers", LDAPUserViewSet, basename="ldapusers")
router.register("ldapgroups", LDAPGroupViewSet, basename="ldapgroups")
router.register("rules", LDAPSudoRuleViewSet, basename="rules")
router.register("netgroups", LDAPNisNetgroupViewSet, basename="netgroups")

urlpatterns = router.urls
