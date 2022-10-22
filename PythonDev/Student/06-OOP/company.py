from datetime import datetime

class Employee:

    __minimumSalary = 12000
    __nextEmployeeID = 0

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = max(salary, Employee.__minimumSalary)
        self.__joined = datetime.now()

        self.__id = Employee.__nextEmployeeID
        Employee.__nextEmployeeID += 1

    def payRaise(self, payRiseAmount):
        self.__salary += payRiseAmount

    def payBonus(self, bonusPercentage=1, min=None, max=None):
        if (min is None or self.__salary >= min)\
                and (max is None or self.__salary <= max):
            self.__salary *= 1 + bonusPercentage / 100


    def toString(self):
        return ("[{0}] {1} earns a salary of {2}, date joined: {3}".format(self.__id, self.__name, self.__salary, self.__joined.strftime("%c")))


    def getMinimumSalary(self):
        return self.__minimumSalary

    def getEmployeeById(self, id):
        if self.__id == id:
            return Employee




