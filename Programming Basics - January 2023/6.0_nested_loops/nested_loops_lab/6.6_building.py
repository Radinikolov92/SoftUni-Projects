# read
number_of_floors = int(input())
number_of_rooms_per_floor = int(input())

for floors in range(number_of_floors, 0, -1):
    if floors == number_of_floors:
        for rooms in range(0, number_of_rooms_per_floor):
            print(f"L{floors}{rooms} ", end="")
    elif floors % 2 == 0:
        for rooms in range(0, number_of_rooms_per_floor):
            print(f"O{floors}{rooms} ", end="")
    elif floors % 2 != 0:
        for rooms in range(0, number_of_rooms_per_floor):
            print(f"A{floors}{rooms} ", end="")
    print()
