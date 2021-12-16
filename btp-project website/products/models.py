from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):

    title=models.CharField(max_length=255)
    device11=models.FloatField(default=0)
    device12=models.FloatField(default=0)
    device13=models.FloatField(default=0, null=False)
    switch11=models.FloatField(default=0)
    switch12=models.FloatField(default=0)
    device21=models.FloatField(default=0)
    device22=models.FloatField(default=0)
    device23=models.FloatField(default=0)
    switch21=models.FloatField(default=0)
    switch22=models.FloatField(default=0)
    device31=models.FloatField(default=0)
    device32=models.FloatField(default=0)
    device33=models.FloatField(default=0)
    switch31=models.FloatField(default=0)
    switch32=models.FloatField(default=0)
    pub_date=models.DateTimeField()
    hunter=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Link(models.Model):
    title=models.CharField(max_length=255)
    room1_upload_link=models.TextField()
    room1_download_link=models.TextField()
    room1_id=models.FloatField()
    room2_upload_link=models.TextField()
    room2_download_link=models.TextField()
    room2_id=models.FloatField()
    room3_upload_link=models.TextField()
    room3_download_link=models.TextField()
    room3_id=models.FloatField()
    pub_date=models.DateTimeField()
    hunter=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Device(models.Model):
    title=models.CharField(max_length=255)
    device11_name=models.CharField(max_length=255)
    device12_name=models.CharField(max_length=255)
    device13_name=models.CharField(max_length=255)
    switch11_name=models.CharField(max_length=255)
    switch12_name=models.CharField(max_length=255)
    device21_name=models.CharField(max_length=255)
    device22_name=models.CharField(max_length=255)
    device23_name=models.CharField(max_length=255)
    switch21_name=models.CharField(max_length=255)
    switch22_name=models.CharField(max_length=255)
    device31_name=models.CharField(max_length=255)
    device32_name=models.CharField(max_length=255)
    device33_name=models.CharField(max_length=255)
    switch31_name=models.CharField(max_length=255)
    switch32_name=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    hunter=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class Option(models.Model):
    title=models.CharField(max_length=255)
    option11=models.FloatField(default=0)
    option12=models.FloatField(default=0)
    option13=models.FloatField(default=0)
    option21=models.FloatField(default=0)
    option22=models.FloatField(default=0)
    option23=models.FloatField(default=0)
    option31=models.FloatField(default=0)
    option32=models.FloatField(default=0)
    option33=models.FloatField(default=0)
    pub_date=models.DateTimeField()
    hunter=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
