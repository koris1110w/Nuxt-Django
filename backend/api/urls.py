from django.urls import path

from . import views

app_name = "api"

urlpatterns = [
    path("riddles/", views.APIRiddleListView.as_view(), name="riddles"),
    path("riddles/<int:pk>/", views.APIRiddleDetailView.as_view(), name="detail"),
    path("creator/<int:pk>/", views.APICreatorDetailView.as_view(), name="creator"),
    path('ranking/', views.APIRankingView.as_view(), name='api_ranking'),
    path("playing/<int:pk>/", views.APIPlayingView.as_view(), name="api_playing"),
    path("collect_review/<int:pk>/", views.APICollectReviewView.as_view()),
]