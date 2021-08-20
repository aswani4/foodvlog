from django.urls import path
from . import views

urlpatterns=[
    path('cart_det',views.cart_Details,name='cart_det'),
    path('add/<int:product_id>/',views.add_cart,name='add'),
    path('decrement/<int:product_id>/',views.min_cart,name='decrement'),
    path('remove/<int:product_id>/',views.cart_delete,name='remove'),

]