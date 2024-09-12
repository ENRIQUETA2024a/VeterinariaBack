from django.db import models
from apps.vet.models.patient_model import Patient

class Consults(models.Model):
    id = models.AutoField("IdConsults", primary_key=True, db_column="id")
    consult_date=models.DateField("consult_dat" ,null=False)
    reason = models.CharField("reason",max_length=255,null=False)
    antecedents = models.CharField("antecedents",max_length=255,null=True)
    diseases = models.CharField("diseases",max_length=255,null=True)
    next_consult = models.DateField("next_consult",max_length=255,null=True)
    patient = models.ForeignKey(Patient,models.DO_NOTHING,db_column='patient_id',null=False)
    status = models.IntegerField("status",null=True)


    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"
        db_table = "tbl_consults"

    def __str__(self):
        return f"{self.consult_date} {self.reason}"
