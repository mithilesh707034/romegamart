from django.db import models

class Seller(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default='',null=True,blank=True)
    phone=models.CharField(max_length=10,default='',null=True,blank=True)
    email=models.EmailField(default='',null=True,blank=True)
    company_name=models.CharField(max_length=100,default='',null=True,blank=True)
    company_slug=models.CharField(max_length=100,default='',null=True,blank=True)
    brand_name=models.CharField(max_length=100,default='',null=True,blank=True)
    brand_slug=models.CharField(max_length=100,default='',null=True,blank=True)

    password=models.CharField(max_length=100,default='',null=True,blank=True)
    address=models.CharField(max_length=100,default='',null=True,blank=True)
    alternate_phone=models.CharField(max_length=100,default='',null=True,blank=True)

    photo=models.FileField(upload_to="uploads",default='',null=True,blank=True)
    banner=models.FileField(upload_to="uploads",default='',null=True,blank=True)
    gst_certificate=models.FileField(upload_to="uploads",default='',null=True,blank=True)
    udhyam_certificate=models.FileField(upload_to="uploads",default='',null=True,blank=True)
    cancelled_check=models.FileField(upload_to="uploads",default='',null=True,blank=True)
    pan_card=models.FileField(upload_to="uploads",default='',null=True,blank=True)
    aadhar_card=models.FileField(upload_to="uploads",default='',null=True,blank=True)

    date=models.DateField(auto_now=True)
    rating=models.IntegerField(default=0,null=True,blank=True)
    follower=models.IntegerField(default=0,null=True,blank=True)
    otp=models.IntegerField(default=9241,null=True,blank=True)
    verification=models.CharField(max_length=100,default='Pending',null=True,blank=True)
    def __str__(self):
        return self.name

    

class Buyer(models.Model):
    id=models.AutoField(primary_key=True)
    phone=models.CharField(max_length=10,default='',null=True,blank=True)
    name=models.CharField(max_length=100,default='',null=True,blank=True)
    email=models.EmailField(default='',null=True,blank=True)
    pin=models.CharField(max_length=100,default='',null=True,blank=True)
    address=models.CharField(max_length=100,default='',null=True,blank=True)
    city=models.CharField(max_length=100,default='',null=True,blank=True)
    state=models.CharField(max_length=100,default='',null=True,blank=True)
    password=models.CharField(max_length=100,default='',null=True,blank=True)

    pan=models.FileField(upload_to="uploads",default='',null=True,blank=True)
    gst_certificate=models.FileField(upload_to="uploads",default='',null=True,blank=True)
    
    date=models.DateField(auto_now=True)
    otp=models.IntegerField(default=9241,null=True,blank=True)
    verification=models.CharField(max_length=100,default='Pending',null=True,blank=True)
    user_type=models.CharField(max_length=100,default="Buyer",null=True,blank=True)
    def __str__(self):
        return self.name

    
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200,default='',null=True,blank=True)
    maincategory=models.CharField(max_length=200,default='',null=True,blank=True)
    maincategory_slug=models.CharField(max_length=200,default='',null=True,blank=True)
    subcategory=models.CharField(max_length=200,default='',null=True,blank=True)
    subcategory_slug=models.CharField(max_length=200,default='',null=True,blank=True)
    brand=models.CharField(max_length=200,default='',null=True,blank=True)
    brand_slug=models.CharField(max_length=200,default='',null=True,blank=True)
    unit=models.CharField(max_length=200,default='',null=True,blank=True)
    unit_slug=models.CharField(max_length=200,default='',null=True,blank=True)
    weight=models.CharField(max_length=200,default='',null=True,blank=True)
    minimum_purchase_qty=models.IntegerField()
    tags=models.TextField(default='',null=True,blank=True)
    product_image=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    product_thumbnail=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    link_type=models.CharField(max_length=200,default='',null=True,blank=True)
    video_link=models.CharField(max_length=200,default='',null=True,blank=True)
    color=models.CharField(max_length=200,default='',null=True,blank=True)
    attribute=models.CharField(max_length=200,default='',null=True,blank=True)
    unit_price=models.CharField(max_length=200,default='',null=True,blank=True)
    discount_range=models.CharField(max_length=200,default='',null=True,blank=True)
    discount=models.CharField(max_length=200,default='',null=True,blank=True)
    qty=models.IntegerField(default=1,null=True,blank=True)
    sku=models.CharField(max_length=200,default='',null=True,blank=True)
    external_link=models.CharField(max_length=200,default='',null=True,blank=True)
    external_link_button_text=models.CharField(max_length=200,default='',null=True,blank=True)
    key_features=models.TextField(default='',null=True,blank=True)
    subcategory_specification=models.TextField(default='',null=True,blank=True)
    product_description=models.TextField(default='',null=True,blank=True)
    product_faq_title=models.TextField(default='',null=True,blank=True)
    product_faq_answer=models.TextField(default='',null=True,blank=True)
    pdf_specification=models.CharField(max_length=200,default='',null=True,blank=True)
    seo_meta_title=models.TextField(default='',null=True,blank=True)
    meta_description=models.TextField(default='',null=True,blank=True)
    meta_image=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    free_shipping=models.CharField(max_length=200,default='',null=True,blank=True)
    fat_rate=models.CharField(max_length=200,default='',null=True,blank=True)
    is_product_quality_multiply=models.CharField(max_length=200,default='',null=True,blank=True)
    low_stock_qty=models.CharField(max_length=200,default='',null=True,blank=True)
    hide_stock=models.CharField(max_length=200,default='',null=True,blank=True)
    cash_on_delivery=models.CharField(max_length=200,default='',null=True,blank=True)
    shipping_day=models.CharField(max_length=200,default='',null=True,blank=True)
    tax=models.CharField(max_length=200,default='',null=True,blank=True)
    def __str__(self):
        return str(self.name)




class Maincategory(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default='',null=True,blank=True)
    slug=models.CharField(max_length=100,default='',null=True,blank=True)
    image=models.ImageField(upload_to="uploads",default='',null=True,blank=True)


class Category(models.Model):
    id=models.AutoField(primary_key=True)
    maincategory=models.CharField(max_length=100,default='',null=True,blank=True)
    maincategory_slug=models.CharField(max_length=100,default='',null=True,blank=True)
    category_name=models.CharField(max_length=100,default='',null=True,blank=True)
    category_slug=models.CharField(max_length=100,default='',null=True,blank=True)
    image=models.ImageField(upload_to="uploads",default='',null=True,blank=True)

class Brand(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default='',null=True,blank=True)
    slug=models.CharField(max_length=100,default='',null=True,blank=True)
    image=models.ImageField(upload_to="uploads",default='',null=True,blank=True)