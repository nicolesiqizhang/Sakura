from django.contrib import admin

# Register your models here.
from .models import Customer
from .models import Topic
from .models import Thread

admin.site.register(Customer)
admin.site.register(Topic)
admin.site.register(Thread)