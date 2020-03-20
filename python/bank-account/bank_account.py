import threading

class BankAccount(object):
    
    def is_open(func):
        def wrapper(self, *args):
            if self._status is not "opened":
                raise ValueError("Account not opened")
            return func(self, *args)
        return wrapper
    
    def __init__(self):
        self.balance = 0
        self._lock = threading.Lock()

    @is_open
    def get_balance(self):
        return self.balance

    def open(self):
        self._status = "opened"

    @is_open
    def deposit(self, amount):
        self._lock.acquire()
        try:
            if amount < 0:
                raise ValueError("Transaction not possible")
            self.balance += amount
        finally:
            self._lock.release()
        return self.balance

    @is_open
    def withdraw(self, amount):
        self._lock.acquire()
        try:
            self.balance -= amount
            if amount < 0 or self.balance < 0:
                raise ValueError("Transaction not possible")
        finally:
            self._lock.release()
        return self.balanc

    def close(self):
        self._status = "closed"
