from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class TeamApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamApplication
        fields = '__all__'


class RotateScoreSerializer(serializers.Serializer):
    creator_from = serializers.PrimaryKeyRelatedField(queryset=Creator.objects.all())
    creator_to = serializers.PrimaryKeyRelatedField(queryset=Creator.objects.all())
    score = serializers.IntegerField()

    def validate(self, data):
        creator_from = data['creator_from']
        score = data['score']
        if creator_from.score - score < 0:
            raise ValidationError({'error': f'{creator_from.name} not enough score'})
        return data