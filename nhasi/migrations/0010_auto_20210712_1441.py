# Generated by Django 3.0.6 on 2021-07-12 14:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nhasi', '0009_benhnhan_ho_ten_nha_si'),
    ]

    operations = [
        migrations.AddField(
            model_name='benhnhan',
            name='dia_chi',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='benhnhan',
            name='kham_den_ngay',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='benhnhan',
            name='kham_tu_ngay',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='benhnhan',
            name='so_dien_thoai',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
