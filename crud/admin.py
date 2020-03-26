from django.contrib import admin
from .models import Barang, Pembayaran, Pembeli, Suplier, Transaksi
# Register your models here.

admin.site.register(Barang)
admin.site.register(Pembayaran)
admin.site.register(Pembeli)
admin.site.register(Suplier)
admin.site.register(Transaksi)
