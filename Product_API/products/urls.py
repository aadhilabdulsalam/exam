from django.urls import path
from products import views

urlpatterns = [
    path('items', views.ProductListCreate.as_view()),
    path('items/<int:pk>', views.ProductRetrieveUpdateDelete.as_view()),
]
