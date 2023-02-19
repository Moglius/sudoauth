from rest_framework.routers import DefaultRouter
from .views import (
    LnxShellViewSet,
    LnxGroupViewSet
)


router = DefaultRouter()
router.register('lnxshells', LnxShellViewSet, basename="lnxshell")
router.register('lnxgroups', LnxGroupViewSet, basename="lnxgroups")

urlpatterns = router.urls
