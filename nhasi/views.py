from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from datetime import datetime, timedelta, date
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.http import JsonResponse
from django.core import serializers
from .models import BenhNhan, NhaSi, CanhBao, TrieuChung, DiUng, ThoiGian, LichLamViec
from nhasi.choices import thoi_gian_choices
import csv
import json
import random
import datetime
import traceback
from random import randrange
from datetime import date
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

@login_required(login_url = "login")
def nhasi(request):
    mas_so_default = random.randint(1000000000, 9999999999)
    today = date.today()
    y = today.strftime("%Y")
    m = today.strftime("%m")
    d = today.strftime("%d")
    dmy = y[-2:]+m+d
    id = BenhNhan.objects.latest('id')
    id_new = dmy + str(int(id.id) + 1)
    mas_so_default = id_new
    benh_nhan = BenhNhan.objects.filter(is_available = True, trang_thai_kham = 0)
    id = BenhNhan.objects.latest('id')
    nha_si = NhaSi.objects.filter(is_available = True)
    canh_bao = CanhBao.objects.filter(is_available = True)
    di_ung = DiUng.objects.filter(is_available = True)
    trieu_chung = TrieuChung.objects.filter(is_available = True)
    thoi_gian = ThoiGian.objects.filter(is_available = True)
    context = {
        'benh_nhan' : benh_nhan,
        'nha_si':nha_si,
        'canh_bao': canh_bao,
        'trieu_chung':trieu_chung,
        'di_ung':di_ung,
        'thoi_gian_choices':thoi_gian,
        'mas_so_default': mas_so_default
    }
    return render(request, 'nhasi/nhasiview.html',context)

@login_required(login_url = "login")
def danhSach(request):
    benh_nhan = BenhNhan.objects.filter(is_available=True, trang_thai_kham = 0)
    context = {
        'benh_nhan' : benh_nhan,
    }
    return render(request, 'nhasi/danhsachview.html', context)

@login_required(login_url = "login")
def lichLamViec(request):
    nha_si = NhaSi.objects.filter(is_available = True)
    context = {
        'nha_si':nha_si,
    }
    return render(request, 'nhasi/lichlamviec.html', context)

@login_required(login_url = "login")
def ajax_chonBenhNhan(request):
    if request.method == 'GET':
        id_benhNhan = request.GET['id_benhNhan']
        detail = BenhNhan.objects.filter(ma_ho_so = id_benhNhan, trang_thai_kham = 0)
        posts_serialized = serializers.serialize('json', detail)
        return JsonResponse(posts_serialized, safe=False)
    else:
        return JsonResponse("Eror")

@login_required(login_url = "login")
def ajax_inBenhNhan(request):
    if request.method == 'GET':
        ma_so = request.GET['ma_so']
        detail = BenhNhan.objects.filter(ma_ho_so = ma_so)
        posts_serialized = serializers.serialize('json', detail)
        return JsonResponse(posts_serialized, safe=False)
    else:
        return JsonResponse("Eror")

@login_required(login_url = "login")
def ajax_xoaBenhNhan(request):
    if request.method == 'GET':
        ma_so = request.GET['ma_so']
        data = BenhNhan.objects.get(ma_ho_so=ma_so)
        isDel = 0
        try:
            data.delete()
            isDel = 1
        except Exception as e:
            isDel = 0
        data_check = {
                'isDel': isDel,
                'message': "xoa thanh cong"
        }
        return JsonResponse(data_check)

