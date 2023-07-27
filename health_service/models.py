from django.db import models

# Create your models here.
class HealthType(models.Model):
    type = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.type

class HealthService(models.Model):
    type = models.ForeignKey(HealthType,on_delete=models.PROTECT)
    name = models.CharField(max_length=50,null=True)
    address = models.TextField(null=True)
    email = models.EmailField(null=True,blank=True, default='')
    website = models.URLField(null=True, blank=True, default='')
    opening_day = models.CharField(max_length=50,null=True, default='Monday-Saturday')
    holiday = models.CharField(max_length=50, null=True, default='Sunday', blank=True)
    emergency_cases = models.BooleanField(null=True,default=False, blank=True)
    emergency_time = models.CharField(max_length=50, null=True, default='24 hours', blank=True)
    available_doctors = models.IntegerField(null=True, blank=True)
    appointment_contact_no = models.CharField(max_length=15,null=True, blank=True)
    hospital_contact_no = models.CharField(max_length=15,null=True, blank=True)
    hospital_specialities = models.CharField(max_length=1000,null=True, blank=True)

    main_image = models.ImageField(upload_to='health_image', null=True)

    other_image1 = models.ImageField(upload_to='health_image', null=True, blank=True)
    other_image2 = models.ImageField(upload_to='health_image', null=True, blank=True)

    def __str__(self):
        return self.name


