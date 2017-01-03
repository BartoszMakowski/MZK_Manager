# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Autobusy(models.Model):
    numer_boczny = models.SmallIntegerField(primary_key=True)
    marka = models.CharField(max_length=20, blank=True, null=True)
    model = models.CharField(max_length=20, blank=True, null=True)
    rok_produkcji = models.SmallIntegerField()
    pojemnosc = models.SmallIntegerField()
    zajezdnie = models.ForeignKey('Zajezdnie', models.DO_NOTHING)
    niskopodlogowy = models.NullBooleanField()
    rejestracja = models.CharField(max_length=9)
    przegubowy = models.NullBooleanField()
    pojemnosc_silnika = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)


    def __str__(self):
        return self.numer_boczny + ' ' + self.marka


    class Meta:
        managed = False
        db_table = 'autobusy'


class Kierowcy(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    pesel = models.CharField(primary_key=True, max_length=11)
    prawo_jazdy = models.CharField(max_length=10)
    przewoznicy_nip = models.ForeignKey('Przewoznicy', models.DO_NOTHING, db_column='przewoznicy_nip')
    autobusy_numer_boczny = models.ForeignKey(Autobusy, models.DO_NOTHING, db_column='autobusy_numer_boczny')


    def __str__(self):
        return self.imie + ' ' + self.nazwisko


    class Meta:
        managed = False
        db_table = 'kierowcy'


class Linie(models.Model):
    numer = models.CharField(primary_key=True, max_length=4)
    dlugosc = models.DecimalField(max_digits=5, decimal_places=2)
    przewoznicy_nip = models.ForeignKey('Przewoznicy', models.DO_NOTHING, db_column='przewoznicy_nip')
    pora_dzialania = models.CharField(max_length=16, blank=True, null=True)
    typ = models.CharField(max_length=1)


    def __str__(self):
        return self.numer


    class Meta:
        managed = False
        db_table = 'linie'


class Motorniczy(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    pesel = models.CharField(primary_key=True, max_length=11)
    prawo_jazdy = models.CharField(max_length=10)
    przewoznicy_nip = models.ForeignKey('Przewoznicy', models.DO_NOTHING, db_column='przewoznicy_nip')
    tramwaje_numer_boczny = models.ForeignKey('Tramwaje', models.DO_NOTHING, db_column='tramwaje_numer_boczny')


    def __str__(self):
        return self.imie + ' ' + self.nazwisko


    class Meta:
        managed = False
        db_table = 'motorniczy'


class Odjazdy(models.Model):
    godzina = models.TimeField()
    tolerancja = models.SmallIntegerField(blank=True, null=True)
    nazwa_systemowa = models.CharField(primary_key=True, max_length=8)
    typ_dnia = models.CharField(max_length=16)
    kolejnosc_pojazdu = models.SmallIntegerField()


    def __str__(self):
        return self.nazwa_systemowa + ' ' + self.godzina


    class Meta:
        managed = False
        db_table = 'odjazdy'


class Przejazdy(models.Model):
    kolejnosc_wyjazdu = models.SmallIntegerField()
    numer_boczny = models.ForeignKey('Tramwaje', models.DO_NOTHING, db_column='numer_boczny', blank=True, null=True)
    pesel = models.ForeignKey(Motorniczy, models.DO_NOTHING, db_column='pesel', blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    linie_numer = models.ForeignKey(Linie, models.DO_NOTHING, db_column='linie_numer')


    def __str__(self):
        return self.linie_numer + ' ' + self.kolejnosc


    class Meta:
        managed = False
        db_table = 'przejazdy'
        unique_together = (('kolejnosc_wyjazdu', 'linie_numer'),)


class Przewoznicy(models.Model):
    nazwa = models.CharField(max_length=150)
    nip = models.CharField(primary_key=True, max_length=10)
    adres = models.CharField(max_length=200)


    def __str__(self):
        return self.nazwa


    class Meta:
        managed = False
        db_table = 'przewoznicy'


class Przystanki(models.Model):
    nazwa_systemowa = models.CharField(primary_key=True, max_length=8)
    nazwa_przyjazna = models.CharField(max_length=32)
    adres = models.CharField(max_length=100)
    zadaszenie = models.NullBooleanField()
 

    def __str__(self):
        return self.nazwa_przyjazna


    class Meta:
        managed = False
        db_table = 'przystanki'


class PunktyTrasy(models.Model):
    kolejnosc = models.SmallIntegerField()
    linie_numer = models.ForeignKey(Linie, models.DO_NOTHING, db_column='linie_numer')
    kierunek = models.SmallIntegerField()
    przystanki_nazwa_systemowa = models.ForeignKey(Przystanki, models.DO_NOTHING, db_column='przystanki_nazwa_systemowa')
    czas_przejazdu = models.SmallIntegerField(blank=True, null=True)


    def __str__(self):
        return self.linie_numer + '- ' + self.kierunek + '- ' + self.kolejnosc


    class Meta:
        managed = False
        db_table = 'punkty_trasy'
        unique_together = (('linie_numer', 'kolejnosc', 'kierunek', 'przystanki_nazwa_systemowa'),)


class Tramwaje(models.Model):
    numer_boczny = models.SmallIntegerField(primary_key=True)
    marka = models.CharField(max_length=20, blank=True, null=True)
    model = models.CharField(max_length=20, blank=True, null=True)
    rok_produkcji = models.SmallIntegerField()
    pojemnosc = models.SmallIntegerField()
    zajezdnie = models.ForeignKey('Zajezdnie', models.DO_NOTHING)
    niskopodlogowy = models.NullBooleanField()
    samodzielny = models.BooleanField()


    def __str__(self):
        return self.numer_boczny + ' ' + self.model


    class Meta:
        managed = False
        db_table = 'tramwaje'


class Zajezdnie(models.Model):
    pojemnosc = models.SmallIntegerField()
    adres = models.CharField(max_length=200)
    typ = models.CharField(max_length=32)
    id = models.SmallIntegerField(primary_key=True)
    przewoznicy_nip = models.ForeignKey(Przewoznicy, models.DO_NOTHING, db_column='przewoznicy_nip')

    def __str__(self):
        return self.adres

    class Meta:
        managed = False
        db_table = 'zajezdnie'
