from django.contrib import admin

from myapp.models import Consume, Food

# Register your models here.
admin.site.register(Food)
admin.site.register(Consume)