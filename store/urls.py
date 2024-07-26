from django.urls import path
from . import views

# URLs config
urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_details)
]
