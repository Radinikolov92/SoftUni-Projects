# read
count = int(input())

# logic
numbers_p1 = 0
numbers_p2 = 0
numbers_p3 = 0
numbers_p4 = 0
numbers_p5 = 0
for n in range(1, count + 1):
    num = int(input())
    if num < 200:
        numbers_p1 += 1
    elif 200 <= num <= 399:
        numbers_p2 += 1
    elif 400 <= num <= 599:
        numbers_p3 += 1
    elif 600 <= num <= 799:
        numbers_p4 += 1
    else:
        numbers_p5 += 1

p1 = numbers_p1 / count * 100
p2 = numbers_p2 / count * 100
p3 = numbers_p3 / count * 100
p4 = numbers_p4 / count * 100
p5 = numbers_p5 / count * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
