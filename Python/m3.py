# Program: Emulating ATM machine

def deposit(balance, amount):
    balance += amount
    return balance


def withdraw(balance, amount):
    balance -= amount
    return balance


def check_balance(balance):
    print("Current balance:", balance)
    return balance


def main():
    balance = 0
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            amount = int(input("Enter the amount to deposit: "))
            balance = deposit(balance, amount)
        elif choice == 2:
            amount = int(input("Enter the amount to withdraw: "))
            balance = withdraw(balance, amount)
        elif choice == 3:
            balance = check_balance(balance)
        elif choice == 4:
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
