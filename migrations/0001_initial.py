# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autobusy',
            fields=[
                ('numer_boczny', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('marka', models.CharField(blank=True, max_length=20, null=True)),
                ('model', models.CharField(blank=True, max_length=20, null=True)),
                ('rok_produkcji', models.SmallIntegerField()),
                ('pojemnosc', models.SmallIntegerField()),
                ('niskopodlogowy', models.NullBooleanField()),
                ('rejestracja', models.CharField(max_length=9)),
                ('przegubowy', models.NullBooleanField()),
                ('pojemnosc_silnika', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'autobusy',
            },
        ),
        migrations.CreateModel(
            name='Kierowcy',
            fields=[
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('pesel', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('prawo_jazdy', models.CharField(max_length=10)),
            ],
            options={
                'managed': False,
                'db_table': 'kierowcy',
            },
        ),
        migrations.CreateModel(
            name='Linie',
            fields=[
                ('numer', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('dlugosc', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pora_dzialania', models.CharField(blank=True, max_length=16, null=True)),
                ('typ', models.CharField(max_length=1)),
            ],
            options={
                'managed': False,
                'db_table': 'linie',
            },
        ),
        migrations.CreateModel(
            name='Motorniczy',
            fields=[
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('pesel', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('prawo_jazdy', models.CharField(max_length=10)),
            ],
            options={
                'managed': False,
                'db_table': 'motorniczy',
            },
        ),
        migrations.CreateModel(
            name='Odjazdy',
            fields=[
                ('godzina', models.TimeField()),
                ('tolerancja', models.SmallIntegerField(blank=True, null=True)),
                ('nazwa_systemowa', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('typ_dnia', models.CharField(max_length=16)),
                ('kolejnosc_pojazdu', models.SmallIntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'odjazdy',
            },
        ),
        migrations.CreateModel(
            name='Przejazdy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kolejnosc_wyjazdu', models.SmallIntegerField()),
                ('data', models.DateField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'przejazdy',
            },
        ),
        migrations.CreateModel(
            name='Przewoznicy',
            fields=[
                ('nazwa', models.CharField(max_length=150)),
                ('nip', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('adres', models.CharField(max_length=200)),
            ],
            options={
                'managed': False,
                'db_table': 'przewoznicy',
            },
        ),
        migrations.CreateModel(
            name='Przystanki',
            fields=[
                ('nazwa_systemowa', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nazwa_przyjazna', models.CharField(max_length=32)),
                ('adres', models.CharField(max_length=100)),
                ('zadaszenie', models.NullBooleanField()),
            ],
            options={
                'managed': False,
                'db_table': 'przystanki',
            },
        ),
        migrations.CreateModel(
            name='PunktyTrasy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kolejnosc', models.SmallIntegerField()),
                ('kierunek', models.SmallIntegerField()),
                ('czas_przejazdu', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'punkty_trasy',
            },
        ),
        migrations.CreateModel(
            name='Tramwaje',
            fields=[
                ('numer_boczny', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('marka', models.CharField(blank=True, max_length=20, null=True)),
                ('model', models.CharField(blank=True, max_length=20, null=True)),
                ('rok_produkcji', models.SmallIntegerField()),
                ('pojemnosc', models.SmallIntegerField()),
                ('niskopodlogowy', models.NullBooleanField()),
                ('samodzielny', models.BooleanField()),
            ],
            options={
                'managed': False,
                'db_table': 'tramwaje',
            },
        ),
        migrations.CreateModel(
            name='Zajezdnie',
            fields=[
                ('pojemnosc', models.SmallIntegerField()),
                ('adres', models.CharField(max_length=200)),
                ('typ', models.CharField(max_length=32)),
                ('id', models.SmallIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
                'db_table': 'zajezdnie',
            },
        ),
    ]
