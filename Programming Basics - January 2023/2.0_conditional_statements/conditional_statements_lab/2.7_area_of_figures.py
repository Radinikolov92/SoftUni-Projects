# read
from math import pi
figure = input()

# logic
if figure == "square":
    number_a = float(input())
    area = (float(number_a)) * (float(number_a))
    print(f"{area:.3f}")
elif figure == "rectangle":
    number_a = float(input())
    number_b = float(input())
    area = (float(number_a)) * (float(number_b))
    print(f"{area:.3f}")
elif figure == "circle":
    number_a = float(input())
    radius = (float(pi)) * (float(number_a))
    area = (float(pi)) * (float(number_a)) * (float(number_a))
    print(f"{area:.3f}")
elif figure == "triangle":
    number_a = float(input())
    number_b = float(input())
    area = (float(number_a)) * (float(number_b)) / 2
    print(f"{area:.3f}")
