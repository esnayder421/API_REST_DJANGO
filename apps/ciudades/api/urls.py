from rest_framework import routers
from apps.ciudades.api.api import apiCiudad


router = routers.DefaultRouter()

router.register('api/ciudades', apiCiudad, 'apiCiudad')

urlpatterns = router.urls
