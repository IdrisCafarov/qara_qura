from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Product)
admin.site.register(Contact)

MAX_OBJECTS = 1

@admin.register(About)
class AdminAbout(admin.ModelAdmin):

    def has_add_permission(self, request):
          if self.model.objects.count() >= MAX_OBJECTS:
               return False
          return super().has_add_permission(request)

