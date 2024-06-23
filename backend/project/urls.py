from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include("api.urls")),
    path('markdownx/', include('markdownx.urls')),
    # jwt-tokenを取得
    path('api-auth/jwt/', views.TokenObtainPairView.as_view()),
    # jwt-tokenを再取得
    path('api-auth/jwt/refresh', views.TokenRefreshView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)