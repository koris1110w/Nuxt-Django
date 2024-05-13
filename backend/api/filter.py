from django_filters import rest_framework as filters
from django.db.models import Q
from . import models

FILTER_SET = (
    ("created_at", "新着順"),
    ("rating", "評価順"),
    ("playings", "プレイ数順"),
    ("level", "難易度順"),
)

TIME_SET = (
    (1, "〜30分"),
    (2, "30〜90分"),
    (3, "90分~180分"),
    (4, "180分〜")
)
    
LEVEL_SET = (
    (1, "初級"),
    (2, "中級"),
    (3, "上級"),
    (4, "超上級")
)

class RiddleFilter(filters.FilterSet):
    type = filters.MultipleChoiceFilter(choices=models.TYPE_SET)
    time = filters.MultipleChoiceFilter(choices=models.TIME_SET)
    level = filters.MultipleChoiceFilter(choices=models.LEVEL_SET)
    creator = filters.NumberFilter()
    word = filters.CharFilter(method='wordFilter')
    order = filters.CharFilter(method='orderFilter')

    class Meta:
        model = models.RiddleModel
        fields = ['type','time','level','word','order','creator',]

    def wordFilter(self,queryset,name,value):
        #ここでOR検索を入れる。fieldsのcustomerNameに入ってきた値を利用
        return queryset.filter(Q(name__icontains=value)|Q(description__icontains=value))
    
    def orderFilter(self,queryset,name,value):
        return queryset.order_by(value).reverse()
    
    # def timeFilter(self,queryset,name,value):
    #     print(value)
    #     if value == "1":
    #         return queryset.filter(rating_quantity__gte=1, rating_quantity__lt=2)
    #     elif value == "2":
    #         return queryset.filter(rating_quantity__gte=2, rating_quantity__lt=3)
    #     elif value == "3":
    #         return queryset.filter(rating_quantity__gte=3, rating_quantity__lt=4)
    #     elif value == "4":
    #         return queryset.filter(rating_quantity__gte=4, rating_quantity__lt=5)
        
    # def levelFilter(self,queryset,name,value):
    #     if value == "1":
    #         return queryset.filter(rating_level__gte=1, rating_level__lt=2)
    #     elif value == "2":
    #         return queryset.filter(rating_level__gte=2, rating_level__lt=3)
    #     elif value == "3":
    #         return queryset.filter(rating_level__gte=3, rating_level__lt=4)
    #     elif value == "4":
    #         return queryset.filter(rating_level__gte=4, rating_level__lt=5)