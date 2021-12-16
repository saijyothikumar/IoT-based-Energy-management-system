from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from .models import Link
from .models import Device
from .models import Option
import requests
import sqlite3
import math
import urllib.request
import time
import threading
import random
from django .utils import timezone
# Create your views here.
def index(request):
    return render(request,'products/index.html')

def error(request):
    return render(request,'products/error.html')

@login_required(login_url="/accounts/login")
def home(request):
    device = Device.objects.filter(title=request.user.username).last()
    product = Product.objects.filter(title=request.user.username).last()
    option= Option.objects.filter(title=request.user.username).last()
    return render(request,'products/home.html',{'product':product,'device':device,'option':option})
def detail1(request):
    if Link.objects.filter(title=request.user.username).last()==None or Device.objects.filter(title=request.user.username).last()==None:
        return render(request,'products/addlink.html',{'error':'links and device names are required'})
    else:
        device = Device.objects.filter(title=request.user.username).last()
        product = Product.objects.filter(title=request.user.username).last()
        link= Link.objects.filter(title=request.user.username).last()
        option= Option.objects.filter(title=request.user.username).last()
        initial="https://thingspeak.com/channels/"
        final1="/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"
        final2="/charts/2?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"
        final3="/charts/3?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"
        final4="/charts/4?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"
        final5="/charts/5?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"
        final6="/charts/6?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"
        final7="/charts/7?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"
        final8="/charts/8?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"
        id2=str(int(link.room2_id))
        id1=str(int(link.room1_id))
        img_linK_1=initial+id1+final1
        img_linK_2=initial+id1+final2
        img_linK_3=initial+id1+final3
        img_linK_4=initial+id1+final4
        img_linK_5=initial+id1+final5
        img_linK_6=initial+id1+final6
        img_linK_7=initial+id1+final7
        img_linK_8=initial+id2+final8
        return render(request,'products/detail1.html',{'product':product,'device':device,'link':link,'option':option,'img_linK_1':img_linK_1,'img_linK_2':img_linK_2,'img_linK_3':img_linK_3,'img_linK_4':img_linK_4,'img_linK_5':img_linK_5,'img_linK_6':img_linK_6,'img_linK_7':img_linK_7,'img_linK_8':img_linK_8})
def detail2(request):
    if Link.objects.filter(title=request.user.username).last()==None or Device.objects.filter(title=request.user.username).last()==None:
        return render(request,'products/addlink.html',{'error':'links and device names are required'})
    else:
        device = Device.objects.filter(title=request.user.username).last()
        product = Product.objects.filter(title=request.user.username).last()
        link= Link.objects.filter(title=request.user.username).last()
        option= Option.objects.filter(title=request.user.username).last()
        initial="https://thingspeak.com/channels/"
        final1="/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"
        final2="/charts/2?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"
        final3="/charts/3?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"
        final4="/charts/4?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"
        final5="/charts/5?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"
        final6="/charts/6?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"
        final7="/charts/7?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"
        id1=str(int(link.room2_id))
        img_linK_1=initial+id1+final1
        img_linK_2=initial+id1+final2
        img_linK_3=initial+id1+final3
        img_linK_4=initial+id1+final4
        img_linK_5=initial+id1+final5
        img_linK_6=initial+id1+final6
        img_linK_7=initial+id1+final7
        return render(request,'products/detail2.html',{'product':product,'device':device,'link':link,'option':option,'img_linK_1':img_linK_1,'img_linK_2':img_linK_2,'img_linK_3':img_linK_3,'img_linK_4':img_linK_4,'img_linK_5':img_linK_5,'img_linK_6':img_linK_6,'img_linK_7':img_linK_7})
