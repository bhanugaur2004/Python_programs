balance = 25000
pin = "1234"

attempts = 0

while attempts < 3:

    entered_pin = input("Enter PIN: ")

    if entered_pin == pin:
        print("Login successful!")
        break

    attempts += 1

    print(
        "Incorrect PIN.",
        3 - attempts,
        "attempts remaining."
    )

else:

    print("Card blocked!")
    exit()

while True:

    print("\n====== ATM ======")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":

        print("Balance:", balance)

    elif choice == "2":

        amount = float(
            input("Deposit amount: ")
        )

        if amount > 0:
            balance += amount
            print("Deposited:", amount)

    elif choice == "3":

        amount = float(
            input("Withdrawal amount: ")
        )

        if amount > balance:
            print("Insufficient balance.")

        elif amount > 20000:
            print("Daily withdrawal limit exceeded.")

        else:
            balance -= amount
            print("Collect your cash.")

    elif choice == "4":

        print("Thank you!")
        break

    else:
        print("Invalid choice.")