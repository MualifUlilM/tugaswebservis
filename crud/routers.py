from rest_framework.routers import DefaultRouter
from .views import BarangViewset, PembayaranViewset, PembeliViewset, SuplierViewset, TransaksiViewset


router = DefaultRouter()
router.register(r'barang', BarangViewset)
router.register(r'pembayaran', PembayaranViewset)
router.register(r'pembeli', PembeliViewset)
router.register(r'suplier', SuplierViewset)
router.register(r'transaksi', TransaksiViewset)