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

########################### Second Admin Page ##############################

class PostAdminSite(admin.AdminSite):
    site_header = "Portfolio admin"
    site_title = "Portfolio Admin Portal"
    index_title = "Welcome to Portfolio"

post_admin_site = PostAdminSite(name='post_admin')
############################################ Porfolio ################################




MAX_OBJECTS = 2


class EducationInline(admin.StackedInline):
    model = Education
    max_num = 20
    extra = 1

class SpecializationInline(admin.StackedInline):
    model = Specialization
    max_num = 20
    extra = 1

class SkillInline(admin.StackedInline):
    model = Skills
    max_num = 20
    extra = 1


class DontLog:
    def log_addition(self, *args):
        return
    def log_change(self, *args):
        return
    def log_deletion(self, *args):
        return

class AdminPortfolio(DontLog,admin.ModelAdmin):
    inlines = [EducationInline, SpecializationInline,SkillInline]

    def has_add_permission(self, request):
          if self.model.objects.count() >= MAX_OBJECTS:
               return False
          return super().has_add_permission(request)

post_admin_site.register(Portfolio,AdminPortfolio)



class ImagesInline(admin.StackedInline):
    model = ProjectImages
    max_num = 20
    extra = 1

class TechInline(admin.StackedInline):
    model = Technologies
    max_num = 20
    extra = 1


class AdminProject(DontLog,admin.ModelAdmin):
    inlines = [ImagesInline, TechInline]

    def has_add_permission(self, request):
          if self.model.objects.count() >= MAX_OBJECTS:
               return False
          return super().has_add_permission(request)

post_admin_site.register(Project,AdminProject)





