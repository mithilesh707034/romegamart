from django.shortcuts import render


def home_page(Request):
    return render(Request,'front/index.html')

def brand_page(Request):
    return render(Request,'front/brands.html')

def categories_page(Request):
    return render(Request,'front/categories.html')

def product_page(Request):
    return render(Request,'front/products.html')

def product_details_page(Request):
    return render(Request,'front/product-details.html')

def flash_deals_page(Request):
    return render(Request,'front/flash-deals.html')

def blog_page(Request):
    return render(Request,'front/blog.html')

def cart_page(Request):
    return render(Request,'front/cart.html')

def compare_page(Request):
    return render(Request,'front/compare.html')

def wishlist_page(Request):
    return render(Request,'front/wishlist.html')

def buyer_login_page(Request):
    return render(Request,'front/login.html')

def buyer_registration_page(Request):
    return render(Request,'front/registration.html')

def seller_login_page(Request):
    return render(Request,'seller/login.html')

def seller_registration_page(Request):
    return render(Request,'seller/create.html')

def seller_product_page(Request):
    return render(Request,'seller/seller-product.html')