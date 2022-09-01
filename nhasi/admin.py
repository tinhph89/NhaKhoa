from django.contrib import admin
from .models import NhaSi, BenhNhan, CanhBao, TrieuChung, DiUng, ThoiGian, LichLamViec

class NhaSiAdmin(admin.ModelAdmin):
    list_display = ('ma_so_nha_si','ho_ten', 'so_dien_thoai')
    list_display_links = ('ma_so_nha_si','ho_ten')
    list_filter = ('ma_so_nha_si','ho_ten')
    search_fields = ('ma_so_nha_si','ho_ten')
    list_per_page = 25
    # resource_class = NhaSiResource

# class TienSuBenhAdmin(admin.ModelAdmin):
#     list_display = ('ma_so_benh_nhan',)
#     list_display_links = ('ma_so_benh_nhan',)
#     list_per_page = 25
#     list_filter = ('ma_so_benh_nhan',)

class BenhNhanAdmin(admin.ModelAdmin):
    list_display = ('ma_ho_so','ho_benh_nhan', 'chu_lot_benh_nhan','ten_bn','trang_thai_kham','is_available')
    list_display_links = ('ma_ho_so','trang_thai_kham')
    list_filter = ('ma_ho_so',)
    search_fields = ('ma_ho_so','ten_bn')
    list_per_page = 25
    

class CanhBaoAdmin(admin.ModelAdmin):
    list_display = ('ma_so_canh_bao','noi_dung')
    list_filter = ('ma_so_canh_bao')
    search_fields = ('ma_so_canh_bao','noi_dung')
    list_per_page = 25
    list_filter = ('ma_so_canh_bao',)
    list_display_links = ('ma_so_canh_bao','noi_dung')

class TrieuChungAdmin(admin.ModelAdmin):
    list_display = ('ma_so_trieu_chung','noi_dung')
    list_filter = ('ma_so_trieu_chung')
    search_fields = ('ma_so_trieu_chung','noi_dung')
    list_per_page = 25
    list_filter = ('ma_so_trieu_chung',)
    list_display_links = ('ma_so_trieu_chung','noi_dung')

class DiUngAdmin(admin.ModelAdmin):
    list_display = ('ma_so_di_ung','noi_dung')
    list_filter = ('ma_so_di_ung')
    search_fields = ('ma_so_di_ung','noi_dung')
    list_per_page = 25
    list_filter = ('ma_so_di_ung',)
    list_display_links = ('ma_so_di_ung','noi_dung')

class ThoiGianAdmin(admin.ModelAdmin):
    list_display = ('thoi_gian',)
    list_filter = ('thoi_gian',)
    search_fields = ('thoi_gian',)
    list_per_page = 25
    list_filter = ('thoi_gian',)
    list_display_links = ('thoi_gian',)

class LichLamViecAdmin(admin.ModelAdmin):
    list_display = ('ma_so_nha_si','ho_ten_nha_si')
    list_filter = ('ma_so_nha_si','ho_ten_nha_si')
    search_fields = ('ma_so_nha_si','ho_ten_nha_si')
    list_per_page = 25
    list_filter = ('ma_so_nha_si','ho_ten_nha_si')
    list_display_links = ('ma_so_nha_si','ho_ten_nha_si')

admin.site.register(BenhNhan, BenhNhanAdmin)
admin.site.register(NhaSi, NhaSiAdmin)
admin.site.register(LichLamViec, LichLamViecAdmin)
admin.site.register(CanhBao, CanhBaoAdmin)
admin.site.register(TrieuChung, TrieuChungAdmin)
admin.site.register(DiUng, DiUngAdmin)
admin.site.register(ThoiGian, ThoiGianAdmin)