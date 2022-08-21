from django.urls import path, include
from rest_framework import views
from rest_framework.routers import DefaultRouter
from .views import MotorModuleViewset

router = DefaultRouter()
router.register('motor', MotorModuleViewset)




urlpatterns = [
    path('', include(router.urls))
]
