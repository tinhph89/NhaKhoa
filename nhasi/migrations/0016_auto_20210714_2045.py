# Generated by Django 3.0.6 on 2021-07-14 20:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nhasi', '0015_benhnhan_noi_dung_kham'),
    ]

    operations = [
        migrations.AddField(
            model_name='benhnhan',
            name='canh_bao_suc_khoe',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='benhnhan',
            name='di_ung',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='benhnhan',
            name='trieu_chung',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
