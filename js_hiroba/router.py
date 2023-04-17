from command.views import CommandViewSet
from rest_framework import routers

router = routers.DefaultRouter()
# Command END POINT
router.register('code', CommandViewSet)
urlpatterns = router.urls