import math
# read
lab_length_m = float(input())
lab_width_m = float(input())
corridor_width_cm = 100
work_station_width = 70
work_station_length = 120
work_station_unit = 1
door_loss = work_station_unit
teacher_place = work_station_unit * 2

# logic
lab_length_cm = lab_length_m * 100  # conversion
lab_width_cm = lab_width_m * 100  # conversion

# width calculation
lab_width_cm_with_loss = lab_width_cm - corridor_width_cm
work_stations_per_row = math.floor(lab_width_cm_with_loss / work_station_width)
work_station_width_remainder_cm = math.floor(lab_width_cm_with_loss % work_station_width)

# length calculation
rows = math.floor(lab_length_cm / work_station_length)
work_station_length_reminder_cm = math.floor(lab_length_cm % work_station_length)

# space calculation
work_stations_number = rows * work_stations_per_row
work_stations_with_loss_total = work_stations_number - (door_loss + teacher_place)

# print
print(int(work_stations_with_loss_total))
