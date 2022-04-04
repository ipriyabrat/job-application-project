from django.shortcuts import render
from testapp.models import HydJobs,BangaloreJobs,PuneJobs
# Create your views here.

def homepage_view(request):
    return render(request,'testapp/base.html')

def hydjobs_view(request):
    jobs_list = HydJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/hydjob.html',context=my_dict)

def banglore_view(request):
    jobs_list = BangaloreJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/bnaglrjob.html',context=my_dict)

def pune_view(request):
    jobs_list = PuneJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/punejob.html',context=my_dict)

