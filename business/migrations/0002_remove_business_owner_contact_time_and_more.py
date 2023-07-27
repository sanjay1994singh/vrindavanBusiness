# Generated by Django 4.0 on 2023-07-22 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='owner_contact_time',
        ),
        migrations.RemoveField(
            model_name='business',
            name='owner_email',
        ),
        migrations.RemoveField(
            model_name='business',
            name='owner_moble',
        ),
        migrations.AddField(
            model_name='business',
            name='hot_water',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='intercome',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='is_six',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='manager_contact_no',
            field=models.CharField(default='', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='power_backup_ac',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='power_backup_fan',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='room_img1',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='business_image'),
        ),
        migrations.AddField(
            model_name='business',
            name='room_img2',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='business_image'),
        ),
        migrations.AddField(
            model_name='business',
            name='room_img3',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='business_image'),
        ),
        migrations.AddField(
            model_name='business',
            name='room_img4',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='business_image'),
        ),
        migrations.AddField(
            model_name='business',
            name='room_service',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='room_tv',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='six_ac',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='six_ac_price',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='six_for',
            field=models.IntegerField(default=5, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='six_non_ac',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='six_non_ac_price',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='travel_guide',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='attr1',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='attr10',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='attr2',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='attr3',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='attr4',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='attr5',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='attr6',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='attr7',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='attr8',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='attr9',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='owner_name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
