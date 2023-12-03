from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

import app.views


schema_view = get_schema_view(
    openapi.Info(
        title="Emo-Server API",
        default_version='v1',
        description="DDD 10기 앱 2팀 서버 API 문서",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('app.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
