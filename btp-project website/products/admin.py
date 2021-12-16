from django.contrib import admin
from .models import Product
from .models import Link
from .models import Device
from .models import Option
admin.site.register(Product)
admin.site.register(Link)
admin.site.register(Device)
admin.site.register(Option)

# Register your models here.
