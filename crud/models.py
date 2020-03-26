from django.db import models

# Create your models here.
class Suplier(models.Model):
    nama_suplier = models.CharField(max_length=50)
    no_telp = models.CharField(max_length=13)
    alamat = models.TextField()

    def __str__(self):
        return self.nama_suplier

class Barang(models.Model):
    nama_barang = models.CharField(max_length=50)
    harga = models.IntegerField()
    stok = models.IntegerField()
    suplier = models.ForeignKey(Suplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_barang

class Pembeli(models.Model):
    nama = models.CharField(max_length=50)
    jk = models.CharField(max_length=1, default='L')
    no_telp = models.CharField(max_length=13)
    alamat = models.TextField()

    def __str__(self):
        return self.nama

class Transaksi(models.Model):
    id_barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    id_pembeli = models.ForeignKey(Pembeli, on_delete=models.CASCADE)
    tanggal = models.DateTimeField(auto_now=True)
    keterangan = models.TextField()

class Pembayaran(models.Model):
    id_transaksi = models.ForeignKey(Transaksi ,on_delete=models.CASCADE)
    tanggal_bayar = models.DateTimeField(auto_now=True)
    total_bayar = models.IntegerField()