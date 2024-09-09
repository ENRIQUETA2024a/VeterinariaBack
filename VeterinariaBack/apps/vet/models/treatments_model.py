from django.db import models
from apps.vet.models.diagnoses_model import Diagnoses


class Treatments(models.Model):
    id = models.AutoField("Id", primary_key=True, db_column="id")
    detail = models.CharField("detail", max_length=50, null=True)
    diagnosis = models.ForeignKey(Diagnoses, models.DO_NOTHING,db_column='diagnosis_id',blank=False,null=False)
    status = models.IntegerField("status", null=True)

    class Meta:
        verbose_name = "Tratamiento"
        verbose_name_plural = "Tratamientos"
        db_table = "tbl_treatments"

    def __str__(self):
        return f"{self.detail}"
