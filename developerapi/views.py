from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from developersearch.models import Developers
from developerapi.serializers import UserSerializer, GroupSerializer, DeveloperSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class DeveloperList(viewsets.ModelViewSet):
    queryset = Developers.objects.all()
    serializer_class = DeveloperSerializer


