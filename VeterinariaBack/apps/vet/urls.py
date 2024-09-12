from django.urls import path
from apps.vet.api_views.cliente_views import LoginView
from apps.vet.api_views.patient_views import PatientViewDetail
from apps.vet.api_views.receta_views import RecetaView
from apps.vet.api_views.exams_views import ExamsView
from apps.vet.api_views.consults_views import ConsultView,ConsultDateView
from apps.vet.api_views.diagnoses_views import DiagnosesView
from apps.vet.api_views.treatments_views import TreatmentsView
from apps.vet.api_views.product_treatments_views import Product_TreatmentsView

urlpatterns = [
    # Cliente
    path("login/", LoginView.as_view(), name="login"),
    # Paciente
    path("paciente/<int:pk>", PatientViewDetail.as_view(), name="paciente_view_detail"),
    # Receta
    path("receta/<int:pk>", RecetaView.as_view(), name="receta_view"),
    # Examenes
    path("examenes/<int:pk>", ExamsView.as_view(), name="examenes_view"),
    # Consultas
    path("consultas/<int:pk>", ConsultView.as_view(), name="consults_view"),
    path("consultas_list/<int:pk>", ConsultDateView.as_view(), name="consults_filter_fecha"),
    # Diagnosticos
    path("diagnosticos/<int:pk>", DiagnosesView.as_view(), name="diagnoses_view"),
    # Trtamiento
    path("tratamientos/<int:pk>", TreatmentsView.as_view(), name="tratamientos_view"),
    # Products Tratamientos
    path("products_tratamientos/<int:pk>", Product_TreatmentsView.as_view(), name="products_tratamientos_view")
]