def detail3(request):
    if Link.objects.filter(title=request.user.username).last()==None or Device.objects.filter(title=request.user.username).last()==None:
        return render(request,'products/addlink.html',{'error':'links and device names are required'})
    else:
        device = Device.objects.filter(title=request.user.username).last()
        product = Product.objects.filter(title=request.user.username).last()
        link= Link.objects.filter(title=request.user.username).last()
        option= Option.objects.filter(title=request.user.username).last()
        initial="https://thingspeak.com/channels/"
        final1="/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"
        final2="/charts/2?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"
        final3="/charts/3?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"
        final4="/charts/4?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"
        final5="/charts/5?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"
        final6="/charts/6?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"
        final7="/charts/7?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"
        id1=str(int(link.room3_id))
        img_linK_1=initial+id1+final1
        img_linK_2=initial+id1+final2
        img_linK_3=initial+id1+final3
        img_linK_4=initial+id1+final4
        img_linK_5=initial+id1+final5
        img_linK_6=initial+id1+final6
        img_linK_7=initial+id1+final7
        return render(request,'products/detail3.html',{'product':product,'device':device,'link':link,'option':option,'img_linK_1':img_linK_1,'img_linK_2':img_linK_2,'img_linK_3':img_linK_3,'img_linK_4':img_linK_4,'img_linK_5':img_linK_5,'img_linK_6':img_linK_6,'img_linK_7':img_linK_7})
@login_required(login_url="/accounts/login")
def addlink(request):
    if request.method=='POST':
        if request.POST['room1_download_link'] and request.POST['room1_upload_link'] and request.POST['room1_id'] and request.POST['room2_upload_link'] and request.POST['room2_download_link'] and request.POST['room2_id'] and request.POST['room3_upload_link'] and request.POST['room3_download_link'] and request.POST['room3_id']:
            link=Link()
            link.title=request.user.username
            link.room1_upload_link=request.POST['room1_upload_link']
            link.room1_download_link=request.POST['room1_download_link']
            link.room1_id=request.POST['room1_id']
            link.room2_upload_link=request.POST['room2_upload_link']
            link.room2_download_link=request.POST['room2_download_link']
            link.room2_id=request.POST['room2_id']
            link.room3_upload_link=request.POST['room3_upload_link']
            link.room3_download_link=request.POST['room3_download_link']
            link.room3_id=request.POST['room3_id']
            link.hunter=request.user
            link.pub_date=timezone.datetime.now()
            link.save()
            return redirect('home')
        else:
            return render(request,'products/addlink.html',{'error':'all fields are required'})
    else:
        return render(request,'products/addlink.html')

@login_required(login_url="/accounts/login")
def addname(request):
    if request.method=='POST':
        if request.POST['device11'] and request.POST['device12'] and request.POST['device13'] and request.POST['switch11'] and request.POST['switch12'] and request.POST['device21'] and request.POST['device22'] and request.POST['device23'] and request.POST['switch21'] and request.POST['switch22'] and request.POST['device31'] and request.POST['device32'] and request.POST['device33'] and request.POST['switch31'] and request.POST['switch32']:
            device=Device()
            device.title=request.user.username
            device.device11_name=request.POST['device11']
            device.device12_name=request.POST['device12']
            device.device13_name=request.POST['device13']
            device.switch11_name=request.POST['switch11']
            device.switch12_name=request.POST['switch12']
            device.device21_name=request.POST['device21']
            device.device22_name=request.POST['device22']
            device.device23_name=request.POST['device23']
            device.switch21_name=request.POST['switch21']
            device.switch22_name=request.POST['switch22']
            device.device31_name=request.POST['device31']
            device.device32_name=request.POST['device32']
            device.device33_name=request.POST['device33']
            device.switch31_name=request.POST['switch31']
            device.switch32_name=request.POST['switch32']
            device.pub_date=timezone.datetime.now()
            device.hunter=request.user
            device.save()
            return redirect('home')
        else:
            return render(request,'products/addname.html',{'error':'all fields are required'})
    else:
        return render(request,'products/addname.html')


@login_required(login_url="/accounts/signup")
def update(request):
    product = Product()
    product.title = request.user.username
    option = Option.objects.filter(title=request.user.username).last()
    if request.method == 'POST':
        if Link.objects.filter(title=request.user.username).last()==None or Device.objects.filter(title=request.user.username).last()==None:
            return render(request,'products/addlink.html',{'error':'links and device names are required'})
        else:
            r1=requests.get(Link.objects.filter(title=request.user.username).last().room1_download_link)
            print(Link.objects.filter(title=request.user.username).last().room1_download_link)
            data1=r1.json()
            product.device11=data1['feeds'][0]['field1']
            print(product.device11)
            product.device12=data1['feeds'][0]['field2']
            product.device13=data1['feeds'][0]['field3']
            print(product.device13)

            r2=requests.get(Link.objects.filter(title=request.user.username).last().room2_download_link)
            data2=r2.json()
            product.device21=data2['feeds'][0]['field1']
            product.device22=data2['feeds'][0]['field2']
            product.device23=data2['feeds'][0]['field3']
            option.option23 = data2['feeds'][0]['field8']
            print("total pow used: ")
            print(option.option23)

            r3=requests.get(Link.objects.filter(title=request.user.username).last().room3_download_link)
            data3=r3.json()
            product.device31=data3['feeds'][0]['field1']
            product.device32=data3['feeds'][0]['field2']
            product.device33=data3['feeds'][0]['field3']

            product.pub_date=timezone.datetime.now()
            product.hunter=request.user
            product.save()
            option.save()
            return redirect('home')


