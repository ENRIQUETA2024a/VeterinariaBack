from rest_framework import serializers
from apps.vet.models.diagnoses_model import Diagnoses
from apps.vet.models.treatments_model import Treatments


class TreatmentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Treatments
        fields = "__all__"
