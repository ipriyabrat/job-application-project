 
from django.urls import path,include

from testapp.api.views import HydJobCRUDCBVs,BangalorejobCRUDCBVs,PuneJobCRUDCBVs
from rest_framework import  routers
router=routers.DefaultRouter()
router.register('hydjobinfo',HydJobCRUDCBVs)
router.register('bangalorejobinfo',BangalorejobCRUDCBVs)
router.register('punejobinfo',PuneJobCRUDCBVs)


urlpatterns = [
  
    path('',include(router.urls)),
]