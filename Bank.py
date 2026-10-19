def check_balance():
    print("Checkig balance...")
    print(f"Your balance is {balance}")

def deposit(deposit_amount):
    global balance
    if deposit_amount > 0:    
        print("Depositing money...")
        balance += deposit_amount
    else:
        print("Can't deposit a negetive or zero amount.")


def withdraw(withdraw_amount):
    global balance
    

    if withdraw_amount > balance:
        print("You don't have sufficient balance. Enter another amount.")
        return 0

    elif 0 < withdraw_amount <= balance:
        print("Withdrawing money...")
        balance -= withdraw_amount

    elif withdraw_amount <= 0:
        print("Can't withdraw a negetive or zaro amount.")    

print("---Welcome to RaZf Bank---")

balance = 100

while True:
    print("1. Checking balance")
    print("2. Deposit money")
    print("3. Withdrwa money")
    print("4. Exit")
    choice = (input("Enter a choice(1-4): "))


    if choice == '1':
        check_balance()


    elif choice == '2':
        deposit_amount = float(input("Enter the deposit amount: "))
        deposit(deposit_amount)


    elif choice == '3':
        withdraw_amount = float(input("Enter the withdraw amount: "))
        withdraw(withdraw_amount)


    elif choice == '4':
        break


    else:
        print("Invalid input. Please Re-try.")


print("Thank You.")        