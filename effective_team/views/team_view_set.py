from rest_framework import viewsets
from effective_team.models import Team
from effective_team.serializers import TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    '''
     CRUD realization for model
    '''
    queryset = Team.objects.all()
    serializer_class = TeamSerializer