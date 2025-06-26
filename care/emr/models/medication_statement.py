from django.db import models

from care.emr.models.base import EMRBaseModel


class MedicationStatement(EMRBaseModel):
    status = models.CharField(max_length=100)
    reason = models.CharField(max_length=100, null=True, blank=True)
    medication = models.JSONField(default=dict)
    patient = models.ForeignKey("emr.Patient", on_delete=models.CASCADE)
    encounter = models.ForeignKey("emr.Encounter", on_delete=models.CASCADE)
    effective_period = models.JSONField(default=dict)
    information_source = models.CharField(max_length=100)
    dosage_text = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
