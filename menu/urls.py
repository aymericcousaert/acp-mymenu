from django.urls import path, include

from menu import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('', include('django.contrib.auth.urls')),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('product/<int:pk>/description', views.ProductDescription.as_view(), name='productDescription'),
    path('payments/', views.PaymentMethodListView.as_view(), name='payment_list'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('promotions/', views.PromotionListView.as_view(), name='promotions'),
]


