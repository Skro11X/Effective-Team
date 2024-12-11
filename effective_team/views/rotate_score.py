from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from effective_team.models import Member
from effective_team.serializers import RotateScoreSerializer

class RotateScoreAPIView(APIView):

    def post(self, request):
        serializer = RotateScoreSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            with transaction.atomic():
                self._init_swap(data)
                self._calculate_score()
                response_data = {self._creator_from.name: self._creator_from.score, self._creator_to.name: self._creator_to.score}
                return Response(data=response_data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def _init_swap(self, data):
        self._creator_from = data['creator_from']
        self._creator_to = data['creator_to']
        self._score = data['score']

    def _calculate_score(self):
        self._creator_from.score -= self._score
        self._creator_to.score += self._score
        self._creator_from.save()
        self._creator_to.save()
