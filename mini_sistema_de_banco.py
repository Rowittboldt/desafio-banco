menu = """

[d] Deposit
[w] Withdraw
[e] Extract
[q] Quit

=> """

balance = 0
limit = 1000
extract = ""
withdraw_number = 0
WITHDRAW_LIMIT = 5

while True:
    option = input(menu)

    if option == "d":
        value = float(input("Insert value to be deposited: "))
        if value > 0:
            balance += value
            extract += f"Deposit: U$ {value:.2f}\n"
            print("Deposit made successfully!")
        else:
            print("Operation failed, the amount informed is invalid.")

    elif option == "w":
        value = float(input("Inform withdraw value: "))

        exceeded_balance = value > balance
        exceeded_limit = value > limit
        exceeded_withdraw = withdraw_number >= WITHDRAW_LIMIT

        if exceeded_balance:
            print("Operation failed! Insufficient funds.")
        elif exceeded_limit:
            print("Operation failed! The amount exceeds the limit.")
        elif exceeded_withdraw:
            print("Operation failed! The number of transactions has exceeded for today.")
        elif value > 0:
            balance -= value
            extract += f"Withdraw: U$ {value:.2f}\n"
            withdraw_number += 1
            print("Money Withdrawn successfully, please take your money from the bin.")
        else:
            print("Operation failed! The amount informed is invalid.")

    elif option == "e":
        print("\n================ EXTRACT ================")
        print("NO RECORD OF TRANSACTIONS." if not extract else extract)
        print(f"\nBalance: U$ {balance:.2f}")
        print("==========================================")

    elif option == "q":
        break

    else:
        print("Invalid operation, please select again one of the options shown")