@login_required(login_url="/accounts/signup")
def son11(request):
    if request.method == 'POST':
        if Link.objects.filter(title=request.user.username).last()==None or Device.objects.filter(title=request.user.username).last()==None:
            return render(request,'products/addlink.html',{'error':'links and device names are required'})
        else:
            product = Product.objects.filter(title=request.user.username).last()
            product.switch11 = 1
            product.save()
            on11=product.switch11
            URL=Link.objects.filter(title=request.user.username).last().room1_upload_link
            conn=urllib.request.urlopen(URL+"&field4=%d" %(on11))
            return redirect('home')
def son12(request):
    if request.method == 'POST':
        if Link.objects.filter(title=request.user.username).last()==None or Device.objects.filter(title=request.user.username).last()==None:
            return render(request,'products/addlink.html',{'error':'links and device names are required'})
        else:
            product = Product.objects.filter(title=request.user.username).last()
            product.switch12 = 1
            product.save()
            on12=product.switch12
            URL=Link.objects.filter(title=request.user.username).last().room1_upload_link
            conn=urllib.request.urlopen(URL+"&field5=%d" %(on12))
            return redirect('home')
def son21(request):
    if request.method == 'POST':
        if Link.objects.filter(title=request.user.username).last()==None or Device.objects.filter(title=request.user.username).last()==None:
            return render(request,'products/addlink.html',{'error':'links and device names are required'})
        else:
            product = Product.objects.filter(title=request.user.username).last()
            product.switch21 = 1
            product.save()
            on21=product.switch21
            URL=Link.objects.filter(title=request.user.username).last().room2_upload_link
            conn=urllib.request.urlopen(URL+"&field4=%d" %(on21))
            return redirect('home')

def son22(request):
    if request.method == 'POST':
        if Link.objects.filter(title=request.user.username).last()==None or Device.objects.filter(title=request.user.username).last()==None:
            return render(request,'products/addlink.html',{'error':'links and device names are required'})
        else:
            product = Product.objects.filter(title=request.user.username).last()
            product.switch22 = 1
            product.save()
            on22=product.switch22
            URL=Link.objects.filter(title=request.user.username).last().room2_upload_link
            conn=urllib.request.urlopen(URL+"&field5=%d" %(on22))
            return redirect('home')
def son31(request):
    if request.method == 'POST':
        if Link.objects.filter(title=request.user.username).last()==None or Device.objects.filter(title=request.user.username).last()==None:
            return render(request,'products/addlink.html',{'error':'links and device names are required'})
        else:
            product = Product.objects.filter(title=request.user.username).last()
            product.switch31 = 1
            product.save()
            on31=product.switch31
            URL=Link.objects.filter(title=request.user.username).last().room3_upload_link
            conn=urllib.request.urlopen(URL+"&field4=%d" %(on31))
            return redirect('home')
def son32(request):
    if request.method == 'POST':
        if Link.objects.filter(title=request.user.username).last()==None or Device.objects.filter(title=request.user.username).last()==None:
            return render(request,'products/addlink.html',{'error':'links and device names are required'})
        else:
            product = Product.objects.filter(title=request.user.username).last()
            product.switch32 = 1
            product.save()
            on32=product.switch32
            URL=Link.objects.filter(title=request.user.username).last().room3_upload_link
            conn=urllib.request.urlopen(URL+"&field5=%d" %(on32))
            return redirect('home')
def soff11(request):
    if request.method == 'POST':
        if Link.objects.filter(title=request.user.username).last()==None or Device.objects.filter(title=request.user.username).last()==None:
            return render(request,'products/addlink.html',{'error':'links and device names are required'})
        else:
            product = Product.objects.filter(title=request.user.username).last()
            product.switch11 = 0
            product.save()
            print(product.switch11)
            off11=product.switch11
            URL=Link.objects.filter(title=request.user.username).last().room1_upload_link
            conn=urllib.request.urlopen(URL+"&field4=%d" %(off11))
            return redirect('home')
