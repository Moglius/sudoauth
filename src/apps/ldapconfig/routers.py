from rest_framework.routers import DefaultRouter
from .views import (DNSHostViewSet, LDAPDnViewSet,
    LDAPConfigViewSet)


router = DefaultRouter()
router.register('dnshosts', DNSHostViewSet, basename="dnshost")
router.register('ldapdns', LDAPDnViewSet, basename="ldapdn")
router.register('ldapconfigs', LDAPConfigViewSet, basename="ldapconfig")

urlpatterns = router.urls
