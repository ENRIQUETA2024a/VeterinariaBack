from django.db import models

class Products(models.Model):
    id=models.AutoField("Id",primary_key=True,db_column="id")
    name = models.CharField("name",max_length=255  ,null=True)
    category_id = models.IntegerField("category_id", null=True)
    laboratory = models.CharField("laboratory",max_length=255, null=True)
    expirationDate = models.DateField("expirationDate", null=True)
    stock = models.IntegerField("stock", null=True)
    cost = models.DecimalField("cost",max_digits=10,decimal_places=2, null=True)
    price = models.DecimalField("price",max_digits=10,decimal_places=2, null=True)
    photo = models.CharField("photo",max_length=255, null=True)
    registrationDate = models.DateTimeField("registrationDate", null=True)
    idEmployeeModifies = models.IntegerField("idEmployeeModifies", null=True)
    deletedDate = models.DateTimeField("deletedDate", null=True)
    idEmployeeDeletes = models.IntegerField("idEmployeeDeletes", null=True)
    status = models.IntegerField("status", null=True)
    public_id = models.CharField("public_id",max_length=255, null=True)


    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"        
        ordering = ["id"]
        db_table = "tbl_products"  
        

    def __str__(self):
        return f"{self.name}"