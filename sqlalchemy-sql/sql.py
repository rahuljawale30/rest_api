from configuration import db


class Employee(db.Model):
    id = db.Column('empid',db.Integer(),primary_key = True)
    name = db.Column('empname',db.String(40),null=True)
    email = db.Column('empemail',db.String(50),unique=True)
    role = db.Column('emprole',db.String(40))
    salary = db.Column('empsalary',db.Float())
    address = db.Column('empaddress',db.String(255))
    date = db.Column('empdate',db.Datetime())

    class meta:
        __table_name__ = Employee
# for create table
db.create.all()

e1 = Employee(1,'rahul','rahuljawale30@gmail.com','Manager', 23443.34,'Pune')
db.session.add()
db.session.commit()

e2 = Employee(2,'madan','rahuljawale0@gmail.com','Assist-Manager', 23443.34,'Pune')
e3 = Employee(3,'anup','rahuljawale90@gmail.com','developer', 23443.34,'Pune')
e4 = Employee(4,'nakul','rahuljawale93@gmail.com','jr developer', 23443.34,'Pune')
db.session.add_all([e2,e3,e4])
db.session.commit()

emp1 = Employee.query.filter_by(id=101).first()
print(emp1)

emplist = Employee.query.all()
print(emplist)

emp2 = Employee.query.filter_by(id=102).first()
if emp2:
    db.session.delete()
    db.session.commit()

emp3 = Employee.query.filter_by(id=103).first()
if emp3:
    emp3.name ='Yogesh'
    db.session.commit()

# to count the by name,role, department
count = Employee.query.filter(role='manager').count()

# to count all the emplyee where name= rahul
name = Employee.query.filter_by(name='rahul').all()

# to apply filter
emp = Employee.query.filter_by(Employee.id>2).all()

emp = Employee.query.filter_by(Employee.id!=2)

emp = Employee.query.filter_by(Employee.id)


like =  Employee.query().filter(Employee.name.like('Ra%'))

# In operator
result = Employee.query.filter(Employee.id.in_([1, 3]))
for row in result:
    print(row)

# Like Operator
result = Employee.query.filter(Employee.id > 2, Employee.name.like('Ra%'))
for row in result:

from sqlalchemy import or_
result = Employee.query.filter(or_(Employee.id > 2, Employee.name.like('Ra%')))
for row in result:
