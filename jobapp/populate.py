import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobapp.settings')
import django
django.setup()

from testapp.models import HydJobs,BangaloreJobs,PuneJobs
from faker import Faker
from random import *
fake=Faker()
def phonenumbergen():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
#['date','company','title','eligibility','address','email','phonenumber']
def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany=fake.company()
        ftitle = fake.random_element(elements=('Project Manager','Team Lead','Software Engineer','Associate Engineer'))
        feligibility = fake.random_element(elements=('B.Tech','M.Tech','MCA','Phd'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        hyd_jobs_record = HydJobs.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            eligibility=feligibility,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber)
        hyd_jobs_record = BangaloreJobs.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            eligibility=feligibility,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber)
        hyd_jobs_record = PuneJobs.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            eligibility=feligibility,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber)

n = int(input('Enter Number of Records:'))
populate(n)
print(f'{n} Records Inserted Succesfully')
