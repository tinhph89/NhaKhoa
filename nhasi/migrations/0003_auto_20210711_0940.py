# Generated by Django 3.0.6 on 2021-07-11 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nhasi', '0002_auto_20210710_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benhnhan',
            name='ma_so_nha_si',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nhasi.NhaSi'),
        ),
    ]
