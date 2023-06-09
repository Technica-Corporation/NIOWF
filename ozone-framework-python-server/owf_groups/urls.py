from django.urls import path

from .views import OWFGroupPeopleViewSet, OWFGroupViewSet, OWFGroupWidgetViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'admin/groups', OWFGroupViewSet, basename='admin_groups')
router.register(r'admin/groups-people', OWFGroupPeopleViewSet, basename='admin_groups-people')

urlpatterns = [
    path('admin/groups-widgets/', OWFGroupWidgetViewSet.as_view(), name='admin_groups-widgets'),
]
urlpatterns += router.urls
