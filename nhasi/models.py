from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class NhaSi(models.Model):
    user_nha_si = models.ForeignKey(User,on_delete = models.DO_NOTHING)
    ma_so_nha_si = models.CharField(max_length = 500)
    ho_ten = models.CharField(max_length = 500)
    so_dien_thoai = models.CharField(max_length = 200)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    is_available    = models.BooleanField(default=True)

    def __str__(self):
        return self.ho_ten

class LichLamViec(models.Model):
    ma_so_nha_si = models.CharField(max_length = 100)
    ho_ten_nha_si = models.CharField(max_length = 100)
    thoi_gian_nghi = models.CharField(max_length = 100)
    def __str__(self):
        return self.ho_ten_nha_si


class BenhNhan(models.Model):
    ma_ho_so = models.CharField(max_length = 100, unique=True)
    ho_benh_nhan =  models.CharField(max_length = 50)
    chu_lot_benh_nhan =  models.CharField(max_length = 50)
    ten_bn = models.CharField(max_length = 50)
    cb_tc_du = models.CharField(max_length = 100)
    ngay_sinh_benh_nhan = models.DateField()
    gioi_tinh_benh_nhan = models.IntegerField()
    ma_so_nha_si =  models.CharField(max_length = 50)
    ho_ten_nha_si = models.CharField(max_length = 50)
    so_dien_thoai = models.CharField(max_length = 50)
    dia_chi = models.CharField(max_length = 50)
    kham_tu_ngay = models.DateField()
    ghi_chu = models.CharField(max_length = 50)
    thoi_gian_kham = models.CharField(max_length = 100)
    trang_thai_kham =  models.CharField(max_length = 500)
    noi_dung_kham  = models.CharField(max_length = 500)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    is_available    = models.BooleanField(default=True)
    canh_bao_suc_khoe = models.CharField(max_length = 500)
    di_ung = models.CharField(max_length = 500)
    trieu_chung = models.CharField(max_length = 500)

    def full_name(self):
        return f'{self.ho_bn} {self.chu_lot_bn} {self.ten_bn}'

    class Meta:
        verbose_name = 'benhnhan'
        verbose_name_plural = 'benhnhan'

class CanhBao(models.Model):
    ma_so_canh_bao= models.CharField(max_length = 100)
    noi_dung = models.CharField(max_length = 100)
    is_available    = models.BooleanField(default=True)
    def __str__(self):
        return self.ma_so_canh_bao


class TrieuChung(models.Model):
    ma_so_trieu_chung = models.CharField(max_length = 100)
    noi_dung = models.CharField(max_length = 100)
    is_available    = models.BooleanField(default=True)
    def __str__(self):
        return self.ma_so_trieu_chung

class DiUng(models.Model):
    ma_so_di_ung = models.CharField(max_length = 100)
    noi_dung = models.CharField(max_length = 100)
    is_available    = models.BooleanField(default=True)
    def __str__(self):
        return self.ma_so_di_ung


class ThoiGian(models.Model):
    thoi_gian= models.CharField(max_length = 100)
    is_available    = models.BooleanField(default=True)
    def __str__(self):
        return self.thoi_gian


