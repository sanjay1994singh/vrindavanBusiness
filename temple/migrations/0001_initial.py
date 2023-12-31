# Generated by Django 4.2.2 on 2023-06-18 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temple',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True, unique=True)),
                ('add', models.TextField(null=True)),
                ('created_at', models.DateTimeField()),
                ('devi_devta', models.CharField(max_length=200, null=True)),
                ('sevayat_name', models.CharField(max_length=500, null=True)),
                ('mandir_prabandhak', models.CharField(max_length=1000, null=True)),
                ('darshan_time', models.CharField(max_length=50, null=True)),
                ('arti1_time', models.CharField(max_length=50, null=True)),
                ('arti2_time', models.CharField(max_length=50, null=True)),
                ('arti3_time', models.CharField(max_length=50, null=True)),
                ('arti4_time', models.CharField(max_length=50, null=True)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
