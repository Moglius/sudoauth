from rest_framework.routers import DefaultRouter
from .views import (SudoRuleViewSet, SudoCommandViewSet,
    SudoHostViewSet, SudoCommandRoleViewSet, SudoHostGroupViewSet)


router = DefaultRouter()
router.register('rules', SudoRuleViewSet, basename="rule")
router.register('commands', SudoCommandViewSet, basename="command")
router.register('roles', SudoCommandRoleViewSet, basename="role")
router.register('hosts', SudoHostViewSet, basename="hosts")
router.register('netgroups', SudoHostGroupViewSet, basename="netgroup")

urlpatterns = router.urls
