from django.contrib import admin
from django.contrib.admin.options import TabularInline
from .models import Course, Tag, Prerequisite, Learning, Video, Payments, UserCourse

# Register your models here.


class VideoAdmin(admin.TabularInline):
    model = Video

class TagAdmin(admin.TabularInline):
    model = Tag

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

class LearningAdmin(admin.TabularInline):
    model = Learning
    

class AdminCourse(admin.ModelAdmin):
    #fields = ['name', 'description', 'price', 'active']
    list_display = ['name', 'description', 'price', 'active']
    inlines = [ TagAdmin, PrerequisiteAdmin, LearningAdmin, VideoAdmin]
    


admin.site.register(Course,AdminCourse)
admin.site.register(UserCourse)
admin.site.register(Payments)