from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from effective_team.models import Member
from effective_team.serializers import MemberSerializer


class MemberAPIView(CreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
