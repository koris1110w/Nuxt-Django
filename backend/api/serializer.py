from rest_framework import serializers
from . import models

class RiddleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RiddleModel
        fields = "__all__"
        read_only_fields = ('id',)

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CreatorModel
        fields = "__all__"
        read_only_fields = ('id',)