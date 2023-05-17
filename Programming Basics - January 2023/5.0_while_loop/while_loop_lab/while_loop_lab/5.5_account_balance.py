# read
account_balance = 0

# logic
while True:
    deposit = input()

    if deposit == "NoMoreMoney":
        print(f"Total: {account_balance:.2f}")
        break

    deposit = float(deposit)

    if deposit >= 0:
        account_balance += deposit
        print(f"Increase: {deposit:.2f}")

    else:
        print("Invalid operation!")
        print(f"Total: {account_balance:.2f}")
        break
