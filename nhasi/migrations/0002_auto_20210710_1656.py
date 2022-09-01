# Generated by Django 3.0.6 on 2021-07-10 16:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nhasi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BenhNhan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_ho_so', models.CharField(max_length=100)),
                ('ho_benh_nhan', models.CharField(max_length=50)),
                ('chu_lot_benh_nhan', models.CharField(max_length=50)),
                ('ten_bn', models.CharField(max_length=50)),
                ('ngay_sinh_benh_nhan', models.DateField()),
                ('gioi_tinh_benh_nhan', models.IntegerField()),
                ('ma_so_nha_si', models.CharField(max_length=500)),
                ('trang_thai_kham', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CanhBao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_so_canh_bao', models.CharField(max_length=100)),
                ('noi_dung', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DiUng',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_so_di_ung', models.CharField(max_length=100)),
                ('noi_dung', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TienSuBenh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_so_benh_nhan', models.CharField(max_length=100)),
                ('ma_so_cdt', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TrieuChung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_so_trieu_chung', models.CharField(max_length=100)),
                ('noi_dung', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='nhasi',
            old_name='ma_so',
            new_name='ma_so_nha_si',
        ),
        migrations.AddField(
            model_name='nhasi',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nhasi',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='LichLamViec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lam_viec_tu_ngay', models.DateField()),
                ('lam_viec_den_ngay', models.DateField()),
                ('lam_viec_tu_gio', models.CharField(max_length=100)),
                ('lam_viec_den_gio', models.CharField(max_length=100)),
                ('nha_si', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nhasi.NhaSi')),
            ],
        ),
    ]
