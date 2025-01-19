class WithdrawError(Exception):             # custom exception
    pass

class Bank:

    def __init__(self,bank_name):
        self.bank_name = bank_name


class Account(Bank):

    def set_balance(self,bal):
        self.balance = bal

    def get_balance(self):
        return self.balance
    
    def credit_amt(self,amount):
        self.balance += amount
        print(f"{amount}/- Credited Successfully!")

    def debit_amt(self,amount):
        try:
            if(amount > self.balance):
                raise WithdrawError()
        except WithdrawError:
            print("Insufficient Amount!")
        else:
            self.balance -= amount
            print(f"{amount}/- debited successfully!")


class Customer(Account):

    def __init__(self,name,acc_no):
        self.c_name = name
        self.acc_no = acc_no

c1 = Customer("Zed",1234)
c1.set_balance(200)
print(c1.get_balance())
c1.credit_amt(350)
c1.debit_amt(1000)
