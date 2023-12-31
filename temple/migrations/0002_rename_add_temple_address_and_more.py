# Generated by Django 4.0 on 2023-07-23 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temple', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='temple',
            old_name='add',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='temple',
            old_name='mobile',
            new_name='contact_number',
        ),
        migrations.RenameField(
            model_name='temple',
            old_name='arti1_time',
            new_name='darshan_time_summer',
        ),
        migrations.RenameField(
            model_name='temple',
            old_name='arti2_time',
            new_name='darshan_time_winter',
        ),
        migrations.RenameField(
            model_name='temple',
            old_name='devi_devta',
            new_name='deity',
        ),
        migrations.RenameField(
            model_name='temple',
            old_name='mandir_prabandhak',
            new_name='mandir_manager',
        ),
        migrations.RenameField(
            model_name='temple',
            old_name='sevayat_name',
            new_name='sewayat_name',
        ),
        migrations.RemoveField(
            model_name='temple',
            name='arti3_time',
        ),
        migrations.RemoveField(
            model_name='temple',
            name='arti4_time',
        ),
        migrations.RemoveField(
            model_name='temple',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='temple',
            name='darshan_time',
        ),
        migrations.AddField(
            model_name='temple',
            name='arti1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='temple',
            name='arti2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='temple',
            name='arti3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='temple',
            name='arti4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='temple',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='temple',
            name='website',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='temple',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='temple',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
