# read
word = str(input())

# logic

a = 1
e = 2
i = 3
o = 4
u = 5
total = 0

for ch in word:
    if ch == "a":
        total += a
    if ch == "e":
        total += e
    if ch == "i":
        total += i
    if ch == "o":
        total += o
    if ch == "u":
        total += u

print(total)
