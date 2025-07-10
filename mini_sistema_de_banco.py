menu = """

[d] Deposit
[w] withdraw
[e] Extract
[q] Quit

=> """

balance = 0
limit = 1000
balance = ""
withdraw_amount = 0
WITHDRAW_LIMIT = 5

while True:

    option = input(menu)

    if option = "d":
        value = float(input ("Insert value to be deposited: "))
        if value > 0:
            balance += value
            balance += f"Deposit: U$ {value:.2f}\n"

        else:
            print("Operation failed, the amount informed is invalid.")

    elif option == "w":
        value = float(input("Inform withdraw value: "))

        exceded_balance = value > balance

        exceded_limit = value > limit

        exceded_withdraw = withdraw_number >= WITHDRAW_LIMIT

        if exceded_balance:
            print("Operation failed! Insufficient funds.")

        elif exceded_limit:
            print("Operation failed! The amount exceed the total Balance.")

        elif exceded_withdraw:
            print("Operation failed! The number of transactions has exceeded for today.")

        elif value > 0:
            balance -= value
            balance += f"Withraw value: U$ {value:.2f}\n"
            withdraw_number += 1

        else:
            print("Operation failed! The amount informed is invalid.")

    elif option == "e":
        print("\n================ EXTRACT ================")
        print("NO RECORD OF TRANSACTIONS." if not balance else balance)
        print(f"\nBalance: U$ {balance:.2f}")
        print("==========================================")

    elif option == "q":
        break

    else:
        print("Invalid operation, please select again one of the options shown")

