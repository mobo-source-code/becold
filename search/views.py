from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Motor
from .serializers import MotorSerializer 


class MotorModuleViewset(viewsets.ModelViewSet):
    queryset = Motor.objects.all()
    serializer_class = MotorSerializer





