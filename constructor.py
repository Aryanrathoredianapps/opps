
#  Self

# class Employee:
#     no_of_leave=8
#     def printdetails(self):
#         return f"Name is {self.name},Salary is {self.salary},Role is {self.role}"


# aryan = Employee()
# nidhi = Employee()


# aryan.name="Aryan"
# aryan.salary=100
# aryan.role="Developer"

# nidhi.name="Nidhi"
# nidhi.salary=50
# nidhi.role="developer "

# print(aryan.printdetails())

# constructor

class Employee:
    no_of_leave=8

    def __init__(self,a_name,a_salary,a_role):
        self.name=a_name
        self.salary=a_salary
        self.role=a_role
    
    def printdetails(self):
        return f"Name is {self.name},Salary is {self.salary},Role is {self.role}"


aryan = Employee("Aryan",200000,"developer")



print(aryan.printdetails())