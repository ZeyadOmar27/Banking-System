class BankAccount:
    def __init__(self, name, initial_amount):
        self.name = name
        self.initial = initial_amount

    def get_balance(self):
        print(f"Account '{self.name}' created \nBalance: ${self.initial:.2f} ")
    
    def deposit(self, deposit_amount):
        if deposit_amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.initial = self.initial + deposit_amount
    
    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.initial:
            print("Insufficient funds")
        elif withdraw_amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.initial = self.initial - withdraw_amount

    def transfer(self, amount, receiver):
        if self.initial >= amount:
            self.initial = self.initial - amount
            receiver.initial += amount
        else:
            print("Insufficient funds")

