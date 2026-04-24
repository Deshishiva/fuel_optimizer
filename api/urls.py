from django.urls import path
from .views import optimize_route

urlpatterns = [
    path('route/', optimize_route),
]