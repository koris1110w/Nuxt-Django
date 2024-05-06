from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from . import models
from . import serializer
from . import pagination
from . import filter

class APIRiddleListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = models.RiddleModel.objects.all().order_by("created_at")
    serializer_class = serializer.RiddleSerializer
    pagination_class = pagination.StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = filter.RiddleFilter

class APIRankingView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = models.RiddleModel.objects.order_by('rating').reverse()[0:5]
    serializer_class = serializer.RiddleSerializer

class APIRiddleDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        object = get_object_or_404(models.RiddleModel, pk=pk)
        return Response({'riddle': object}, status=200)

class APIPlayingView(APIView):
    permission_classes = [AllowAny]

    def post(self, *args, **kwargs):
        pk = kwargs.get('pk')
        object = get_object_or_404(models.RiddleModel, pk=pk)
        object.playings += 1
        object.save()
        return Response({'status': 'success'}, status=200)