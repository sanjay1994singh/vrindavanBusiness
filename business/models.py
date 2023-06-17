from django.db import models

# Create your models here.
class FoodType(models.Model):
    type = models.CharField(max_length=200,null=True,unique=True)

    def __str__(self):
        return self.type
        

class FoodCategory(models.Model):
    food_type = models.ForeignKey(FoodType,on_delete=models.PROTECT)
    category = models.CharField(max_length=200,null=True,unique=True)

    def __str__(self):
        return self.category

class FoodList(models.Model):
    food_category = models.ForeignKey(FoodCategory,on_delete=models.PROTECT)
    food_item_list = models.CharField(max_length=200,null=True,unique=True)

    def __str__(self):
        return self.food_item_list

class BusinessType(models.Model):
    name = models.CharField(max_length=200,null=True,unique=True)
    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.name
    
class business(models.Model):
    business_type = models.ForeignKey(BusinessType,on_delete=models.PROTECT)
    name = models.CharField(max_length=1000,null=True)
    address = models.TextField(null=True)
    landmark = models.CharField(max_length=1000,null=True)
    city = models.CharField(max_length=1000,null=True,default='')
    state = models.CharField(max_length=1000,null=True,default='')
    country = models.CharField(max_length=1000,null=True,default='')
    mobile = models.CharField(max_length=20,null=True)
    phone = models.CharField(max_length=20,null=True)
    email = models.EmailField(null=True)
    website = models.URLField(null=True)
    main_img = models.ImageField(upload_to='business_image',null=True,default=None)

    is_single = models.BooleanField(null=True,default=True)
    single_ac = models.IntegerField(null=True, default=0)
    single_non_ac = models.IntegerField(null=True, default=0)

    single_for = models.IntegerField(null=True,default=1)
    
    single_ac_price = models.FloatField(null=True, default=0.0)
    single_non_ac_price = models.FloatField(null=True, default=0.0)

    is_double = models.BooleanField(null=True,default=True)
    double_ac = models.IntegerField(null=True, default=0)
    double_non_ac = models.IntegerField(null=True, default=0)

    double_for = models.IntegerField(null=True,default=2)

    double_ac_price = models.FloatField(null=True, default=0.0)
    double_non_ac_price = models.FloatField(null=True, default=0.0)

    is_triple = models.BooleanField(null=True,default=True)
    triple_ac = models.IntegerField(null=True, default=0)
    triple_non_ac = models.IntegerField(null=True, default=0)

    triple_for = models.IntegerField(null=True,default=3)

    triple_ac_price = models.FloatField(null=True, default=0.0)
    triple_non_ac_price = models.FloatField(null=True, default=0.0)

    is_four = models.BooleanField(null=True,default=False)
    four_ac = models.IntegerField(null=True, default=0)
    four_non_ac = models.IntegerField(null=True, default=0)

    four_for = models.IntegerField(null=True,default=4)

    four_ac_price = models.FloatField(null=True, default=0.0)
    four_non_ac_price = models.FloatField(null=True, default=0.0)

    is_five = models.BooleanField(null=True,default=False)
    five_ac = models.IntegerField(null=True, default=0)
    five_non_ac = models.IntegerField(null=True, default=0)

    five_for = models.IntegerField(null=True,default=5)

    five_ac_price = models.FloatField(null=True, default=0.0)
    five_non_ac_price = models.FloatField(null=True, default=0.0)

    is_hall = models.BooleanField(null=True,default=False)
    hall_ac = models.IntegerField(null=True, default=0)
    hall_non_ac = models.IntegerField(null=True, default=0)

    hall_for = models.IntegerField(null=True,default=1)

    hall_ac_price = models.FloatField(null=True, default=0.0)
    hall_non_ac_price = models.FloatField(null=True, default=0.0)

    arrangement_for_katha = models.BooleanField(null=True,default=False)
    katha_people = models.IntegerField(null=True,default=0)

    arrangement_for_wedding = models.BooleanField(null=True,default=False)
    wedding_people = models.IntegerField(null=True,default=0)

    arrangement_for_birthday = models.BooleanField(null=True,default=False)
    birthday_people = models.IntegerField(null=True,default=0)

    arrangement_for_other = models.BooleanField(null=True,default=False)
    other_people = models.IntegerField(null=True,default=0)

    booking = models.BooleanField(null=True,default=False)
    booking_accept = models.CharField(max_length=500,null=True, default='')

    kitchen = models.BooleanField(null=True,default=False)
    kitchen_for = models.IntegerField(null=True,default=0)

    parking = models.BooleanField(null=True,default=False)
    parking_address = models.CharField(max_length=100, null=True,default='Hotel')
    
    restaurant = models.BooleanField(null=True,default=False)
    restaurant_for = models.IntegerField(null=True,default=0)

    taxi_service = models.BooleanField(null=True,default=False)

    checkout = models.CharField(max_length=50,null=True, default='12:00pm for 24 hrs')

    owner_name = models.CharField(max_length=100,null=True,default='')
    owner_email = models.EmailField(null=True,default='')
    owner_moble = models.CharField(max_length=20,null=True,default='')
    owner_contact_time = models.CharField(max_length=100,null=True,default='10:00 AM to 06:00 PM')

    attr1 = models.CharField(max_length=100,null=True,default='')
    attr2 = models.CharField(max_length=100,null=True,default='')
    attr3 = models.CharField(max_length=100,null=True,default='')
    attr4 = models.CharField(max_length=100,null=True,default='')
    attr5 = models.CharField(max_length=100,null=True,default='')


    attr6 = models.IntegerField(null=True,default=0)
    attr7 = models.IntegerField(null=True,default=0)
    attr8 = models.IntegerField(null=True,default=0)
    attr9 = models.IntegerField(null=True,default=0)
    attr10 = models.IntegerField(null=True,default=0)

    def __str__(self):
        return self.name

class Facility(models.Model):
    desc = models.TextField(null=True,default='')
    business = models.ForeignKey(business,on_delete=models.PROTECT)

    def __str__(self):
        return self.desc









