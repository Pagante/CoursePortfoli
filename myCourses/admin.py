from django.contrib import admin
from .models import MyCourse
from django.utils.html import format_html

# Register your models here.
class myCourseAdmin(admin.ModelAdmin):
    def Thumbnail(self, object):
        return format_html('<img src="{}" width="40px" style="border-radius:50%" />'.format(object.image.url))
        Thumbnail.short_description = 'Course Image'
    list_display = ('id','Thumbnail','course_title','description')
    list_display_link = ('id','Thumbnail','course_title','description')
admin.site.register(MyCourse, myCourseAdmin)
