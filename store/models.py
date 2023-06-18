from django.db import models

# Create your models here.
class StoreType(models.Model):
    type = models.CharField(max_length=100,null=True)
    desc = models.TextField(null=True)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type


class Store(models.Model):
    store_type = models.ForeignKey(StoreType,on_delete=models.PROTECT)
    store_name = models.CharField(max_length=1000,null=True)
    desc = models.TextField(null=True)

    add = models.TextField(null=True)
    email = models.EmailField(null=True)
    mobile = models.CharField(max_length=20,null=True)
    phone = models.CharField(max_length=20,null=True)

    timing_from1 = models.CharField(max_length=50)
    timing_to1 = models.CharField(max_length=50)

    timing_from2 = models.CharField(max_length=50)
    timing_to2 = models.CharField(max_length=50)

    holiday = models.CharField(max_length=500,null=True)
    owner_name = models.CharField(max_length=500,null=True)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.store_name





