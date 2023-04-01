from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BlogPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    participants = models.ManyToManyField(User, related_name="blog_participants")

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title