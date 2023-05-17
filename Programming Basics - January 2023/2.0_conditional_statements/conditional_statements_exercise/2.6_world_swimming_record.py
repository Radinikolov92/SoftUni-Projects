import math
# read
world_record = float(input())
distance_in_m = float(input())
time_for_1m = float(input())
water_resistance = (math.floor(distance_in_m / 15) * 12.5)

# logic
I_time = distance_in_m * time_for_1m
I_real_time = I_time + water_resistance
if I_real_time >= world_record:
    time_deficit = I_real_time - world_record
    print(f"No, he failed! He was {time_deficit:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {I_real_time:.2f} seconds.")
