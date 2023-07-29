from django.db import models


# Create your models here.
class StoreType(models.Model):
    type = models.CharField(max_length=100, null=True)
    desc = models.TextField(null=True)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type


class Store(models.Model):
    store_type = models.ForeignKey(StoreType, on_delete=models.PROTECT)
    store_name = models.CharField(max_length=1000, null=True)
    description = models.TextField(null=True, blank=True)

    address = models.TextField(null=True)
    website = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True)

    timing_from1 = models.CharField(max_length=50, null=True, blank=True)
    timing_to1 = models.CharField(max_length=50, null=True, blank=True)

    timing_from2 = models.CharField(max_length=50, null=True, blank=True)
    timing_to2 = models.CharField(max_length=50, null=True, blank=True)

    holiday = models.CharField(max_length=500, null=True, blank=True)
    owner_name = models.CharField(max_length=500, null=True, blank=True)

    date = models.DateTimeField(auto_now_add=True)

    main_image = models.ImageField(upload_to='store_image', null=True, blank=True)

    other_image1 = models.ImageField(upload_to='store_image', null=True, blank=True)
    other_image2 = models.ImageField(upload_to='store_image', null=True, blank=True)

    def __str__(self):
        return self.store_name
