from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(AboutHeader)
admin.site.register(AboutHeader_2)
admin.site.register(Instructor)
admin.site.register(Solution)
MAX_OBJECTS = 1

@admin.register(About)
class AdminAbout(admin.ModelAdmin):

    def has_add_permission(self, request):
          if self.model.objects.count() >= MAX_OBJECTS:
               return False
          return super().has_add_permission(request)

@admin.register(GeneralSettings)
class AdminGeneralSettings(admin.ModelAdmin):

    def has_add_permission(self, request):
          if self.model.objects.count() >= MAX_OBJECTS:
               return False
          return super().has_add_permission(request)
    

