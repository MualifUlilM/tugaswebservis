from rest_framework import serializers
from .models import Barang, Pembayaran, Pembeli, Suplier, Transaksi

#serializer classes

class BarangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barang
        fields = '__all__'

class PembayaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pembayaran
        fields = '__all__'

class PembeliSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pembeli
        fields = '__all__'

class SuplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suplier
        fields = '__all__'

class TransaksiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaksi
        fields = '__all__'