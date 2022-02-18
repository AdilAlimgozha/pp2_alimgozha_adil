class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self):
        self.depos = int(input("add money: "))
        self.balance = self.balance + self.depos
        print("Your balance now: ", self.balance)
    
    def withdraw(self):
        self.withdr = int(input("How much money do you want to withdraw? "))
        if self.withdr <= self.balance:
            self.balance = self.balance - self.withdr
            print("Your balance now: ", self.balance)
        else:
            self.balance = self.balance - self.withdr
            print("Overdrawn")

acc = Account(input(), int(input()))
while acc.balance >= 0:
    action = input("add or withdraw?")
    if action == "add":
        acc.deposit()
    elif action == "withdraw":
        acc.withdraw()
#done