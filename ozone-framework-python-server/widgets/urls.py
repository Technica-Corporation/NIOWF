from .views import WidgetDefinitionViewSet, WidgetTypesViewSet, WidgetViewSet, WidgetDefinitionWidgetTypesViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'admin/widgets', WidgetDefinitionViewSet, basename='widgets')
router.register(r'admin/widget-definition-widgets-types', WidgetDefinitionWidgetTypesViewSet, basename='widgets-t-d')
router.register(r'admin/widgets-types', WidgetTypesViewSet, basename='widget-types')
router.register(r'widgets', WidgetViewSet)


urlpatterns = [

]
urlpatterns += router.urls
