from django.contrib import admin

from .models import Bird

# Register your models here.
admin.site.register(Bird) # allow crud updates for our Cat table in our admin app
