from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SudoRuleViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('sudo-rules', SudoRuleViewSet, basename="sudo-rule")

urlpatterns = router.urls
