# class Account:
#     def __init__(self, number, pin):
#         self.number = number
#         self.pin = pin
#         self.balance = 0


# >>> from account import Account
# >>> a = Account(number = 1234, pin = 6789)
# >>> a.pin
# 6789
# >>> a.number
# 1234
# >>> a.balance
# 


class Account:
    def __init__(self, number, pin):
        self.number = number
        self.__pin = pin
        self.__balance = 0

    def show_balance(self, pin):
        if pin == self.__pin:
            return self.__balance
        
        else:
            return "Wrong pin"


# >>> my_account = Account(1234, 6789)
# >>> my_account.show_balance()
# >>> my_account.show_balance(678)
# 'Wrong pin'
# >>> my_account.show_balance(6789)
# 0

    def deposit(self, amount):
        self.__balance += amount

        print(f"{amount} has been deposited to your account. Your current balance is {self.__balance}")

# >>> from account import Account
# >>> a = Account(number = 1234, pin = 6789)
# >>> a.show_balance(pin = 678)
# 'Wrong pin'
# >>> a.deposit(amount = 5000)
# 5000 has been deposited to your account. Your current balance is 5000

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return f"{amount} has been withdrawn from your account. Your current balance is {self.__balance}"
        
        else:
            return f"Insufficient balance. Withdrawal declined."
        
# >>> a.withdraw(amount = 2000)
# '2000 has been withdrawn from your account. Your current balance is 5000'


    def view_account_details(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        print(f"Dear {self.first_name} {self.last_name}, your balance is {self.__balance}")

# >>> a.view_account_details('Eshe', 'Aziz')
# Dear Eshe Aziz, your balance is 0

    def change_account(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        print(f"Account owner updated to {self.first_name} {self.last_name}")

#     >>> a.change_account('Moureen', 'Gitahi')
# Account owner updated to Moureen Gitahi

    def account_statement(self):
        
        print(f"Available balance : {self.__balance}")


    def set_overdraft_limit(self, pin, new_limit):
        if pin == self.__pin:
            self.overdraft_limit = new_limit
            return "Overdraft limit is updated"
        else:
            return "Wrong Pin"
        
    def calculate_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        return f"Interest of {interest_amount} applied. New balance: {self.balance}"
    
    def freeze_account(self, pin):
        if pin == self.__pin:
            self.frozen = True
            return "Account is frozen"
        else:
            return "Wrong Pin"
        
    def unfreeze_account(self, pin):
        if pin == self.__pin:
            self.frozen = False
            return "Account unfrozen "
        else:
            return "Wrong Pin"
        
    def transaction_history(self):
        return self.transaction_history
    def set_minimum_balance(self, pin, new_minimum_balance):
        if pin == self.__pin:
            self.minimum_balance = new_minimum_balance
            return "Minimum balance requirement updated"
        else:
            return "Wrong Pin"
        
    def transfer_funds(self, pin, target_account, amount):
        if pin == self.__pin:
            if not self.frozen:
                if self.balance + self.overdraft_limit - amount >= self.minimum_balance:
                    self.balance -= amount
                    target_account.balance += amount
                    self.transaction_history.append(f"Transferred {amount} to account {target_account.number}")
                    return "Transfer successful"
                else:
                    return "Insufficient funds"
            else:
                return "Account frozen"
        else:
            return "Wrong Pin"
        
    def close_account(self, pin):
        if pin == self.__pin:
            self.balance = 0
            self.frozen = True
            self.owner_name = "Closed Account"
            self.transaction_history.append("Account closed")
            self.__account_status = "Closed"
            return "Account closed"
        else:
            return "Wrong Pin"



















