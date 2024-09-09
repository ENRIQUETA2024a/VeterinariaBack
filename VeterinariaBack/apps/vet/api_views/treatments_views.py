import traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.vet.models.treatments_model import Treatments
from apps.vet.serializers.treatments_serializers import TreatmentsSerializer

class TreatmentsView(APIView):

    def get(self,request,pk):
        try:
            treatments_data= Treatments.objects.filter(diagnosis=pk)
            if treatments_data:
                print(treatments_data)
                return Response(TreatmentsSerializer(treatments_data,many=True).data,status=status.HTTP_200_OK)
            return Response({'mensaje':"No existe ninguN tratamiento asociado a ese diagnostico"},status=status.HTTP_404_NOT_FOUND)
        except:
            tb = traceback.format_exc()
            print(tb)
            return Response({"SERVER ERROR"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)