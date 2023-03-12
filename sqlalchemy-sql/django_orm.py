from django.db.models import models

class Employee(models.Model):
    name = models.CharField(max_len=30)
    email = models.EmailField()
    role =  models.CharField(max_len=230)
    salary = models.FloatField()
    address = models.TextField(max_len=255)
    contact = models.BigIntegerField()
    date = models.DateField()

# insert into database
Employee.object.create(name='rahul',email='rahul@gmail.com',role='developer',salary=23445.23,address='Pune',contact=893484348,date=2-10-2022)

# bulk insert into database



# select all employee
employees = Employee.object.all()

# select specific employee
emp1 = Employee.object.filer(id=1)
emp2 = Employee.object.get(id=2)

# for specific columan
Employee.object.only('name','email')

# distinct
Employee.object.values('name','age').distinct()

# to select the limit
Employee.object.all[:10]
Employee.object.all[5:20]

# select by greater than or less than
Employee.object.filter(age__gt=18)  #>
Employee.object.filter(age__gte=18)  #>=
Employee.object.filter(age__lt=18)   #<
Employee.object.filter(age__gte=18)  #<=

# bETWEEN OPERATOR
Employee.object.filter(age__range=(10,33))

# Like Operator
Employee.object.filter(name__icontain='A')
Employee.object.filter(name__contain='A')

Employee.object.filter(name__isstartwith="A")
Employee.object.filter(name__startwith="A")

Employee.object.filter(name__isendwith="A")
Employee.object.filter(name__endwith="A")

# IN OPERATOR
# where id in (1,9)
Employee.object.filter(id__in=[1,4])

# AND OPERATOR
Employee.objects.filter(role="developer", address='Pune' )

# OR OPERATOR
from django.db.models import Q
Employee.objects.filter(Q(role='developer')|Q(address='Pune'))

#NOT EQUAL TO
Employee.objects.exclude(rolr='developer')

# ORDER BY ASC DESC
Employee.objects.order_by('role')
Employee.objects.order_by('-role')

# update the employee
emp = Employee.objects.get(id=1)
emp.name= 'madan'
emp.save()

# Update the multiple row for eg we want to increase the salary by 10 %
from django.db.models import F
Employee.objects.update(salary=F('salary')*1.0)

# DELETE THE EMPLOYEE
Employee.objects.all().delete()

Employee.objects.filter(age__gt=10).delete()

## Aggregation
from django.db.models import Min
Employee.objects.all().aggregate(Min('Age')){'age__min':10}

from django.db.models import Max
Employee.objects.all().aggregate(Max()){'age__max':30}

from django.db.models import Sum
Employee.objects.all().aggregate(Sum()){'age__sum':505}

# HAVING CLAUSE
# SELECT * COUNT('gender') FROM Person GROUP BY gender HAVING count > 1;
Employee.objects.annotate(count=Count('gender')).values('gender','count').filter(count__gt=1)

# JOINS
class Address(models.Model):
    address = models.CharField(max_lenght=100)

class Employee(models.Model):
    name = models.CharField(max_len=60)
    Employee = models.ForeignKey(Employee, on_delete= models.CASCADE)

employee = Employee.objects.select_related('Address').get(id=1)address.employee.name