@login_required(login_url = "login")
def luuThongTinBenhNhan(request):
    if request.method == 'GET':
        print("luu thong tin benh nhan")
        ma_ho_so = request.GET['ma_ho_so']
        ho_benh_nhan = request.GET['ho']
        chu_lot_benh_nhan = request.GET['ten_dem']
        ten_bn = request.GET['ten']
        ngay_sinh = request.GET['ngay_sinh']
        ngay_sinh_ins = datetime.datetime.strptime(ngay_sinh, "%d/%m/%Y").strftime("%Y-%m-%d")
        gioi_tinh = request.GET['gioi_tinh']
        so_dien_thoai = request.GET['so_dien_thoai']
        dia_chi = request.GET['dia_chi']
        ma_so_bac_si = request.GET['ma_so_bac_si']
        ten_bac_si = request.GET['ten_bac_si']
        thoi_gian_tu = request.GET['thoi_gian_tu']
        tu_ngay_ins = datetime.datetime.strptime(thoi_gian_tu, "%d/%m/%Y").strftime("%Y-%m-%d")
        thoi_gian_kham = request.GET['thoi_gian_kham']
        
        ghi_chu = request.GET['ghi_chu']
        tien_su_benh = request.GET['tien_su_benh']
        noi_dung_kham = request.GET['noi_dung_kham']
        canh_bao =  request.GET['nd_canh_bao']
        di_ung = request.GET['nd_di_ung']
        trieu_chung = request.GET['nd_trieu_chung']
        id_benh_nhan = request.GET['id_benh_nhan']
        ngay = date.today()
        is_dup = BenhNhan.objects.filter(ma_ho_so = ma_ho_so).exists()
        id_save = 0

        message = ""
        id_benh_nhan_server = 0
       
        if (is_dup == 0):
            data = BenhNhan(ma_ho_so=ma_ho_so,
                            ho_benh_nhan=ho_benh_nhan,
                            chu_lot_benh_nhan=chu_lot_benh_nhan,
                            ten_bn=ten_bn,
                            cb_tc_du  = tien_su_benh,
                            ngay_sinh_benh_nhan=ngay_sinh_ins,
                            gioi_tinh_benh_nhan =gioi_tinh,
                            ma_so_nha_si =ma_so_bac_si,
                            ho_ten_nha_si =ten_bac_si,
                            so_dien_thoai =so_dien_thoai,
                            dia_chi =dia_chi,
                            kham_tu_ngay =tu_ngay_ins,
                            thoi_gian_kham =thoi_gian_kham,
                            noi_dung_kham = noi_dung_kham,
                            ghi_chu = ghi_chu,
                            trang_thai_kham = 0,
                            canh_bao_suc_khoe = canh_bao,
                            di_ung = di_ung,
                            trieu_chung = trieu_chung
                            )

            data.save()
            id_save = 1
            id_benh_nhan_server = data.id
        else:
            BenhNhan.objects.filter(ma_ho_so = ma_ho_so).update(
                            ho_benh_nhan=ho_benh_nhan,
                            chu_lot_benh_nhan=chu_lot_benh_nhan,
                            ten_bn=ten_bn,
                            cb_tc_du  = tien_su_benh,
                            ngay_sinh_benh_nhan=ngay_sinh_ins,
                            gioi_tinh_benh_nhan =gioi_tinh,
                            ma_so_nha_si =ma_so_bac_si,
                            ho_ten_nha_si =ten_bac_si,
                            so_dien_thoai =so_dien_thoai,
                            dia_chi = dia_chi,
                            kham_tu_ngay =tu_ngay_ins,
                            thoi_gian_kham =thoi_gian_kham,
                            noi_dung_kham = noi_dung_kham,
                            ghi_chu = ghi_chu,
                            trang_thai_kham = 0,
                            canh_bao_suc_khoe = canh_bao,
                            di_ung = di_ung,
                            trieu_chung = trieu_chung
            )
            id_save = 2
            id_benh_nhan_server=id_benh_nhan
       
        
        data_check = {
                'id_save': id_save,
                'id_benh_nhan_server': id_benh_nhan_server
        }
        return JsonResponse(data_check)




@login_required(login_url = "login")

def ajax_lichNghi(request):
    if request.method == 'GET':
        thoi_gian_nghi = request.GET['lich_nghi']
        ho_ten_nha_si = request.GET['ho_ten_nha_si']
        ma_so_nha_si = request.GET['ma_so_bac_si']
        is_dup = LichLamViec.objects.filter(ma_so_nha_si = ma_so_nha_si, ho_ten_nha_si = ho_ten_nha_si).exists()
        if(is_dup == 0):
            dataSaved = LichLamViec(
                ma_so_nha_si= ma_so_nha_si,
                ho_ten_nha_si = ho_ten_nha_si,
                thoi_gian_nghi = thoi_gian_nghi
            )
            dataSaved.save()
            id_alert = dataSaved.id
        else:
            LichLamViec.objects.filter(ma_so_nha_si = ma_so_nha_si, ho_ten_nha_si = ho_ten_nha_si).update(
                ma_so_nha_si= ma_so_nha_si,
                ho_ten_nha_si = ho_ten_nha_si,
                thoi_gian_nghi = thoi_gian_nghi
            )
            id_alert = 0

        data_check = {
                'id_alert': id_alert,
                'thoi_gian_nghi': thoi_gian_nghi
        }
        return JsonResponse(data_check)

@login_required(login_url = "login")
def ajax_lay_lichNghi(request):
    if request.method == 'GET':
        ho_ten_nha_si = request.GET['ho_ten_nha_si']
        ma_so_nha_si = request.GET['ma_so_bac_si']
        detail = LichLamViec.objects.filter(ma_so_nha_si = ma_so_nha_si, ho_ten_nha_si = ho_ten_nha_si)
        posts_serialized = serializers.serialize('json', detail)
        return JsonResponse(posts_serialized, safe=False)
    else:
        return JsonResponse("Eror")

@login_required(login_url = "login")
def ajax_lichChiTiet(request):
    if request.method == 'GET':
        ma_so_bac_si = request.GET['ma_so_bac_si']
        dmy = request.GET['dmy']
        ngay_kham = datetime.datetime.strptime(dmy, "%d/%m/%Y").strftime("%Y-%m-%d")
        detail = BenhNhan.objects.filter(ma_so_nha_si = ma_so_bac_si, kham_tu_ngay = ngay_kham)
        posts_serialized = serializers.serialize('json', detail)
        return JsonResponse(posts_serialized, safe=False)
    else:
        return JsonResponse("Eror")