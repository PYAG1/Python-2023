from abc import  ABC, abstractmethod

class Bank(ABC):
    def basicinfo(self):
        print("This is a geberic bank")
        return "Generic bank: 0"
    @abstractmethod
    def withdraw(self):
        pass


class Swiss(Bank):#inherits from the Bank Class
    def __init__(self):
        self.bal = 1000

    def basicinfo(self):
        print("This is the Swiss Bank")
        return "Swiss Bank:"+ self.bal
    
    def withdraw(self,amount):
            self.bal = self.bal - amount
            print("Withdrawn amount"+ amount)
    
        