from django.contrib import admin
from .models import *

# Register your models here.
   

class department_display(admin.ModelAdmin):
    list_display=['dep_name']
class batch_display(admin.ModelAdmin):
    list_display=['batch_time']
class student_display(admin.ModelAdmin):
    list_display=['std_name','address','dep']
admin.site.register(department,department_display)
admin.site.register(batch,batch_display)
admin.site.register(students,student_display)

