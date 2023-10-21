from django.db import models


# Create your models here.

class AdhyatmType(models.Model):
    type = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.type


class AdhyatmJagat(models.Model):
    type = models.ForeignKey(AdhyatmType, on_delete=models.PROTECT)
    name = models.CharField(max_length=1000, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    contact_person = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.TextField(null=True, blank=True)
    main_image = models.ImageField(upload_to='adhyatm_jagat_image', null=True, blank=True)

    def __str__(self):
        return self.name
