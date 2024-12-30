import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fbvcrudproject.settings')
import django
django.setup()

from testapp.models import Employee
from faker import Faker
faker=Faker()
from random import *
def populate(n):
    for i in range(n):
        feno=randint(1001,9999)
        fename=faker.name()
        fesal=randint(10000,20000)
        feaddr=faker.city()
        emp_record=Employee.objects.get_or_create(
            eno=feno,
            ename=fename,
            esal=fesal,
            eaddr=feaddr
        )
n=int(input('Enter Number of Employess:'))
populate(n)
print(f'{n} is recorded')