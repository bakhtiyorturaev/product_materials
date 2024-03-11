from django.urls import path
from .views import ProductMaterialsAPIView

urlpatterns = [
    path('', ProductMaterialsAPIView.as_view()),
]
