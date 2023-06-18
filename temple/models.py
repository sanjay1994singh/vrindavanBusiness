from django.db import models

# Create your models here.
class Temple(models.Model):
    name = models.CharField(max_length=500,null=True,unique=True)
    add = models.TextField(null=True)
    created_at = models.DateTimeField()
    devi_devta = models.CharField(max_length=200,null=True)
    sevayat_name = models.CharField(max_length=500,null=True)
    mandir_prabandhak = models.CharField(max_length=1000,null=True)
    darshan_time = models.CharField(max_length=50,null=True)
    arti1_time = models.CharField(max_length=50,null=True)
    arti2_time = models.CharField(max_length=50,null=True)
    arti3_time = models.CharField(max_length=50,null=True)
    arti4_time = models.CharField(max_length=50,null=True)

    mobile = models.CharField(max_length=20,null=True)
    phone = models.CharField(max_length=20,null=True)
    email = models.EmailField(null=True)
    
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

