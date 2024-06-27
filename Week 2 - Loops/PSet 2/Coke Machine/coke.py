amount_due = 50

while amount_due != 0:
    print(f"Amount Due: {amount_due}")

    money_recieved = (int(input("Insert Coin: ")))
    while money_recieved <= 0 or money_recieved not in [25, 10, 5]:
        print(f"Amount Due: {amount_due}")
        money_recieved = (int(input("Insert Coin: ")))

    if money_recieved >= amount_due:
        print(f"Change Owed: {money_recieved - amount_due}")
        amount_due = 0

    else:
        amount_due = amount_due - money_recieved

