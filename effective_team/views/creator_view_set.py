from rest_framework import viewsets
from effective_team.models import Creator
from effective_team.serializers import CreatorSerializer


class CreatorViewSet(viewsets.ModelViewSet):
    '''
    CRUD realization for model Creator
    '''
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer