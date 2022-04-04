 
from rest_framework.serializers import ModelSerializer
from testapp.models import HydJobs,BangaloreJobs,PuneJobs


class HydJobsSerializer(ModelSerializer):
    class Meta:
        model=HydJobs
        fields='__all__'


class BangaloreSerializer(ModelSerializer):
    class Meta:
        model=BangaloreJobs
        fields='__all__'

        
class PuneSerializer(ModelSerializer):
    class Meta:
        model=PuneJobs
        fields='__all__'
