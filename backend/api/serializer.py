from rest_framework import serializers
from . import models
from django.db.models import Avg

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CreatorModel
        fields = "__all__"
        read_only_fields = ('id',)

class RiddleSerializer(serializers.ModelSerializer):
    creator = CreatorSerializer(read_only=True)
    type_str = serializers.SerializerMethodField("get_type_str")
    level_str = serializers.SerializerMethodField("get_level_str")
    time_str = serializers.SerializerMethodField("get_time_str")

    class Meta:
        model = models.RiddleModel
        fields = "__all__"
        read_only_fields = ('id',)

    def get_type_str(self, obj):
        return obj.get_type_display()

    def get_time_str(self, obj):
        time = obj.time
        if time <= 2:
            time_str = "〜30分"
        elif time <= 3:
            time_str = "30〜90分"
        elif time <= 4:
            time_str = "90〜180分"
        elif time <= 5:
            time_str = "180分〜"
        return time_str
    
    def get_level_str(self, obj):
        level = obj.level
        if level <= 2:
            level_str = "初級"
        elif level <= 3:
            level_str = "中級"
        elif level <= 4:
            level_str = "上級"
        elif level <= 5:
            level_str = "超上級"
        return level_str

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReviewModel
        fields = "__all__"
        read_only_fields = ('id',)

class ArticleSerializer(serializers.ModelSerializer):
    riddles = RiddleSerializer(read_only=True, many=True)
    
    class Meta:
        model = models.ArticleModel
        fields = "__all__"
        read_only_fields = ('id',)