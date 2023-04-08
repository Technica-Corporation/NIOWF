from .views import DashboardViewSet, DashboardAdminViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'dashboards', DashboardViewSet, basename='dashboards')
router.register(r'admin/dashboards', DashboardAdminViewSet, basename='admin_dashboards')

urlpatterns = [
]
urlpatterns += router.urls
