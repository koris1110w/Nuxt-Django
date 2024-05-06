from django_filters import rest_framework as filters
from django.db.models import Q
from . import models

FILTER_SET = (
    ("created_at", "新着順"),
    ("rating", "評価順"),
    ("playings", "プレイ数順"),
    ("level", "難易度順"),
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
