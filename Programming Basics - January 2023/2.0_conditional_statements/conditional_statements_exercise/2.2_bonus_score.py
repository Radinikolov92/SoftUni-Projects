# read
score = int(input())

# logic
if score <= 100:
    bonus = 5
elif score > 1000:
    bonus = score * 0.10
else:
    bonus = score * 0.20
if score % 2 == 0:
    bonus += 1
elif score % 10 == 5:
    bonus += 2

# print
print(bonus)
print(score + bonus)
