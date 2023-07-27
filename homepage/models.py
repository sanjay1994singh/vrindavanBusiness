from django.db import models

# Create your models here.
class LookupField(models.Model):
    code = models.CharField(max_length=50, null=True, blank=True)
    tile = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='lookup_image', null=True, blank=True)
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.tile




