class Account:
    def __init__(self,owner,balance =0):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return "Account owner: %s, Account balance: %s" %(self.owner, self.balance)

    def deposit(self, amount):
        self.balance += amount
        print(f"Your current balance is {self.balance}.")
        print(f"Your have successfully logged {amount}!")
        return self.balance
    def withdraw(self, amount_withdraw):
        if (amount_withdraw <= self.balance):
            self.balance -= amount_withdraw
        else:
            print("Not enough money to withdraw!")
        return self.balance
# 1. Instantiate the class
acct1 = Account('JJ',10000)
# 2. Print the object
print(acct1) # Account owner: Jose, Account balance: €100
# 3. Show the account owner attribute
acct1.owner # 'Jose'
# 4. Show the account balance attribute
acct1.balance # 100
# 5. Make a series of deposits and withdrawals
acct1.deposit(50) # Deposit Accepted
acct1.withdraw(75) # Withdrawal Accepted
# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500) # Funds Unavailable!

