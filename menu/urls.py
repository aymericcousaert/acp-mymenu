from django.urls import path

from menu import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('product/', views.newproduct, name='product'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('category/', views.newCategory, name='category'),
    path('productChoice/<category>/', views.SelectProduct.as_view(), name='productChoice')
]
