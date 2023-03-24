from rest_framework.routers import DefaultRouter
from .views import (SudoRuleViewSet, SudoCommandViewSet,
    SudoHostViewSet)


router = DefaultRouter()
router.register('rules', SudoRuleViewSet, basename="rule")
router.register('commands', SudoCommandViewSet, basename="command")
router.register('hosts', SudoHostViewSet, basename="hosts")

urlpatterns = router.urls
