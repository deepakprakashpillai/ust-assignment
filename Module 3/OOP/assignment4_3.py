class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def display_person_details(self):
        return f"Name: {self.name}, Age: {self.age}"

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)  
        self.employee_id = employee_id 

    def display_employee_details(self):
        return f"{self.display_person_details()}, Employee ID: {self.employee_id}"

class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name 

    def display_department(self):
        return f"Department: {self.dept_name}"

class Manager(Employee, Department):
    def __init__(self, name, age, employee_id, dept_name):
        Employee.__init__(self, name, age, employee_id)  
        Department.__init__(self, dept_name) 

    def display_manager_details(self):
        return f"{self.display_employee_details()}, {self.display_department()}"

manager = Manager(name="John", age=35, employee_id="E123", dept_name="IT")

print(manager.display_manager_details())
