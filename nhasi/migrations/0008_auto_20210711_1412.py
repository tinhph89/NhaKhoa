# Generated by Django 3.0.6 on 2021-07-11 14:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nhasi', '0007_benhnhan_ngay_kham'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TienSuBenh',
        ),
        migrations.AddField(
            model_name='benhnhan',
            name='cb_tc_du',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
