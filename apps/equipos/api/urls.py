from rest_framework import routers
from apps.equipos.api.api import ApiEqupos 


router = routers.DefaultRouter()

router.register('api/equipos', ApiEqupos, 'apiEqupos')

urlpatterns = router.urls