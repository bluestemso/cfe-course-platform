from cloudinary import CloudinaryImage
from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import Course, Lesson

class LessonInline(admin.StackedInline):
    model = Lesson
    readonly_fields = ['updated_at']
    extra = 0

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ['title', 'status', 'access']
    list_filter = ['status', 'access']
    fields = ['title', 'description', 'status', 'image', 'access', 'display_image', 'public_id']
    readonly_fields = ['display_image', 'public_id']

    def display_image(self, obj, *args, **kwargs):
        url = obj.image.url
        cloudinary_id = str(obj.image)
        cloudinary_html = CloudinaryImage(cloudinary_id).image(width=500)
        return format_html(cloudinary_html)

    display_image.short_description = 'Current Image'

# admin.site.register(Course)