from rest_framework import serializers
from . import models


class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CreatorModel
        fields = "__all__"

class RiddleSerializer(serializers.ModelSerializer):
    creator = CreatorSerializer(read_only=True)
    creator_name = serializers.SerializerMethodField("get_creator_name")
    time_str = serializers.SerializerMethodField("get_time_str")
    class Meta:
        model = models.RiddleModel
        fields = "__all__"
        read_only_fields = ('id',)

    def get_creator_name(self, obj):
        if len(obj.creator.name) > 2:
            return obj.creator.name[:2] + "..."
        return obj.creator.name

    def get_time_str(self, obj):
        return obj.get_time_display()


class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CreatorModel
        fields = "__all__"
        read_only_fields = ('id',)