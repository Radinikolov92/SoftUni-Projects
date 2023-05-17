# read
deposit_total = float(input())
time_of_deposit_in_months = int(input())
index = float(input()) / 100

# logic
sum_of_deposit = deposit_total + time_of_deposit_in_months * ((deposit_total * index) / 12)

# print
print(float(sum_of_deposit))
