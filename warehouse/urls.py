from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductsApiView.as_view())
]
