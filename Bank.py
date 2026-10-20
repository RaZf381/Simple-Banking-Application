
from datetime import datetime


# ==============================
#       RAZF BANK SYSTEM
# ==============================

balance = 0.0
account_number = "RAZF100001"

customer_name = ""
customer_age = 0
customer_phone = ""

kyc_completed = False
card_issued = False
card_active = False

interest_rate = 4.0

transactions = []


# ==============================
#       DESIGN FUNCTIONS
# ==============================

def line():
    print("=" * 42)


def heading(title):
    line()
    print(f"{title:^42}")
    line()


def pause():
    input("\nPress Enter to continue...")


def record_transaction(transaction_type, amount):
    transactions.append({
        "type": transaction_type,
        "amount": amount,
        "balance": balance,
        "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    })


# ==============================
#       INPUT VALIDATION
# ==============================

def get_amount(message):
    while True:
        try:
            amount = float(input(message))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            if not amount < float("inf"):
                print("Please enter a valid amount.")
                continue

            return round(amount, 2)

        except ValueError:
            print("Invalid input! Enter a number.")


def get_menu_choice(message, valid_choices):
    while True:
        choice = input(message).strip()

        if choice in valid_choices:
            return choice

        print("Invalid choice. Please try again.")


# ==============================
#       ACCOUNT FUNCTIONS
# ==============================

def check_balance():
    heading("ACCOUNT BALANCE")
    print(f"Account Number : {account_number}")
    print(f"Available Balance: Rs. {balance:.2f}")


def deposit():
    global balance

    heading("DEPOSIT MONEY")
    amount = get_amount("Enter deposit amount: Rs. ")

    balance = round(balance + amount, 2)
    record_transaction("Deposit", amount)

    print(f"Rs. {amount:.2f} deposited successfully.")
    print(f"New balance: Rs. {balance:.2f}")


def withdraw():
    global balance

    heading("WITHDRAW MONEY")
    amount = get_amount("Enter withdrawal amount: Rs. ")

    if amount > balance:
        print("Insufficient balance!")
        print(f"Available balance: Rs. {balance:.2f}")
        return

    balance = round(balance - amount, 2)
    record_transaction("Withdrawal", amount)

    print(f"Rs. {amount:.2f} withdrawn successfully.")
    print(f"Remaining balance: Rs. {balance:.2f}")


def transfer_money():
    global balance

    heading("MONEY TRANSFER")

    recipient = input("Enter recipient name: ").strip()

    if not recipient:
        print("Recipient name cannot be empty.")
        return

    amount = get_amount("Enter transfer amount: Rs. ")

    if amount > balance:
        print("Insufficient balance!")
        return

    balance = round(balance - amount, 2)
    record_transaction(f"Transfer to {recipient}", amount)

    print(f"Rs. {amount:.2f} transferred successfully.")
    print(f"Recipient: {recipient}")
    print(f"Remaining balance: Rs. {balance:.2f}")


# ==============================
#       TRANSACTION HISTORY
# ==============================

def transaction_history():
    heading("TRANSACTION HISTORY")

    if not transactions:
        print("No transactions have been made yet.")
        return

    for number, transaction in enumerate(transactions, start=1):
        print(f"\nTransaction {number}")
        print(f"Type: {transaction['type']}")
        print(f"Amount: Rs. {transaction['amount']:.2f}")
        print(f"Balance after transaction: "
              f"Rs. {transaction['balance']:.2f}")
        print(f"Date: {transaction['time']}")
        print("-" * 42)


# ==============================
#       ACCOUNT CREATION
# ==============================

def create_account():
    global customer_name, customer_age, customer_phone

    heading("CUSTOMER REGISTRATION")

    if customer_name:
        print("An account has already been created.")
        print(f"Account number: {account_number}")
        return

    name = input("Enter your name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    while True:
        try:
            age = int(input("Enter your age: "))

            if age < 18:
                print("This demo requires customers to be 18 or older.")
                return

            if age > 120:
                print("Please enter a valid age.")
                continue

            break

        except ValueError:
            print("Age must be a whole number.")

    phone = input("Enter a 10-digit demo phone number: ").strip()

    if len(phone) != 10 or not phone.isdigit():
        print("Invalid phone number.")
        return

    customer_name = name
    customer_age = age
    customer_phone = phone

    print("\nAccount created successfully!")
    print(f"Customer name: {customer_name}")
    print(f"Account number: {account_number}")
    print("Complete KYC to access card facilities.")


def account_details():
    heading("ACCOUNT DETAILS")

    if not customer_name:
        print("Please create an account first.")
        return

    print(f"Name: {customer_name}")
    print(f"Age: {customer_age}")
    print(f"Account number: {account_number}")
    print(f"Phone: {customer_phone}")
    print(f"KYC status: {'Completed' if kyc_completed else 'Pending'}")
    print(f"Debit card: {'Issued' if card_issued else 'Not issued'}")
    print(f"Card status: "
          f"{'Active' if card_active else 'Inactive or blocked'}")
    print(f"Balance: Rs. {balance:.2f}")


# ==============================
#       KYC VERIFICATION
# ==============================

def complete_kyc():
    global kyc_completed

    heading("KYC VERIFICATION")

    if not customer_name:
        print("Please create an account first.")
        return

    if kyc_completed:
        print("Your demo KYC is already completed.")
        return

    print("This is a simulated KYC process.")
    print("Do not enter real identity documents.")

    consent = get_menu_choice(
        "Confirm demo verification? (y/n): ",
        ["y", "Y", "n", "N"]
    )

    if consent.lower() == "y":
        kyc_completed = True
        print("Demo KYC completed successfully!")
    else:
        print("KYC verification cancelled.")


# ==============================
#       INTEREST CALCULATOR
# ==============================

def calculate_interest():
    heading("SAVINGS INTEREST")

    print(f"Annual interest rate: {interest_rate:.2f}%")
    print(f"Current balance: Rs. {balance:.2f}")

    try:
        years = float(input("Enter time period in years: "))

        if not 0 < years <= 100:
            print("Enter a period greater than 0 and up to 100 years.")
            return

        interest = balance * interest_rate * years / 100
        final_balance = balance + interest

        print(f"\nEstimated simple interest: Rs. {interest:.2f}")
        print(f"Balance after interest: Rs. {final_balance:.2f}")
        print("This is an estimate, not an actual bank credit.")

    except ValueError:
        print("Invalid input! Enter a number.")


# ==============================
#       DEBIT CARD FUNCTIONS
# ==============================

def issue_card():
    global card_issued

    heading("DEBIT CARD APPLICATION")

    if not customer_name:
        print("Please create an account first.")
        return

    if not kyc_completed:
        print("Complete KYC before applying for a card.")
        return

    if card_issued:
        print("A demo debit card has already been issued.")
        return

    card_issued = True
    print("Your demo debit card has been issued!")
    print("Activate it using the card menu.")


def activate_card():
    global card_active

    heading("ACTIVATE DEBIT CARD")

    if not card_issued:
        print("Apply for a debit card first.")
        return

    if card_active:
        print("Your card is already active.")
        return

    card_active = True
    print("Demo debit card activated successfully!")


def block_card():
    global card_active

    heading("BLOCK DEBIT CARD")

    if not card_issued:
        print("No debit card has been issued.")
        return

    if not card_active:
        print("Your card is already inactive or blocked.")
        return

    card_active = False
    print("Your demo debit card has been blocked.")


def card_purchase():
    global balance

    heading("DEBIT CARD PURCHASE")

    if not card_issued or not card_active:
        print("Your debit card is not active.")
        return

    amount = get_amount("Enter purchase amount: Rs. ")

    if amount > balance:
        print("Transaction declined: insufficient balance.")
        return

    balance = round(balance - amount, 2)
    record_transaction("Debit card purchase", amount)

    print("Purchase successful!")
    print(f"Amount paid: Rs. {amount:.2f}")
    print(f"Remaining balance: Rs. {balance:.2f}")


# ==============================
#       MAIN MENU
# ==============================

def banking_menu():
    while True:
        heading("WELCOME TO RAZF BANK")

        print("1.  Check balance")
        print("2.  Deposit money")
        print("3.  Withdraw money")
        print("4.  Transfer money")
        print("5.  Transaction history")
        print("6.  Create account")
        print("7.  Complete KYC")
        print("8.  View account details")
        print("9.  Calculate interest")
        print("10. Apply for debit card")
        print("11. Activate debit card")
        print("12. Block debit card")
        print("13. Make debit card purchase")
        print("14. Exit")

        line()

        choice = get_menu_choice(
            "Enter your choice (1-14): ",
            [str(i) for i in range(1, 15)]
        )

        print()

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            transfer_money()
        elif choice == "5":
            transaction_history()
        elif choice == "6":
            create_account()
        elif choice == "7":
            complete_kyc()
        elif choice == "8":
            account_details()
        elif choice == "9":
            calculate_interest()
        elif choice == "10":
            issue_card()
        elif choice == "11":
            activate_card()
        elif choice == "12":
            block_card()
        elif choice == "13":
            card_purchase()
        elif choice == "14":
            heading("THANK YOU")
            print("Thank you for using RaZf Bank!")
            print("Have a great day.")
            break

        pause()


# ==============================
#       START APPLICATION
# ==============================

banking_menu()
