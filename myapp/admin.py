from django.contrib import admin

from myapp.models import Consume, Food, UserProfile

# Register your models here.
admin.site.register(Food)
admin.site.register(Consume)
admin.site.register(UserProfile)