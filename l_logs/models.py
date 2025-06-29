from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    """Topic that user learning"""

    text = models.CharField(max_length=255, verbose_name="Topic name")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Owner")

    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = "Topics"

    def __str__(self):
        return self.text
    
class Entry(models.Model):
    """Дописи за темами"""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name="Topic")
    text = models.TextField(verbose_name="Text")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Created")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.text if len(self.text) <= 50 else f"{self.text[:50]}..."