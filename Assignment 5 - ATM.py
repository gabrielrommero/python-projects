from BankAccount import BankAccount

bank_accounts = [BankAccount("jsmith","1452",156.21), 
BankAccount("aobrien","9892",856.21), 
BankAccount("hpotter","6001",43.50), 
BankAccount("hgranger","6993")]

pin_input = input("PIN: ")

user_account = None

for p in bank_accounts:
    if pin_input == p.pin:
        user_account = p
        break
    else:
        print("Incorrect PIN.")
if user_account is not None:
    while True:
        print("\n 1. Withdraw\n 2. Deposit\n 3. Check Balance\n 4. Check Overdraft Status\n 5. Exit")
        option = int(input("\nChoose an Option: "))
        if option == 1:
            value = float(input("Amount: "))
            user_account.withdraw(value)
        if option == 2:
            value = float(input("Amount: "))
            user_account.deposit(value)
        if option == 3:
            print(user_account.balance)
        if option == 4:
            print(user_account.overdraft_status)
        if option == 5:
            print("Thank you.")
            break
else:
    print("Invalid Option. Please, try again.")