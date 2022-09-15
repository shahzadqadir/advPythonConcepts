
class Employee:

    raise_amount = 1.04
    number_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + "." + self.last + "@company.com"

        Employee.number_of_employees += 1

    def full_name(self):
        return self.first + " " + self.last

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def fromstring(cls, input_string):
        first, last, pay = input_string.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


import datetime
day = datetime.date(2020, 10, 16)
print(Employee.is_workday(day))