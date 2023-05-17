# read
change = int(float(input()) * 100)
coins = 0

# calculation
two_lev = 200
one_lev = 100
fifty_cent = 50
twenty_cent = 20
ten_cent = 10
five_cent = 5
three_cent = 3
two_cent = 2
once_cent = 1

# logic
while change > 0:
    if change >= two_lev:
        change -= two_lev
    elif change >= one_lev:
        change -= one_lev
    elif change >= fifty_cent:
        change -= fifty_cent
    elif change >= twenty_cent:
        change -= twenty_cent
    elif change >= ten_cent:
        change -= ten_cent
    elif change >= five_cent:
        change -= five_cent
    elif change >= two_cent:
        change -= two_cent
    elif change >= once_cent:
        change -= once_cent

    coins += 1

# print
print(coins)
