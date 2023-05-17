# read
days = int(input())

# logic
Liters = 0
Degrees = 0
for period in range(1, days + 1):
    liters = float(input())
    if liters <= 0:
        continue
    degrees = float(input())

    degrees_for_liter_calc = liters * degrees
    Liters += liters
    Degrees += degrees_for_liter_calc
average_degrees = Degrees / Liters
if 0 < average_degrees < 38:
    print(f"Liter: {Liters:.2f}")
    print(f"Degrees: {average_degrees:.2f}")
    print(f"Not good, you should baking!")
elif 38 <= average_degrees < 42:
    print(f"Liter: {Liters:.2f}")
    print(f"Degrees: {average_degrees:.2f}")
    print(f"Super!")
elif 42 <= average_degrees:
    print(f"Liter: {Liters:.2f}")
    print(f"Degrees: {average_degrees:.2f}")
    print(f"Dilution with distilled water!")
else:
    print("Did you brew anything?")
