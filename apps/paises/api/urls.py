from rest_framework import routers
from apps.paises.api.api import ApiPais 


router = routers.DefaultRouter()

router.register('api/paises', ApiPais, 'apiPais')

urlpatterns = router.urls



