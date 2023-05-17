# read
cake_with = int(input())
cake_length = int(input())

# calculation
total_cake = cake_with * cake_length

# logic
while total_cake > 0:
    command = input()
    if command != "STOP":
        total_cake = total_cake - int(command)
        continue
    else:
        pieces_left = total_cake
        print(f"{pieces_left} pieces are left.")
        break

else:
    pieces_needed = abs(total_cake)
    print(f"No more cake left! You need {pieces_needed} pieces more.")
