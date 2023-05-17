# read
number_of_groups = int(input())

# logic
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0

for people in range(1, number_of_groups + 1):
    number_of_people = int(input())
    if number_of_people <= 5:
        musala += number_of_people
    elif 6 <= number_of_people <= 12:
        monblan += number_of_people
    elif 13 <= number_of_people <= 25:
        kilimandjaro += number_of_people
    elif 26 <= number_of_people <= 40:
        k2 += number_of_people
    elif 41 <= number_of_people:
        everest += number_of_people
    else:
        print("There is no people for the group!")

total_number_of_people = musala + monblan + kilimandjaro + k2 + everest
musala_group = musala / total_number_of_people * 100
monblan_group = monblan / total_number_of_people * 100
kilimandjaro_group = kilimandjaro / total_number_of_people * 100
k2_group = k2 / total_number_of_people * 100
everest_group = everest / total_number_of_people * 100


# print
print(f"{musala_group:.2f}%")
print(f"{monblan_group:.2f}%")
print(f"{kilimandjaro_group:.2f}%")
print(f"{k2_group:.2f}%")
print(f"{everest_group:.2f}%")
