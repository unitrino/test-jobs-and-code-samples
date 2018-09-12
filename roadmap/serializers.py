from rest_framework import serializers
from django.contrib.auth.models import User
from roadmap.models import Project, Roadmap, Step


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        exclude = ('id',)


class RoadmapSerializer(serializers.ModelSerializer):
    steps = StepSerializer(required=True, many=True)

    class Meta:
        model = Roadmap
        exclude = ('id',)


class ProjectSerializer(serializers.ModelSerializer):
    roadmap = RoadmapSerializer(required=False)
    owner = UserSerializer(required=True)

    class Meta:
        model = Project
        fields = '__all__'