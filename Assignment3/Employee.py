
#Creating an Employee Class
class Employee:
    employee_count = 0

    #Constructor of Employee class which requires four parameters
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        #Counting the number of employees
        Employee.employee_count = Employee.employee_count + 1

    #Method to find the average of the salaries of the employees
    def average_Salary(self,employees_list):
        sum_of_salaries = 0
        for employee in employees_list:
            sum_of_salaries += employee.salary
        print(sum_of_salaries / len(employees_list))

#Creating a class which inherits Employee class
class FullTimeEmployee(Employee):

    def __init__(self, name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)

employees_list = []
full_time_employees_list = []

#Creating objects for Employee Class
employee1 = Employee("Naga Phaneendra", "Mogili", 295000, "Developer")
employee2 = Employee("Prasad", "Gaddam", 300000, "Manager")

#Creating objects for the FullTimeEmployee Class
employee3 = FullTimeEmployee("Stephen", "Kennedy", 295000, "HR")
employee4 = FullTimeEmployee("Uma", "Pichipati", 300000, "Tester")

employees_list.append(employee1)
employees_list.append(employee2)
full_time_employees_list.append(employee3)
full_time_employees_list.append(employee4)

#All the printing statements of the requirements
print("Printing number of employees for each class type")
print(Employee.employee_count)
print(FullTimeEmployee.employee_count)
print("-------------------------------------------------------------")

print("Printing average salaries for both of the class type employees")
employees_list[0].average_Salary(employees_list)
full_time_employees_list[0].average_Salary(full_time_employees_list)
