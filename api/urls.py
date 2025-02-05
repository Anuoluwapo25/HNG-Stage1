from django.urls import path
from .views import ClassifyNum


urlpatterns = {
    path('api/', ClassifyNum.as_views, name="numapi")
}