from django.db import models
from apps.vet.models.treatments_model import Treatments
from apps.vet.models.products_model import Products

class Products_Treatments(models.Model):
    id=models.AutoField("Id",primary_key=True,db_column="id")
    treatments = models.ForeignKey(Treatments,models.DO_NOTHING,db_column='treatment_id',null=True)
    product = models.ForeignKey(Products,models.DO_NOTHING,db_column='product_id',null=True)
    status=models.IntegerField('Descripcion',null=True)

    class Meta:
        verbose_name = "Producto_Tratamiento"
        verbose_name_plural = "Producto_Tratamientos"        
        ordering = ["id"]
        db_table = "tbl_products_treatments"  
        

    def __str__(self):
        return f"{self.treatments}"
