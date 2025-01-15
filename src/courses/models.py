import helpers
from django.db import models
from cloudinary.models import CloudinaryField


helpers.cloudinary_init()

# Create your models here.
class PublishStatus(models.TextChoices):
    PUBLISHED = 'pub', 'Published'
    COMING_SOON = 'coming_soon', 'Coming Soon'
    DRAFT = 'draft', 'Draft'

class AccessRequirement(models.TextChoices):
    ANYONE = 'any', 'Anyone'
    EMAIL_REQUIRED = 'email', 'Email Required'

def handle_upload(instance, filename):
    return f'{filename}'

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to=handle_upload, blank=True, null=True)
    image = CloudinaryField('image', blank=True, null=True)
    status = models.CharField(
        max_length=12, 
        choices=PublishStatus.choices, 
        default=PublishStatus.DRAFT)
    access = models.CharField(
        max_length=5, 
        choices=AccessRequirement.choices, 
        default=AccessRequirement.EMAIL_REQUIRED)
    
    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED

    def __str__(self):
        return self.title

