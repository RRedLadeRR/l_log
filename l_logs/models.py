from django.db import models

# Create your models here.

class Topic(models.Model):
    """Topic that user learning"""

    text = models.CharField(max_length=255, verbose_name="Topic name")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Created")

    def __str__(self):
        return self.text