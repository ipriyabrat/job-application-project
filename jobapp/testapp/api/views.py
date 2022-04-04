from testapp.models import HydJobs,BangaloreJobs,PuneJobs
from testapp.api.serializers import HydJobsSerializer,BangaloreSerializer,PuneSerializer
from rest_framework.viewsets import ModelViewSet


class HydJobCRUDCBVs(ModelViewSet):
    queryset=HydJobs.objects.all()
    serializer_class=HydJobsSerializer
    
class BangalorejobCRUDCBVs(ModelViewSet):
    queryset=BangaloreJobs.objects.all()
    serializer_class=BangaloreSerializer

class PuneJobCRUDCBVs(ModelViewSet):
    queryset=PuneJobs.objects.all()
    serializer_class=PuneSerializer
