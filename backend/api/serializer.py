from rest_framework import serializers
from . import models

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CreatorModel
        fields = "__all__"
        read_only_fields = ('id',)

class RiddleSerializer(serializers.ModelSerializer):
    creator = CreatorSerializer(read_only=True)
    type_str = serializers.SerializerMethodField("get_type_str")
    time_str = serializers.SerializerMethodField("get_time_str")
    level_str = serializers.SerializerMethodField("get_level_str")

    class Meta:
        model = models.RiddleModel
        fields = "__all__"
        read_only_fields = ('id',)

    def get_type_str(self, obj):
        return obj.get_type_display()
    
    def get_time_str(self, obj):
        return obj.get_time_display()
        # if obj.rating_quantity == 0:
        #     return "評価なし"
        # elif obj.rating_quantity < 2:
        #     return "〜30分"
        # elif obj.rating_quantity < 3:
        #     return "30〜90分"
        # elif obj.rating_quantity < 4:
        #     return "90〜180分"
        # elif obj.rating_quantity < 5:
        #     return "180分〜"
    
    def get_level_str(self, obj):
        return obj.get_level_display()
        # if obj.rating_level < 1:
        #     return "評価なし"
        # elif obj.rating_level < 2:
        #     return "初級"
        # elif obj.rating_level < 3:
        #     return "中級"
        # elif obj.rating_level < 4:
        #     return "上級"
        # elif obj.rating_level < 5:
        #     return "超上級"