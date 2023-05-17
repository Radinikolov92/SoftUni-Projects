# read
length_cm = int(input())
wight_cm = int(input())
height_cm = int(input())
percent = float(input())
conversion = float(0.001)

#logic
raw_volume = int(length_cm * wight_cm * height_cm)
volume_in_liters = float(raw_volume * conversion)
occupied_area = float(percent / 100)

needed_liters = float(volume_in_liters * (1 - occupied_area))

# print
print(float(needed_liters))
