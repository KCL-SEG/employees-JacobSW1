"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, pay, monthly, hours = 0, fixed = None, commission_pay = 0, number_of_contracts = 0):
        self.name = name
        self.monthly = monthly
        self.pay = pay
        self.hours = hours
        self.commission_pay = commission_pay
        self.fixed = fixed
        self.number_of_contracts = number_of_contracts

    def get_pay(self):
        return self.get_total_contract_pay() + self.get_total_commission_pay()

    def get_total_contract_pay(self):
        if self.monthly:
            return self.pay
        else:
            return self.pay * self.hours
    
    def get_total_commission_pay(self):
        if self.fixed:
            return self.commission_pay
        else:
            return self.commission_pay * self.number_of_contracts


    def __str__(self):
        return f"{self.contract_pay()}{self.commission()}. Their total pay is {self.get_pay()}."

    def contract_pay(self):
        if self.monthly:
             return f"{self.name} works on a monthly salary of {self.pay}"
        else:
            return f"{self.name} works on a contract of {self.hours} hours at {self.pay}/hour"
    
    def commission(self):
        if self.fixed and self.commission_pay > 0:
            return f" and receives a bonus commission of {self.commission_pay}"
        elif not self.fixed and self.commission_pay > 0:
            return f" and receives a commission for {self.number_of_contracts} contract(s) at {self.commission_pay}/contract"
        else: 
            return ""


            



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, True)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 25, False, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, True, 0, False, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 25, False, 150, False, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, True, 0, True, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 30, False, 120, True, 600)
