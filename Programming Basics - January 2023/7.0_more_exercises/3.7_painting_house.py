# read
house_height = float(input())
length_side_wall = float(input())
triangle_roof_height = float(input())

# calculations
front_wall_door_area = 1.2 * 2
window = 1.5 * 1.5
side_wall_windows_area = window * 2
green_paint_liter = 3.4
red_paint_liter = 4.3

# logic
side_walls = (house_height * length_side_wall) * 2
area_side_walls = side_walls - side_wall_windows_area

front_and_back_walls = (house_height * house_height) * 2
area_front_walls = front_and_back_walls - front_wall_door_area

roof_rectangle = house_height * length_side_wall
roof_rectangle_area = roof_rectangle * 2
roof_triangle = house_height * triangle_roof_height / 2
roof_triangle_area = roof_triangle * 2

roof_total_area = roof_rectangle_area + roof_triangle_area
walls_total_area = area_side_walls + area_front_walls

green_paint_needed = walls_total_area / green_paint_liter
red_paint_needed = roof_total_area / red_paint_liter

# print
print(f"{green_paint_needed:.2f}")
print(f"{red_paint_needed:.2f}")
