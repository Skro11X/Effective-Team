from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, viewsets
from effective_team.models import Creator, Team, Member, TeamApplication
from effective_team.serializers import CreatorSerializer, TeamSerializer, MemberSerializer, TeamApplicationSerializer, RotateScoreSerializer

class CreatorViewSet(viewsets.ModelViewSet):
    queryset = Creator
    serializer_class = CreatorSerializer