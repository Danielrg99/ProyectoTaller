# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Productos(models.Model):
    codproducto = models.IntegerField(db_column='CodProducto', primary_key=True)  # Field name made lowercase.
    preciounitario = models.DecimalField(db_column='PrecioUnitario', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    marca = models.CharField(db_column='Marca', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    fechaelab = models.DateField(db_column='FechaElab', blank=True, null=True)  # Field name made lowercase.
    fechavenc = models.DateField(db_column='FechaVenc', blank=True, null=True)  # Field name made lowercase.
    tipoproducto = models.CharField(db_column='TipoProducto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    peso = models.DecimalField(db_column='Peso', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Productos'

    def __str__(self):
        return f"{self.descripcion}"