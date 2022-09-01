from django.urls import path
from nhasi import views
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template


# url for detail video

urlpatterns = [
    path('', views.nhasi, name='nhasi'),
    path('danh_sach_benh_nhan', views.danhSach, name='danhSach'),
    path('lich_lam_viec', views.lichLamViec, name='lichLamViec'),
    path('ajax_chonBenhNhan', views.ajax_chonBenhNhan, name='ajax_chonBenhNhan'),
    path('luuThongTinBenhNhan', views.luuThongTinBenhNhan, name='luuThongTinBenhNhan'),
    path('ajax_inBenhNhan', views.ajax_inBenhNhan, name='ajax_inBenhNhan'),
    path('ajax_xoaBenhNhan', views.ajax_xoaBenhNhan, name='ajax_xoaBenhNhan'),
    path('ajax_lichNghi', views.ajax_lichNghi, name='ajax_lichNghi'),
    path('ajax_lay_lichNghi', views.ajax_lay_lichNghi, name='ajax_lay_lichNghi'),
    path('ajax_lichChiTiet', views.ajax_lichChiTiet, name='ajax_lichChiTiet'),
    
]


