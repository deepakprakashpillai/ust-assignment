import datetime

class Employee:
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.increment_employee_count()

    @classmethod
    def increment_employee_count(cls):
        cls.employee_count += 1

    @staticmethod
    def is_workday(day):
        if day.weekday() in [0, 1, 2, 3, 4]:
            return True
        return False

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)
emp3 = Employee("Charlie", 55000)

print(f"Name : {emp1.name} Salary : {emp1.salary}")
print(f"Name : {emp2.name} Salary : {emp2.salary}")
print(f"Name : {emp3.name} Salary : {emp3.salary}")


print(f"Total number of employees: {Employee.employee_count}")

today = datetime.date.today()
print(f"Is {today} a workday? {Employee.is_workday(today)}")
