from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from effective_team.models import TeamApplication
from effective_team.serializers import TeamApplicationSerializer


class TeamApplicationAPIView(ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView):
    queryset = TeamApplication.objects.select_related("member").order_by("-member__endurance")[:10]
    serializer_class = TeamApplicationSerializer
