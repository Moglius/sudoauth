from rest_framework.routers import DefaultRouter
from .views import SudoRuleViewSet


router = DefaultRouter()
router.register('sudo-rules', SudoRuleViewSet, basename="sudo-rule")

urlpatterns = router.urls
