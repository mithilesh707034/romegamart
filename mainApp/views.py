from django.shortcuts import render,HttpResponse,redirect
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from .models import *
from .serializers import *
import json
import io
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from random import randrange
from django.conf import settings
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# from romegamart.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY
import razorpay
from django.http.request import HttpHeaders
from django.shortcuts import render
import requests

#Email
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

#Slug
from django.utils.text import slugify
import re

def convert_slugify(slug):
    # Remove any non-alphanumeric characters and convert to lowercase
    clean_slug = re.sub(r'[^a-zA-Z0-9]+', '-', slug.lower())
    
    # Remove leading and trailing dashes
    clean_slug = clean_slug.strip('-')
    
    return clean_slug

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
    msg=''
    if (Request.method == "POST"):
        email = Request.POST.get("email")
        password = Request.POST.get("password")
        user = authenticate(username=email, password=password)
        if (user is not None):
            login(Request, user)
            if (user.is_superuser):
                return redirect("/admin-home")
            else:
                return redirect("/user-dashboard")
        
        else:
            msg="Invalid Email or Password!!!!"
    return render(Request, "front/login.html",{'msg':msg})
    

def buyer_registration_page(Request):
    msg=""
    uname=User.objects.all()
    if (Request.method == "POST"):
            p=Request.POST.get('password')
            b = Buyer()
            b.name = Request.POST.get("name")
            b.email = Request.POST.get("email")
            b.phone = Request.POST.get("phone")
            b.address = Request.POST.get("address")
            b.pin=Request.POST.get("pin")
            b.city = Request.POST.get("city")
            b.address = Request.POST.get("address")
            b.password = Request.POST.get("password")

            b.aadhar = Request.FILES.get("aadhar")
            b.pan = Request.FILES.get("pan")
            b.cancelled_check = Request.FILES.get("cancelled_check")
            b.password = p
            try:
                u=Buyer.objects.get(email=b.email)
                if(u):
                 pass
            except:
                
                   user = User(username=b.email)
                   if (user):
                       user.set_password(p)
                       user.save()
                       b.save()
                       msg="Done"
                    #    subject ='Your Account Has Been Successfully Created: Team RO Megamart'
                    #    message ="Dear "+b.name+"\n\n We are delighted to inform you that your Seller Account has been successfully created with Team RO Megamart. We extend our heartfelt gratitude for choosing our platform to access our latest range of products.\n\n Your account details are as follows: \n\n Username: "+b.email +"\n Password:"+p+" \n\n With your new account, you can now explore and purchase our latest products, accessing a wide array of offerings. \n\n If you have any questions or require assistance, please don't hesitate to reach out to our customer support team. We are dedicated to providing you with the best service and ensuring a seamless shopping experience. \n\n Thank you for being a part of Team RO Megamart. We look forward to serving you with utmost satisfaction.\n \n Best regards,\n Team RO Megamart."
                    #    email_from = settings.EMAIL_HOST_USER
                    #    recipient_list = [b.email ]
                    #    send_mail( subject, message, email_from, recipient_list )
    return render(Request,"front/registration.html",{'uname':uname,'msg':msg})



