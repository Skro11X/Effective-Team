from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from effective_team.models import Team
from effective_team.serializers import TeamSerializer


class TeamAPIView(CreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
