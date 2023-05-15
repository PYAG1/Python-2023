from abc import  ABC, abstractmethod

class Bank(ABC):
    def basicinfo(self):
        print("This is a geberic bank")
        return "Generic bank: 0"
    @abstractmethod
    def withdraw(self):
        pass


class Swiss(Bank):#inherits from the Bank Class
    