def seller_registration_page(Request):
    msg=""
    uname=User.objects.all()
    if (Request.method == "POST"):
            p=Request.POST.get('password')
            b = Seller()
            b.name = Request.POST.get("name")
            b.email = Request.POST.get("email")
            b.phone = Request.POST.get("phone")
            b.company_name = Request.POST.get("company_name")
            b.company_slug=convert_slugify(b.company_name)
            b.brand_name = Request.POST.get("brand_name")
            b.brand_slug=convert_slugify(b.brand_name)
            b.address = Request.POST.get("address")
            b.password = Request.POST.get("password")

            b.alternate_phone = Request.POST.get("alternate_phone")
            b.photo = Request.FILES.get("photo")
            b.gst_certificate = Request.FILES.get("gst_certificate")
            b.udhyam_certificate = Request.FILES.get("udhyam_certificate")
            b.cancelled_check = Request.FILES.get("cancelled_check")
            b.pan_card = Request.FILES.get("pan_card")
            b.aadhar_card = Request.FILES.get("aadhar_card")
            b.password = p
            try:
                u=Seller.objects.get(email=b.email)
                if(u):
                 pass
            except:
                
                   user = User(username=b.email)
                   if (user):
                       user.set_password(p)
                       user.save()
                       b.save()
                       msg="Done"
                       subject ='Your Account Has Been Successfully Created: Team RO Megamart'
                       message ="Dear "+b.name+"\n\n We are delighted to inform you that your Seller Account has been successfully created with Team RO Megamart. We extend our heartfelt gratitude for choosing our platform to access our latest range of products.\n\n Your account details are as follows: \n\n Username: "+b.email +"\n Password:"+p+" \n\n With your new account, you can now explore and purchase our latest products, accessing a wide array of offerings. \n\n If you have any questions or require assistance, please don't hesitate to reach out to our customer support team. We are dedicated to providing you with the best service and ensuring a seamless shopping experience. \n\n Thank you for being a part of Team RO Megamart. We look forward to serving you with utmost satisfaction.\n \n Best regards,\n Team RO Megamart."
                       email_from = settings.EMAIL_HOST_USER
                       recipient_list = [b.email ]
                       send_mail( subject, message, email_from, recipient_list )
    return render(Request,"seller/create.html",{'uname':uname,'msg':msg})



def seller_login_page(Request):
    msg=''
    if (Request.method == "POST"):
        email = Request.POST.get("email")
        password = Request.POST.get("password")
        user = authenticate(username=email, password=password)
        if (user is not None):
            login(Request, user)
            if (user.is_superuser):
                return redirect("/admin-home")
            else:
                return redirect("/seller-dashboard")
        
        else:
            msg="Invalid Email or Password!!!!"
    return render(Request, "seller/login.html",{'msg':msg})


def seller_logout_page(Request):
    logout(Request) 
    return redirect("/seller/login")


def seller_product_page(Request):
    return render(Request,'seller/seller-product.html')



#App Code Start Here
@csrf_exempt
def app_user_login(Request):
     if (Request.method=="POST"):
          phone=Request.POST.get('phone')
          try:
               try:
                  data=Buyer.objects.get(phone=phone)
                  if(data):
                    dataSerializer=BuyerSerializer(data,many=False)
                    realData={'status':True,'message':"User found successfully...",'data':[dataSerializer.data]}
                    return HttpResponse(json.dumps(realData),content_type="application/json")
               except:
                 data=Seller.objects.get(phone=phone)
                 if(data):
                   dataSerializer=SellerSerializer(data,many=False)
                   realData={'status':True,'message':"User found successfully...",'data':[dataSerializer.data]}
                   return HttpResponse(json.dumps(realData),content_type="application/json")
          except:
               msg={'status':False,'message':"User not found..."}
               jsonData=JSONRenderer().render(msg)
               return HttpResponse(jsonData,content_type="application/json")

@csrf_exempt
def app_buyer_registration(Request):
    if (Request.method == "POST"):
            b = Buyer()
            b.name = Request.POST.get("name")
            b.email = Request.POST.get("email")
            b.phone = Request.POST.get("phone")
            b.address = Request.POST.get("address")
            b.pin=Request.POST.get("pin")
            b.city = Request.POST.get("city")
            b.state = Request.POST.get("state")
            b.address = Request.POST.get("address")
            b.password="12345"
            b.pan = Request.FILES.get("pan")
            b.gst_certificate = Request.FILES.get("gst_certificate")
            try:
                u=User.objects.get(username=b.phone)
                if(u):
                    msg={'status':False,'message':"User already exist ..."}
                    jsonData=JSONRenderer().render(msg)
                    return HttpResponse(jsonData,content_type="application/json")
            except:
                
                   user = User(username=b.phone)
                   if (user):
                       user.set_password(b.password)
                       user.save()
                       b.save()
                       msg={'status':True,'message':"Buyer added successfully ..."}
                       jsonData=JSONRenderer().render(msg)  
                       return HttpResponse(jsonData,content_type="application/json")  



