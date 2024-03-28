from rest_framework import serializers
from .models import *

class SellerSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=100)
    phone=serializers.CharField(max_length=10)
    email=serializers.EmailField(default='')
    company_name=serializers.CharField(max_length=100)
    company_slug=serializers.CharField(max_length=100)
    brand_name=serializers.CharField(max_length=100)
    brand_slug=serializers.CharField(max_length=100)

    password=serializers.CharField(max_length=100)
    address=serializers.CharField(max_length=100)
    alternate_phone=serializers.CharField(max_length=100)

    photo=serializers.FileField(max_length=None,use_url=True,allow_null=True,required=False)
    banner=serializers.FileField(max_length=None,use_url=True,allow_null=True,required=False)
    gst_certificate=serializers.FileField(max_length=None,use_url=True,allow_null=True,required=False)
    udhyam_certificate=serializers.FileField(max_length=None,use_url=True,allow_null=True,required=False)
    cancelled_check=serializers.FileField(max_length=None,use_url=True,allow_null=True,required=False)
    pan_card=serializers.FileField(max_length=None,use_url=True,allow_null=True,required=False)
    aadhar_card=serializers.FileField(max_length=None,use_url=True,allow_null=True,required=False)

    date=serializers.CharField(max_length=100)
    rating=serializers.IntegerField()
    follower=serializers.IntegerField()
    otp=serializers.IntegerField()
    verification=serializers.CharField(max_length=100)

    def create(self,validatedData):
        return Seller.objects.create(**validatedData)


class BuyerSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    phone=serializers.CharField(max_length=100)
    name=serializers.CharField(max_length=100)
    email=serializers.EmailField(max_length=100)
    pin=serializers.CharField(max_length=100)
    address=serializers.CharField(max_length=100)
    city=serializers.CharField(max_length=100)
    state=serializers.CharField(max_length=100)
    password=serializers.CharField(max_length=100)

   
    pan=serializers.FileField(max_length=None,use_url=True,allow_null=True,required=False)
    gst_certificate=serializers.FileField(max_length=None,use_url=True,allow_null=True,required=False)
    

    date=serializers.CharField(max_length=100)
    otp=serializers.IntegerField()
    verification=serializers.CharField(max_length=100)
    user_type=serializers.CharField(max_length=100)

    def create(self,validatedData):
        return Buyer.objects.create(**validatedData)


class ProductSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=200)
    maincategory=serializers.CharField(max_length=200)
    maincategory_slug=serializers.CharField(max_length=200)
    subcategory=serializers.CharField(max_length=200)
    subcategory_slug=serializers.CharField(max_length=200)
    brand=serializers.CharField(max_length=200)
    brand_slug=serializers.CharField(max_length=200)
    unit=serializers.CharField(max_length=200)
    unit_slug=serializers.CharField(max_length=200)
    weight=serializers.CharField(max_length=200)
    minimum_purchase_qty=serializers.IntegerField()
    tags=serializers.CharField(max_length=2000)
    product_image=serializers.ImageField(max_length=None,use_url=True,allow_null=True,required=False)
    product_thumbnail=serializers.ImageField(max_length=None,use_url=True,allow_null=True,required=False)
    link_type=serializers.CharField(max_length=200)
    video_link=serializers.CharField(max_length=200)
    color=serializers.CharField(max_length=200)
    attribute=serializers.CharField(max_length=200)
    unit_price=serializers.CharField(max_length=200)
    discount_range=serializers.CharField(max_length=200)
    discount=serializers.CharField(max_length=200)
    qty=serializers.IntegerField(default=1)
    sku=serializers.CharField(max_length=200)
    external_link=serializers.CharField(max_length=200)
    external_link_button_text=serializers.CharField(max_length=200)
    key_features=serializers.CharField(max_length=2000)
    subcategory_specification=serializers.CharField(max_length=2000)
    product_description=serializers.CharField(max_length=2000)
    product_faq_title=serializers.CharField(max_length=2000)
    product_faq_answer=serializers.CharField(max_length=2000)
    pdf_specification=serializers.CharField(max_length=200)
    seo_meta_title=serializers.CharField(max_length=2000)
    meta_description=serializers.CharField(max_length=2000)
    meta_image=serializers.ImageField(max_length=None,use_url=True,allow_null=True,required=False)
    free_shipping=serializers.CharField(max_length=200)
    fat_rate=serializers.CharField(max_length=200)
    is_product_quality_multiply=serializers.CharField(max_length=200)
    low_stock_qty=serializers.CharField(max_length=200)
    hide_stock=serializers.CharField(max_length=200)
    cash_on_delivery=serializers.CharField(max_length=200)
    shipping_day=serializers.CharField(max_length=200)
    tax=serializers.CharField(max_length=200)
    def create(self,validatedData):
        return Product.objects.create(**validatedData)



class MaincategorySerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=100)
    slug=serializers.CharField(max_length=100)
    image=serializers.FileField(max_length=None,use_url=True,allow_null=True,required=False)

    def create(self,validatedData):
        return Maincategory.objects.create(**validatedData)


class CategorySerializer(serializers.Serializer):
    id=serializers.IntegerField()
    maincategory=serializers.CharField(max_length=100)
    maincategory_slug=serializers.CharField(max_length=10)
    category_name=serializers.CharField(max_length=100)
    category_slug=serializers.CharField(max_length=100)
    image=serializers.FileField(max_length=None,use_url=True,allow_null=True,required=False)

    def create(self,validatedData):
        return Category.objects.create(**validatedData)


class BrandSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=100)
    slug=serializers.CharField(max_length=100)
    image=serializers.FileField(max_length=None,use_url=True,allow_null=True,required=False)

    def create(self,validatedData):
        return Brand.objects.create(**validatedData)

