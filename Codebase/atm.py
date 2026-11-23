# ATM MANAGEMENT SYSTEM

# Default Account Details
correct_pin = "1234"
default_balance = 10000


# Function to save data in file
def save_data(balance, transactions):
    try:
        with open("Codebase/atm.txt", "w") as file:
            file.write(str(balance) + "\n")

            for transaction in transactions:
                file.write(transaction + "\n")

    except OSError:
        print("Error: Unable to save ATM data!")
    except (ValueError, OSError):
        print("Error reading file!")

# Function to load data from file
def load_data():
    try:
        with open("Codebase/atm.txt", "r") as file:
            balance = int(file.readline())

            transactions = []

            for line in file:
                transactions.append(line.strip())

        return balance, transactions

    except FileNotFoundError:
        return default_balance, []

    except (ValueError, OSError):
        print("Error reading file!")
        return default_balance, []


# Function to check balance
def check_balance(balance):
    print("Current Balance:", balance)


# Function to deposit money
def deposit(balance, transactions):
    try:
        amount = int(input("Enter deposit amount: "))

        if amount > 0:
            balance = balance + amount

            transactions.append(
                "Deposit " + str(amount) + " | Balance: " + str(balance)
            )

            print("Deposit successful!")
            print("New Balance:", balance)

            save_data(balance, transactions)

        else:
            print("Invalid amount!")

    except ValueError:
        print("Invalid amount. Please enter numbers only.")

    return balance, transactions


# Function to withdraw money
def withdraw(balance, transactions):
    try:
        amount = int(input("Enter withdrawal amount: "))

        if amount > 0:

            if amount <= balance:
                balance = balance - amount

                transactions.append(
                    "Withdraw " + str(amount) + " | Balance: " + str(balance)
                )

                print("Withdrawal successful!")
                print("New Balance:", balance)

                save_data(balance, transactions)

            else:
                print("Insufficient balance!")

        else:
            print("Invalid amount!")

    except ValueError:
        print("Invalid amount. Please enter numbers only.")

    return balance, transactions


# Function to display mini statement
def mini_statement(balance, transactions):
    print("\n===== MINI STATEMENT =====")

    if len(transactions) == 0:
        print("No transactions yet.")

    else:
        count = 1

        for transaction in transactions:
            print(count, ".", transaction)
            count = count + 1

    print("Current Balance:", balance)


# PIN Verification
for attempt in range(3):

    pin = input("Enter your PIN: ")

    if pin == correct_pin:
        print("Login successful!")
        break

    else:
        if attempt < 2:
            print("Invalid PIN. Attempts left:", 2 - attempt)

else:
    print("Account locked. Exiting...")
    quit()


def main():
# Load previous account data
    balance, transactions = load_data()

#ATM Menu:
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Mini Statement")
        print("5. Exit")


        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            balance, transactions = deposit(balance, transactions)

        elif choice == "3":
            balance, transactions = withdraw(balance, transactions)

        elif choice == "4":
            mini_statement(balance, transactions)

        elif choice == "5":
            save_data(balance, transactions)
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__== "__main__":
    main()




