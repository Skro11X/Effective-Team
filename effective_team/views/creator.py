from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from effective_team.models import Creator
from effective_team.serializers import CreatorSerializer


class CreatorAPIView(CreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer