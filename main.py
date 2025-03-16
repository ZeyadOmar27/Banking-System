from bank_accounts import *

accounts = []
transactions = []
while True:
    try:
        number_of_accounts = int(input("Enter the number of accounts to be created: "))
        break
    except ValueError:
        continue

for i in range(number_of_accounts):
    while True:
        try:
            name = input("Account name: ")
            if name.isalpha():
                break
            else:
                raise ValueError
        except ValueError:
            print("please enter letters only")   
    while True:
        try:
            balance = float(input(f"Enter initial balance for {name}: "))
            break
        except ValueError:
            print(f"please re-enter initial balance for {name}:")
    accounts.append(BankAccount(name,balance))
            

        
print("\nCreated Accounts:")
for account in accounts:
    account.get_balance()

while True:
    bank_activity = input("\nDeposit, Withdraw, Transfer, Transactions: ")
    if bank_activity.lower() == ("deposit"):
        deposit_name = input("Enter account name to deposit: ")
        for account in accounts:
            if account.name == deposit_name:
                deposit_amount = float(input("How much do you want to deposit: "))
                account.deposit(deposit_amount)
                print(f"• {deposit_name}'s balance: {account.initial}$")
                transactions.append(f"{deposit_amount}$ have been deposited into {deposit_name}'s account")
                break
        else:
            print("Check the account's name")
                
    elif bank_activity.lower() == ("withdraw"):
        withdraw_name = input("Enter account name to withdraw: ")
        for account in accounts:
            if account.name == withdraw_name:
                withdraw_amount = float(input("How much do you want to withdraw: "))
                account.withdraw(withdraw_amount)
                print(f"• {withdraw_name}'s balance: {account.initial}$")
                transactions.append(f"{withdraw_amount}$ have been withdrawn from {withdraw_name}'s account")
                break
        else:
            print("Check the account's name")
                  
    elif bank_activity.lower() == ("transfer"):
        sender_name = input("Sender name: ")
        receiver_name = input("Reciever name: ")
        amount = float(input("Amount to transfer: "))

        sender = None
        receiver = None

        for account in accounts:
            if account.name == sender_name:
                sender = account
            if account.name == receiver_name:
                receiver = account

        if sender and receiver:
            sender.transfer(amount, receiver)
            print(f"\n• {sender_name}'s balance: {sender.initial}$")
            print(f"• {receiver_name}'s balance: {receiver.initial}$")
            transactions.append(f"{sender_name} has sent {amount}$ to {receiver_name}")
            

        else:
            print("Check the sender and receiver account names.")

    elif bank_activity == ("transactions").lower():
        if not transactions:
            print("There is no transactions yet")
        else:
            print("\ntransactions:")
            for transaction in transactions:
                print(f"• {transaction}")
          

    else:
        print("Invalid option. Please enter Deposit, Withdraw, Transfer, or Transactions.")
        