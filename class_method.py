


class Employee:
    no_of_leave=8

    def __init__(self,a_name,a_salary,a_role):
        self.name=a_name
        self.salary=a_salary
        self.role=a_role
    
    def printdetails(self):
        return f"Name is {self.name},Salary is {self.salary},Role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves) :
    cls.no_of_leaves=newleaves


aryan = Employee("Aryan",200000,"developer")
nidhi = Employee("Nidhi",20,"analyst")


nidhi.change_leaves(3)
print(aryan.no_of_leaves)