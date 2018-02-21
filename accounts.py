import datetime
import pytz


class Account:
    """simple account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self._transaction_list = []
        self._balance = 0
        if balance > 0:
            self.deposit(balance)

        print("Account created for " + self._name)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
            self._transaction_list.append(((Account._current_time()), -amount))
        else:
            print("The amount must be greater than zero and no more than your account your account balance")

    def show_balance(self):
        print("Balance is {}".format(self._balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


#the class creation process involves two process. The class constructor is the __init__ method. The first step is the new process and second the varibale assignment using the init method. Usually you would not need to use the new style
#in python self must be specified, unlike in java, and you must get into a habit of doing that

if __name__ == "__main__":
    tim = Account("Tim", 0)
    # tim.show_balance()

    tim.deposit(1000)
    tim.withdraw(500)
    tim.show_transactions()

    steph = Account("Steph", 800)
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()

#methods part 2
