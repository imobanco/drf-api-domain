from rest_framework.routers import DefaultRouter

from .apis.rest import UserViewSet


router = DefaultRouter()
router.register("users", UserViewSet, basename="user")

urlpatterns = router.urls
