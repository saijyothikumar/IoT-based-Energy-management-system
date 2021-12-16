from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Review(models.Model):
    title=models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    appliance = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    body = models.TextField()
    buy_date=models.DateTimeField()
    pub_date=models.DateTimeField()
    rating=models.FloatField(default=1)
    hunter=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]
    def buy_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
