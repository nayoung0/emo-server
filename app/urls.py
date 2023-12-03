from django.urls import path
from . import views

urlpatterns = [
    path('sample/', views.OnePersonAPIView.as_view(), name='sample'),
]
