from django.urls import path, include

from menu import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('', include('django.contrib.auth.urls')),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('product/', views.CreateProductView.as_view(), name='product'),
    path('product/<int:pk>/delete', views.DeleteProductView.as_view(), name='product-delete'),
    path('payment/', views.PaymentMethodView.as_view(), name='payment'),
    path('payments/', views.PaymentMethodListView.as_view(), name='payment_list')
]
