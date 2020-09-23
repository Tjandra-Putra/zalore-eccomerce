from django.urls import path
from . import views  # dot means current directory
from .views import ClothingDetailView

urlpatterns = [
    path('', views.home, name='zalore-home'),

    path('cart/', views.cart, name='zalore-cart'),

    path('clothing/', views.clothing, name="zalore-clothing"),

    path('clothing/<int:pk>/', ClothingDetailView.as_view(), name='zalore-clothing-detail'),

    path('support/', views.support, name="zalore-support"),

    path('admin/support/', views.admin_support, name="zalore-admin-support"),

    path('admin/', views.admin_dashboard, name="zalore-admin-dashboard"),

    path('admin/product/', views.admin_product, name="zalore-admin-product"),

    path('admin/product/delete/<int:id>/', views.admin_product_delete, name="zalore-admin-product-delete")
]
