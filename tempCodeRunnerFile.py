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
            if self.bal < amount:
                 print(" Insufficient Funds")
                 return self.bal
            else:
                self.bal = self.bal - amount
                print("Withdrawn amount"+ amount)
                print("New balance is " + self.bal)
                return self.bal
        
    
        