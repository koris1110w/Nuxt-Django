from django_filters import rest_framework as filters
from django.db.models import Q
from . import models

TIME_SET = (
    ("1", "〜30分"),
    ("2", "30分〜90分"),
    ("3", "90分~180分"),
    ("4", "180分〜")
)
    
LEVEL_SET = (
    ("1", "初級"),
    ("2", "中級"),
    ("3", "上級"),
    ("4", "超上級")
)

FILTER_SET = (
    ("created_at", "新着順"),
    ("rating", "評価順"),
    ("playings", "プレイ数順"),
    ("level", "難易度順"),
)

TAG_SET = (
    ("sukkiri", "スッキリ"),
    ("story", "ストーリー"),
    ("gimmick", "ギミック")
)

class RiddleFilter(filters.FilterSet):
    type = filters.MultipleChoiceFilter(choices=models.TYPE_SET)
    time = filters.MultipleChoiceFilter(choices=TIME_SET, method='timeFilter')
    level = filters.MultipleChoiceFilter(choices=LEVEL_SET, method='levelFilter')
    creator = filters.NumberFilter()
    word = filters.CharFilter(method='wordFilter')
    order = filters.CharFilter(method='orderFilter')
    tag = filters.MultipleChoiceFilter(choices=TAG_SET, method='tagFilter')

    class Meta:
        model = models.RiddleModel
        fields = ['type','time','level','word','order','creator',]

    def wordFilter(self,queryset,name,value):
        #ここでOR検索を入れる。fieldsのcustomerNameに入ってきた値を利用
        return queryset.filter(Q(name__icontains=value)|Q(description__icontains=value))
    
    def orderFilter(self,queryset,name,value):
        return queryset.order_by(value).reverse()
    
    def tagFilter(self,queryset,name,values):
        if "sukkiri" in values:
            queryset = queryset.filter(sukkiri__gte=4)
        if "story" in values:
            queryset = queryset.filter(story__gte=4)
        if "gimmick" in values:
            queryset = queryset.filter(gimmick__gte=4)
        return queryset
    
    def timeFilter(self,queryset,name,values):
        print(values)
        result = models.RiddleModel.objects.none()
        if "1" in values:
            result = result.union(queryset.filter(time__gte=1, time__lte=2))
        if "2" in values:
            result = result.union(queryset.filter(time__gt=2, time__lte=3))
        if "3" in values:
            result = result.union(queryset.filter(time__gt=3, time__lte=4))
        if "4" in values:
            result = result.union(queryset.filter(time__gt=4, time__lte=5))
        return result
    
    def levelFilter(self,queryset,name,values):
        result = models.RiddleModel.objects.none()
        if "1" in values:
            result = result.union(queryset.filter(level__gte=1, level__lte=2))
        if "2" in values:
            result = result.union(queryset.filter(level__gt=2, level__lte=3))
        if "3" in values:
            result = result.union(queryset.filter(level__gt=3, level__lte=4))
        if "4" in values:
            result = result.union(queryset.filter(level__gt=4, level__lte=5))
        return result