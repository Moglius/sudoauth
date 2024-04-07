from rest_framework.routers import DefaultRouter

from .views import LnxGroupViewSet, LnxShellViewSet, LnxUserViewSet

router = DefaultRouter()
router.register("shells", LnxShellViewSet, basename="shells")
router.register("groups", LnxGroupViewSet, basename="groups")
router.register("users", LnxUserViewSet, basename="users")

urlpatterns = router.urls