def soff12(request):
    if request.method == 'POST':
        if Link.objects.filter(title=request.user.username).last()==None or Device.objects.filter(title=request.user.username).last()==None:
            return render(request,'products/addlink.html',{'error':'links and device names are required'})
        else:
            product = Product.objects.filter(title=request.user.username).last()
            product.switch12 = 0
            product.save()
            off12=product.switch12
            URL=Link.objects.filter(title=request.user.username).last().room1_upload_link
            conn=urllib.request.urlopen(URL+"&field5=%d" %(off12))
            return redirect('home')
def soff21(request):
    if request.method == 'POST':
        if Link.objects.filter(title=request.user.username).last()==None or Device.objects.filter(title=request.user.username).last()==None:
            return render(request,'products/addlink.html',{'error':'links and device names are required'})
        else:
            product = Product.objects.filter(title=request.user.username).last()
            product.switch21 = 0
            product.save()
            off21=product.switch21
            URL=Link.objects.filter(title=request.user.username).last().room2_upload_link
            conn=urllib.request.urlopen(URL+"&field4=%d" %(off21))
            return redirect('home')

def soff22(request):
    if request.method == 'POST':
        if Link.objects.filter(title=request.user.username).last()==None or Device.objects.filter(title=request.user.username).last()==None:
            return render(request,'products/addlink.html',{'error':'links and device names are required'})
        else:
            product = Product.objects.filter(title=request.user.username).last()
            product.switch22 = 0
            product.save()
            off22=product.switch22
            URL=Link.objects.filter(title=request.user.username).last().room2_upload_link
            conn=urllib.request.urlopen(URL+"&field5=%d" %(off22))
            return redirect('home')
def soff31(request):
    if request.method == 'POST':
        if Link.objects.filter(title=request.user.username).last()==None or Device.objects.filter(title=request.user.username).last()==None:
            return render(request,'products/addlink.html',{'error':'links and device names are required'})
        else:
            product = Product.objects.filter(title=request.user.username).last()
            product.switch31 = 0
            product.save()
            off31=product.switch31
            URL=Link.objects.filter(title=request.user.username).last().room3_upload_link
            conn=urllib.request.urlopen(URL+"&field4=%d" %(off31))
            return redirect('home')
def soff32(request):
    if request.method == 'POST':
        if Link.objects.filter(title=request.user.username).last()==None or Device.objects.filter(title=request.user.username).last()==None:
            return render(request,'products/addlink.html',{'error':'links and device names are required'})
        else:
            product = Product.objects.filter(title=request.user.username).last()
            product.switch32 = 0
            product.save()
            off32=product.switch32
            URL=Link.objects.filter(title=request.user.username).last().room3_upload_link
            conn=urllib.request.urlopen(URL+"&field5=%d" %(off32))
            return redirect('home')
def temp1(request):
    if request.method == 'POST':
        if Link.objects.filter(title=request.user.username).last()==None or Device.objects.filter(title=request.user.username).last()==None:
            return render(request,'products/addlink.html',{'error':'links and device names are required'})
        else:
            if Option.objects.filter(title=request.user.username).last()==None:
                return render(request,'products/error.html',{'error':'please click on use switch button to set up'})
            else:
                option=Option.objects.filter(title=request.user.username).last()
                option.option11 = int(request.POST['temp1'])
                option.save()
                t1=option.option11
                URL=Link.objects.filter(title=request.user.username).last().room1_upload_link
                conn=urllib.request.urlopen(URL+"&field6=%d" %(t1))
                return redirect('home')
def temp2(request):
    if request.method == 'POST':
        if Link.objects.filter(title=request.user.username).last()==None or Device.objects.filter(title=request.user.username).last()==None:
            return render(request,'products/addlink.html',{'error':'links and device names are required'})
        else:
            if Option.objects.filter(title=request.user.username).last()==None:
                return render(request,'products/error.html',{'error':'please click on use switch button to set up'})
            else:
                option=Option.objects.filter(title=request.user.username).last()
                option.option21 = int(request.POST['temp2'])
                option.save()
                t2=option.option21
                URL=Link.objects.filter(title=request.user.username).last().room2_upload_link
                conn=urllib.request.urlopen(URL+"&field6=%d" %(t2))
                return redirect('home')
