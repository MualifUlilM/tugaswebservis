from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .serializers import BarangSerializer, PembayaranSerializer, PembeliSerializer, SuplierSerializer, TransaksiSerializer
from .models import Barang, Pembayaran, Pembeli, Suplier, Transaksi

# Create your views here.
# API viewset classes

class BarangViewset(viewsets.ModelViewSet):
    serializer_class = BarangSerializer
    queryset = Barang.objects.all()

class PembayaranViewset(viewsets.ModelViewSet):
    serializer_class = PembayaranSerializer
    queryset = Pembayaran.objects.all()

class PembeliViewset(viewsets.ModelViewSet):
    serializer_class = PembeliSerializer
    queryset = Pembeli.objects.all()

class SuplierViewset(viewsets.ModelViewSet):
    serializer_class = SuplierSerializer
    queryset = Suplier.objects.all()

class TransaksiViewset(viewsets.ModelViewSet):
    serializer_class = TransaksiSerializer
    queryset = Transaksi.objects.all()

# homepage views

def index(request):
    return HttpResponse('Halo Semua')