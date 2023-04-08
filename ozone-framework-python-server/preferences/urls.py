from rest_framework import routers

from preferences.views import PreferenceUserViewSet, PreferenceAdminViewSet

router = routers.SimpleRouter()
router.register(r'preferences', PreferenceUserViewSet, basename='base_preferences')
router.register(r'admin/preferences', PreferenceAdminViewSet, basename='admin_preferences')

urlpatterns = [

]
urlpatterns += router.urls
