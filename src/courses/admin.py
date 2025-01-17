import helpers
from cloudinary import CloudinaryImage
from django.contrib import admin
from django.utils.html import format_html

from .models import Course, Lesson

class LessonInline(admin.StackedInline):
    model = Lesson
    fields = ['title', 'public_id', 'description', 'status', 'thumbnail', 'video', 'order', 'can_preview', 'display_image', 'display_video']
    readonly_fields = ['updated_at', 'public_id', 'display_image', 'display_video']
    extra = 0

    def display_image(self, obj, *args, **kwargs):
        url = helpers.get_cloudinary_image_object(
            obj, 
            field_name="thumbnail",
            width=200)
        return format_html(f'<img src="{url}" />')

    display_image.short_description = 'Current Thumbnail'
    
    def display_video(self, obj, *args, **kwargs):
        video_embed_html = helpers.get_cloudinary_video_object(
            obj, 
            field_name="video",
            as_html=True,
            width=550)
        return video_embed_html

    display_video.short_description = 'Current Video'

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ['title', 'public_id', 'status', 'access']
    list_filter = ['status', 'access']
    fields = ['title', 'public_id', 'description', 'status', 'image', 'access', 'display_image']
    readonly_fields = ['display_image', 'public_id']

    def display_image(self, obj, *args, **kwargs):
        url = obj.image.url
        cloudinary_id = str(obj.image)
        cloudinary_html = CloudinaryImage(cloudinary_id).image(width=500)
        return format_html(cloudinary_html)

    display_image.short_description = 'Current Image'

# admin.site.register(Course)