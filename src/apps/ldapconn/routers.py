from rest_framework.routers import DefaultRouter
from .views import LDAPUserViewSet


router = DefaultRouter()
router.register('ldapusers', LDAPUserViewSet, basename="ldapuser")

urlpatterns = router.urls
