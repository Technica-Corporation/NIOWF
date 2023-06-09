from .views import AppConfViewSet, AppConfAdminViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'admin/application-configuration', AppConfAdminViewSet, basename='admin_application-configuration')
router.register(r'application-configuration', AppConfViewSet, basename='application-configuration')


urlpatterns = [
]
urlpatterns += router.urls
