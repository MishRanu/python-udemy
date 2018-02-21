import sqlite3
import pytz
import datetime

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS transactions (time TIMESTAMP NOT NULL,"
           "account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY(time, account))")


class Account(object):

    @staticmethod
    def _current_time():
        return pytz.utc.localize(datetime.datetime.utcnow())

    def __init__(self, name: str, opening_balance : int = 0):
        cursor = db.execute("SELECT name, balance FROM ACCOUNTS WHERE (name = ?)", (name,))
        row = cursor.fetchone()
        if row:
            self.name, self._balance = row
            print("Retrieved record for {}. ".format(self.name), end='')
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print("Account created for {}. ".format(self.name), end='')
        self.show_balance()

    def _update_and_save(self, amount: int):
        curr_balance = self._balance + amount
        curr_time = Account._current_time()
        db.execute("INSERT INTO transactions VALUES(?, ?, ?)", (curr_time, self.name, amount))
        db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (curr_balance, self.name))
        db.commit()
        self._balance = curr_balance

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            self._update_and_save(amount)
            print("{} deposited ".format(amount/100))
            return self._balance/100

    def withdraw(self, amount: int)->float:
        if 0<amount<=self._balance:
            self._update_and_save(-amount)
            print("{} withdrawn".format(amount/100))
            return self._balance/100
        else:
            print("The amount must be greater than zero and no more than your account balance")
            return self._balance/100

    def show_balance(self):
        print("Balance on account {} is {} ".format(self.name, self._balance/100))


if __name__ == "__main__":
    john = Account("John")
    john.deposit(1010)
    john.deposit(10)
    john.deposit(10)
    john.withdraw(30)
    john.withdraw(0)
    john.show_balance()

    terry = Account("Terry")
    graham = Account("Graham", 9000)
    eric = Account("Eric", 7000)
