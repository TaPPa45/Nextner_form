from django.urls import path
from .views import ProductCreateView, succeed
urlpatterns = [
    path('create-form/', ProductCreateView.as_view(), name='create-form'),
    path('succeed/', succeed, name='succeed'),
]