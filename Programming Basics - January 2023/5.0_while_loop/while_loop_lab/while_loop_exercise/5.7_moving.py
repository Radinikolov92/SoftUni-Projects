# read
W_area = int(input())
L_area = int(input())
H_area = int(input())

# calculation
total_area = W_area * L_area * H_area

# logic
while total_area > 0:
    command = input()
    if command != "Done":
        total_area = total_area - int(command)
        continue
    else:
        area_left = total_area
        print(f"{area_left} Cubic meters left.")
        break

else:
    area_needed = abs(total_area)
    print(f"No more free space! You need {area_needed} Cubic meters more.")
