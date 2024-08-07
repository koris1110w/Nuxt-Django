from django.urls import path

from . import views

def trigger_error(request):
    division_by_zero = 1 / 0

app_name = "api"

urlpatterns = [
    path("riddles/", views.APIRiddleListView.as_view(), name="riddles"),
    path("riddles/<int:pk>/", views.APIRiddleDetailView.as_view(), name="detail"),
    path("creator/<int:pk>/", views.APICreatorDetailView.as_view(), name="creator"),
    path('ranking/', views.APIRankingView.as_view(), name='api_ranking'),
    path("playing/<int:pk>/", views.APIPlayingView.as_view(), name="api_playing"),
    path("collect_review/<int:pk>/", views.APICollectReviewView.as_view()),
    path("articles/", views.APIArticleListView.as_view(), name="articles"),
    path("articles/<int:pk>/", views.APIArticleDetailView.as_view(), name="articles_detail"),
    path('sentry-debug/', trigger_error),
]