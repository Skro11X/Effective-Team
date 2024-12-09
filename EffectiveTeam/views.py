from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from EffectiveTeam.models import Creator, Team, Member, TeamApplication
from EffectiveTeam.serializers import CreatorSerializer, TeamSerializer, MemberSerializer, TeamApplicationSerializer, RotateScoreSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
from django.db import transaction

class CreatorAPIView(CreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer


class TeamAPIView(CreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class MemberAPIView(CreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class TeamApplicationAPIView(ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView):
    queryset = TeamApplication.objects.select_related("member").order_by("-member__endurance")[:10]
    serializer_class = TeamApplicationSerializer


class RotateScoreAPIView(APIView):

    def post(self, request):
        serializer = RotateScoreSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            with transaction.atomic():
                self._init_swap(data)
                if self._creator_from.score - self._score < 0:
                    return Response(data={'error': f'{self._creator_from.name} not enough score'}, status=status.HTTP_400_BAD_REQUEST)
                self._calculate_score()
                response_data = {self._creator_from.name: self._creator_from.score, self._creator_to.name: self._creator_to.score}
                return Response(data=response_data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def _init_swap(self, data):
        self._creator_from = get_object_or_404(Creator, id=data['creator_from'])
        self._creator_to = get_object_or_404(Creator, id=data['creator_to'])
        self._score = data['score']

    def _calculate_score(self):
        self._creator_from.score -= self._score
        self._creator_to.score += self._score
        self._creator_from.save()
        self._creator_to.save()