def temp3(request):
    if request.method == 'POST':
        if Link.objects.filter(title=request.user.username).last()==None or Device.objects.filter(title=request.user.username).last()==None:
            return render(request,'products/addlink.html',{'error':'links and device names are required'})
        else:
            if Option.objects.filter(title=request.user.username).last()==None:
                return render(request,'products/error.html',{'error':'please click on use switch button to set up'})
            else:
                option=Option.objects.filter(title=request.user.username).last()
                option.option31 = int(request.POST['temp3'])
                option.save()
                t3=option.option31
                URL=Link.objects.filter(title=request.user.username).last().room3_upload_link
                conn=urllib.request.urlopen(URL+"&field6=%d" %(t3))
                return redirect('home')
def int1(request):
    if request.method == 'POST':
        if Link.objects.filter(title=request.user.username).last()==None or Device.objects.filter(title=request.user.username).last()==None:
            return render(request,'products/addlink.html',{'error':'links and device names are required'})
        else:
            if Option.objects.filter(title=request.user.username).last()==None:
                return render(request,'products/error.html',{'error':'please click on use switch button to set up'})
            else:
                option=Option.objects.filter(title=request.user.username).last()
                option.option12 = int(request.POST['int1'])
                option.save()
                i1=option.option12
                URL=Link.objects.filter(title=request.user.username).last().room1_upload_link
                conn=urllib.request.urlopen(URL+"&field7=%d" %(i1))
                return redirect('home')
def int2(request):
    if request.method == 'POST':
        if Link.objects.filter(title=request.user.username).last()==None or Device.objects.filter(title=request.user.username).last()==None:
            return render(request,'products/addlink.html',{'error':'links and device names are required'})
        else:
            if Option.objects.filter(title=request.user.username).last()==None:
                return render(request,'products/error.html',{'error':'please click on use switch button to set up'})
            else:
                option=Option.objects.filter(title=request.user.username).last()
                option.option22 = int(request.POST['int2'])
                option.save()
                i2=option.option22
                URL=Link.objects.filter(title=request.user.username).last().room2_upload_link
                conn=urllib.request.urlopen(URL+"&field7=%d" %(i2))
                return redirect('home')
def int3(request):
    if request.method == 'POST':
        if Link.objects.filter(title=request.user.username).last()==None or Device.objects.filter(title=request.user.username).last()==None:
            return render(request,'products/addlink.html',{'error':'links and device names are required'})
        else:
            if Option.objects.filter(title=request.user.username).last()==None:
                return render(request,'products/error.html',{'error':'please click on use switch button to set up'})
            else:
                option=Option.objects.filter(title=request.user.username).last()
                option.option32 = int(request.POST['int3'])
                option.save()
                i3=option.option32
                URL=Link.objects.filter(title=request.user.username).last().room3_upload_link
                conn=urllib.request.urlopen(URL+"&field7=%d" %(i3))
                return redirect('home')
def controlon(request):
    if request.method == 'POST':
        if Link.objects.filter(title=request.user.username).last()==None or Device.objects.filter(title=request.user.username).last()==None:
            return render(request,'products/addlink.html',{'error':'links and device names are required'})
        else:
            option=Option()
            option.title = request.user.username
            option.option13 = 1
            option.pub_date=timezone.datetime.now()
            option.hunter=request.user
            option.save()
            c1=option.option13
            URL=Link.objects.filter(title=request.user.username).last().room1_upload_link
            conn=urllib.request.urlopen(URL+"&field8=%d" %(c1))
            return redirect('home')
def controloff(request):
    if request.method == 'POST':
        if Link.objects.filter(title=request.user.username).last()==None or Device.objects.filter(title=request.user.username).last()==None:
            return render(request,'products/addlink.html',{'error':'links and device names are required'})
        else:
            if Option.objects.filter(title=request.user.username).last()==None:
                return render(request,'products/error.html',{'error':'please click on use switch button to set up'})
            else:
                option=Option.objects.filter(title=request.user.username).last()
                option.option13 = 0
                option.save()
                c2=option.option13
                URL=Link.objects.filter(title=request.user.username).last().room1_upload_link
                conn=urllib.request.urlopen(URL+"&field8=%d" %(c2))
                return redirect('home')
