from django.db import models

# Create your models here.
class PublishStatus(models.TextChoices):
    PUBLISHED = 'pub', 'Published'
    COMING_SOON = 'coming_soon', 'Coming Soon'
    DRAFT = 'draft', 'Draft'

class AccessRequirement(models.TextChoices):
    FREE = 'free', 'Free'
    PREMIUM = 'premium', 'Premium'

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='courses/images/', blank=True, null=True)
    status = models.CharField(
        max_length=10, 
        choices=PublishStatus.choices, 
        default=PublishStatus.DRAFT)
    access = models.CharField(
        max_length=10, 
        choices=AccessRequirement.choices, 
        default=AccessRequirement.FREE)
    
    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED

    def __str__(self):
        return self.title

