from rest_framework import serializers
from apps.vet.models.product_treatments_model import Products_Treatments


class Product_TreatmentsSerializer(serializers.ModelSerializer):
    treatments = serializers.StringRelatedField()
    product = serializers.StringRelatedField()

    class Meta:
        model = Products_Treatments
        fields = "__all__"
