from django.urls import path
from .views import ProductView,ProductIDView

urlpatterns=[
    path('',ProductView.as_view(),name="ProductView"),
    path('<int:pk>/',ProductIDView.as_view(),name="ProductIDView")
]