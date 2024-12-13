from rest_framework import viewsets
from effective_team.models import TeamApplication
from effective_team.serializers import TeamApplicationSerializer


class TeamApplicationViewSet(viewsets.ModelViewSet):
    '''
     CRUD realization for model TeamApplication
    '''
    queryset = TeamApplication.objects.all()
    serializer_class = TeamApplicationSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        pk_exist = self.kwargs
        if pk_exist:
            return super().get_queryset()
        else:
            return self.queryset.select_related("member").order_by("-member__endurance")[:10]
    #TeamApplication.objects.select_related("member").order_by("-member__endurance")[:10]