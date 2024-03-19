from django.urls import path, include
from rest_framework import routers
from rideapi.views import RideLocationUpdateViewSet, UserRegistrationViewSet, UserLoginViewSet,RideViewSet, RideStatusUpdateViewSet

router = routers.DefaultRouter()
router.register(r'register', UserRegistrationViewSet, basename='registration')
router.register(r'login', UserLoginViewSet, basename='login')
router.register(r'rides', RideViewSet, basename='ride')
router.register(r'rides', RideStatusUpdateViewSet, basename='ride')
router.register(r'rides', RideLocationUpdateViewSet, basename='ride')



urlpatterns = [
    path('', include(router.urls)),
]

#PostmanUrl:
#("/api/register/")
#("/api/login/")
#("/api/rides/")
#("/api/rides/<pk>/update_status/)
#("/api/rides/<pk>/update_location/)