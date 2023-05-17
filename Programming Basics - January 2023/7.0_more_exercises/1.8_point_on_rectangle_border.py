# read
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())


# logic
point = "N/A"
if x1 <= x <= x2 and y1 <= y <= y2:
    point = "Inside / Outside"
    if x == x1:
        point = "Border"
    elif x == x2:
        point = "Border"
    elif y == y1:
        point = "Border"
    elif y == y2:
        point = "Border"
    else:
        point = "Inside / Outside"
else:
    point = "Inside / Outside"
# print
print(point)
