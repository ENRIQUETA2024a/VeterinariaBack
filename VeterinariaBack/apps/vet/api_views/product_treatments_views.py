import traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.vet.models.product_treatments_model import Products_Treatments
from apps.vet.serializers.product_treatments_serializers import Product_TreatmentsSerializer

class Product_TreatmentsView(APIView):

    def get(self,request,pk):
        try:
            product_treatments_data= Products_Treatments.objects.filter(treatments=pk)
            if product_treatments_data:
                print(product_treatments_data)
                return Response(Product_TreatmentsSerializer(product_treatments_data,many=True).data,status=status.HTTP_200_OK)
            return Response({'mensaje':"No existe registros"},status=status.HTTP_404_NOT_FOUND)
        except:
            tb = traceback.format_exc()
            print(tb)
            return Response({"SERVER ERROR"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)