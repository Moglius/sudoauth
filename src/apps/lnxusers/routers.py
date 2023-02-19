from rest_framework.routers import DefaultRouter
from .views import (LnxShellViewSet, LnxGroupViewSet,
    LnxUserViewSet
)


router = DefaultRouter()
router.register('lnxshells', LnxShellViewSet, basename="lnxshell")
router.register('lnxgroups', LnxGroupViewSet, basename="lnxgroup")
router.register('lnxusers', LnxUserViewSet, basename="lnxuser")

urlpatterns = router.urls
