from django.urls import path

from menu import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('product/', views.CreateProductView.as_view(), name='product'),
    path('product/<int:pk>/delete', views.DeleteProductView.as_view(), name='product-delete'),
    path('payment/', views.PaymentMethodView.as_view(), name='payment'),
    path('payments/', views.PaymentMethodListView.as_view(), name='payment_list'),
    path('user/', views.CreateUserView.as_view(), name='add_user')
]


'''
https://docs.djangoproject.com/en/2.2/topics/auth/default/#built-in-auth-views
    
    path('accounts/', include('django.contrib.auth.urls')),

This will include the following URL patterns:

accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
'''
