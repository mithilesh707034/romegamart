from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page),
    path('brands/',views.brand_page),
    path('categories/',views.categories_page),
    path('product/',views.product_page),
    path('flash-deals/',views.flash_deals_page),
    path('blog/',views.blog_page),
    path('cart/',views.cart_page),
    path('compare/',views.compare_page),
    path('wishlists/',views.wishlist_page),
    path('users/login/',views.buyer_login_page),
    path('users/registration/',views.buyer_registration_page),
    path('seller/login/',views.seller_login_page),
    path('seller/registration/',views.seller_registration_page),
    path('product-details/',views.product_details_page),
    path('seller-product/',views.seller_product_page),
]
