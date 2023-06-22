from rest_framework.routers import DefaultRouter

from apps.Veterinaria.api.viewset.cliente_api import  UserViewSet
from apps.Veterinaria.api.viewset.mascotas_api import MascotaViewSet
from apps.Veterinaria.api.viewset.historia_clinica_api import HistoriaClinicaViewSet


router = DefaultRouter()

router.register(r'cliente', UserViewSet, basename="Cliente")
router.register(r'mascota', MascotaViewSet, basename="Mascota")
router.register(r'historia_clinica', HistoriaClinicaViewSet, basename="HistoriaClinica")


urlpatterns = router.urls