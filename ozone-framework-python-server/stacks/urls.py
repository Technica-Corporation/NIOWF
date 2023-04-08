from rest_framework import routers
from .views import StackViewSet, StackAdminViewSet, StackGroupsViewSet


router = routers.SimpleRouter()

router.register(r'stacks', StackViewSet, basename='stacks')
router.register(r'admin/stacks', StackAdminViewSet, basename='admin_stacks')
router.register(r'admin/stacks-groups', StackGroupsViewSet, basename='admin_stacks-groups')

urlpatterns = [

]
urlpatterns += router.urls
