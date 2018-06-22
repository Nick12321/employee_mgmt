class Employee:
    def __init__(self, name, title, department):
        self.name = name
        self.title = title
        self.department = department

    def getEmployeeInfo(self):
        return 'Name: ' + self.name + ', title: ' + ', department: ' + self.department

class Permanent(Employee):
    def __init__(self, name, title, department):
        super().__init__(name, title, department)

    def requestVacation(self, startDate, endDate):
        print(super().name + ' has requested a vacation')

class Temporary(Employee):
    def __init__(self, name, title, department, endDate):
        super().__init__(name, title, department)
        self.endDate = endDate

    def getEmployeeInfo(self):
        return super().getEmployeeInfo() + ', End date: ' + self.endDate

class Manager(Permanent):
    def __init__(self, name, title, department):
        super().__init__(name, title, department)
        self.allEmployee = []

    def addEmployee(self, employee):
        self.allEmployee.append(employee)

    def listAllEmployees(self):
        for employee in self.allEmployee:
            print(employee.name)

class TeamLead(Permanent):
    def __init__(self, name, title, department)
    super().__init__(name)
