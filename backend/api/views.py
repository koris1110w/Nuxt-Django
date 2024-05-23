from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from . import models
from . import serializer
from . import pagination
from . import filter

class APIRiddleListView(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    queryset = models.RiddleModel.objects.all().order_by("created_at")
    serializer_class = serializer.RiddleSerializer
    pagination_class = pagination.StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = filter.RiddleFilter

class APIRankingView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = models.RiddleModel.objects.order_by('rating').reverse()[0:10]
    serializer_class = serializer.RiddleSerializer

class APIRiddleDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = models.RiddleModel.objects.all()
    serializer_class = serializer.RiddleSerializer

class APICreatorDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = models.CreatorModel.objects.all()
    serializer_class = serializer.CreatorSerializer

class APIPlayingView(APIView):
    permission_classes = [AllowAny]

    def post(self, *args, **kwargs):
        pk = kwargs.get('pk')
        object = get_object_or_404(models.RiddleModel, pk=pk)
        object.playings += 1
        object.save()
        return Response({'status': 'success'}, status=200)
    
class APICollectReviewView(APIView):
    permission_classes = [AllowAny]

    def post(self, *args, **kwargs):
        pk = kwargs.get('pk')
        object = get_object_or_404(models.RiddleModel, pk=pk)
        review = models.ReviewModel.objects.filter(riddle=object)
        object.rating = review.aggregate(result=Avg("rating"))["result"]
        object.level = review.aggregate(result=Avg("level"))["result"]
        object.time = review.aggregate(result=Avg("time"))["result"]
        object.sukkiri = review.aggregate(result=Avg("sukkiri"))["result"]
        object.gimmick = review.aggregate(result=Avg("gimmick"))["result"]
        object.story = review.aggregate(result=Avg("story"))["result"]
        object.save()
        return Response({'status': 'success'}, status=200)