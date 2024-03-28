from django.contrib import admin
from django.urls import path
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static

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
    path('seller-logout/',views.seller_logout_page),

    #Buyer App Code
    path('app-buyer-registration/',views.app_buyer_registration),
    path('app-user-login/',views.app_user_login),
    path('app-update-buyer-profile/',views.app_update_buyer_profile),
    path('app-get-product/',views.app_get_product),
    path('app-get-maincategory/',views.app_get_maincategory),
    path('app-get-category/',views.app_get_category),
    path('app-get-brand/',views.app_get_brand),
    path('app-get-product-details/',views.app_get_product_details),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

