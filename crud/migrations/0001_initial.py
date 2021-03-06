# Generated by Django 3.0.4 on 2020-03-26 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_barang', models.CharField(max_length=50)),
                ('harga', models.IntegerField()),
                ('stok', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pembeli',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('jk', models.CharField(default='L', max_length=1)),
                ('no_telp', models.CharField(max_length=13)),
                ('alamat', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Suplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_suplier', models.CharField(max_length=50)),
                ('no_telp', models.CharField(max_length=13)),
                ('alamat', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateTimeField(auto_now=True)),
                ('keterangan', models.TextField()),
                ('id_barang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.Barang')),
                ('id_pembeli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.Pembeli')),
            ],
        ),
        migrations.CreateModel(
            name='Pembayaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_bayar', models.DateTimeField(auto_now=True)),
                ('total_bayar', models.IntegerField()),
                ('id_transaksi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.Transaksi')),
            ],
        ),
        migrations.AddField(
            model_name='barang',
            name='suplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.Suplier'),
        ),
    ]
