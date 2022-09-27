class Employee:
    no_of_leave=8
    pass


aryan = Employee()
nidhi = Employee()


aryan.name="Aryan"
aryan.salary=100
aryan.role="Developer"

nidhi.name="Nidhi"
nidhi.salary=50
nidhi.role="developer "


print(aryan.name)
print(nidhi.salary)
print(aryan.no_of_leave)
print(Employee.no_of_leave)

aryan.no_of_leave=10
print(aryan.__dict__)

print(Employee.__dict__)