@csrf_exempt
def app_update_buyer_profile(Request):
    if (Request.method == "POST"):
            phone = Request.POST.get("phone")
            b=Buyer.objects.get(phone=phone)
            b.name = Request.POST.get("name")
            b.email = Request.POST.get("email")
            b.phone = Request.POST.get("phone")
            b.address = Request.POST.get("address")
            b.pin=Request.POST.get("pin")
            b.city = Request.POST.get("city")
            b.state = Request.POST.get("state")
            b.address = Request.POST.get("address")
            if(Request.FILES.get("pan")):
               b.pan = Request.FILES.get("pan")
            if(Request.FILES.get("gst_certificate")):
               b.gst_certificate = Request.FILES.get("gst_certificate")
            b.save()
            msg={'status':True,'message':"Kyc updated successfully ..."}
            jsonData=JSONRenderer().render(msg)
            return HttpResponse(jsonData,content_type="application/json")        


@csrf_exempt
def app_get_maincategory(Request):
     
    data=Maincategory.objects.all()
    if(data):
      dataSerializer=MaincategorySerializer(data,many=True)
      realData={'status':True,'message':"Data found successfully...",'data':dataSerializer.data}
      return HttpResponse(json.dumps(realData),content_type="application/json")
               
    else:
        msg={'status':False,'message':"Data not found..."}
        jsonData=JSONRenderer().render(msg)
        return HttpResponse(jsonData,content_type="application/json")


@csrf_exempt
def app_get_category(Request):
     
    data=Category.objects.all()
    if(data):
      dataSerializer=CategorySerializer(data,many=True)
      realData={'status':True,'message':"Data found successfully...",'data':dataSerializer.data}
      return HttpResponse(json.dumps(realData),content_type="application/json")
               
    else:
        msg={'status':False,'message':"Data not found..."}
        jsonData=JSONRenderer().render(msg)
        return HttpResponse(jsonData,content_type="application/json")



@csrf_exempt
def app_get_brand(Request):
     
    data=Brand.objects.all()
    if(data):
      dataSerializer=BrandSerializer(data,many=True)
      realData={'status':True,'message':"Data found successfully...",'data':dataSerializer.data}
      return HttpResponse(json.dumps(realData),content_type="application/json")
               
    else:
        msg={'status':False,'message':"Data not found..."}
        jsonData=JSONRenderer().render(msg)
        return HttpResponse(jsonData,content_type="application/json")



@csrf_exempt
def app_get_product(Request):
     
    data=Product.objects.all()
    if(data):
      dataSerializer=ProductSerializer(data,many=True)
      realData={'status':True,'message':"Product found successfully...",'data':dataSerializer.data}
      return HttpResponse(json.dumps(realData),content_type="application/json")
               
    else:
        msg={'status':False,'message':"Product not found..."}
        jsonData=JSONRenderer().render(msg)
        return HttpResponse(jsonData,content_type="application/json")



@csrf_exempt
def app_get_product_details(Request):
     if (Request.method=="POST"):
          id=Request.POST.get('id')
          try:
    
            data=Product.objects.get(id=id)
            if(data):
              dataSerializer=ProductSerializer(data,many=False)
              realData={'status':True,'message':"Data found successfully...",'data':[dataSerializer.data]}
              return HttpResponse(json.dumps(realData),content_type="application/json")
               
          except:
               msg={'status':False,'message':"Data not found..."}
               jsonData=JSONRenderer().render(msg)
               return HttpResponse(jsonData,content_type="application/json")
