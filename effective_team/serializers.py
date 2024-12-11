from rest_framework import serializers
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
    creator_from = serializers.IntegerField()
    creator_to = serializers.IntegerField()
    score = serializers.IntegerField()