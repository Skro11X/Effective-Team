from rest_framework import viewsets
from effective_team.models import Member
from effective_team.serializers import MemberSerializer


class MemberViewSet(viewsets.ModelViewSet):
    '''
     CRUD realization for model Creator
    '''
    queryset = Member.objects.all()
    serializer_class = MemberSerializer