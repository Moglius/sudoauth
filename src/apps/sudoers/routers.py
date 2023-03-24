from rest_framework.routers import DefaultRouter
from .views import SudoRuleViewSet, SudoCommandViewSet


router = DefaultRouter()
router.register('rules', SudoRuleViewSet, basename="rule")
router.register('commands', SudoCommandViewSet, basename="command")

urlpatterns = router.urls
