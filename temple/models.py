from django.db import models

# Create your models here.
class Temple(models.Model):
    name = models.CharField(max_length=500,null=True,unique=True)
    address = models.TextField(null=True)
    deity = models.CharField(max_length=200,null=True)
    sewayat_name = models.CharField(max_length=500,null=True)
    mandir_manager = models.CharField(max_length=1000,null=True)
    darshan_time_summer = models.CharField(max_length=50,null=True)
    darshan_time_winter = models.CharField(max_length=50,null=True)
    # main_img = models.ImageField(upload_to='temple_image',null=True,default=None)
    arti1 = models.CharField(max_length=50,null=True, blank=True)
    arti2 = models.CharField(max_length=50,null=True, blank=True)
    arti3 = models.CharField(max_length=50,null=True, blank=True)
    arti4 = models.CharField(max_length=50,null=True, blank=True)

    contact_number = models.CharField(max_length=20,null=True)
    phone = models.CharField(max_length=20,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.TextField(blank=True)
    description = models.TextField(blank=True)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

