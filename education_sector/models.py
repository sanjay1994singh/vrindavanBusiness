from django.db import models


# Create your models here.
class EducationSector(models.Model):
    name = models.CharField(max_length=1000, null=True)
    address = models.TextField(null=True)
    description = models.TextField(null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True, blank=True)
    website = models.TextField(null=True, blank=True)
    year_of_establish = models.CharField(max_length=30, null=True, blank=True)
    timing = models.CharField(max_length=30, null=True, blank=True)
    affilliated_by = models.CharField(max_length=100, null=True, blank=True)
    approved_by = models.CharField(max_length=100, null=True, blank=True)
    courses_list = models.TextField(null=True, blank=True)
    facilities = models.TextField(null=True, blank=True)
    medium_language = models.CharField(max_length=100, null=True, blank=True)
    school_class = models.CharField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=500, null=True, blank=True)
    owner_name = models.CharField(max_length=100, null=True, blank=True)
    owner_contact = models.CharField(max_length=100, null=True, blank=True)
    main_image = models.ImageField(upload_to='education_image', null=True)
    other_image1 = models.ImageField(upload_to='education_image', null=True, blank=True)
    other_image2 = models.ImageField(upload_to='education_image', null=True, blank=True)
    other_image3 = models.ImageField(upload_to='education_image', null=True, blank=True)

    def __str__(self):
        return self.name
