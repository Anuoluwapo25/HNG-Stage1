from django.urls import path
from .views import ClassifyNum


urlpatterns = {
    path('api/classify-number/', ClassifyNum.as_view(), name="numapi")
}