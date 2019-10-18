from django.urls import path

from menu import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('products/', views.ProductListView.as_view(), name='products'),
]
