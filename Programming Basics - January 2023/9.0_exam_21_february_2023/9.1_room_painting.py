# read
import math
paint_buckets = int(input())
wallpaper_rolls = int(input())
price_for_a_pair_of_gloves = float(input())
price_for_brush = float(input())
price_for_a_paint_bucket = 21.50
price_for_a_roll_of_wallpaper = 5.20

# calculation
gloves_needed = math.ceil(35 * wallpaper_rolls / 100)
brushes_needed = math.floor(48 * paint_buckets / 100)

# logic
paint_total = paint_buckets * price_for_a_paint_bucket
wallpaper_total = wallpaper_rolls * price_for_a_roll_of_wallpaper
gloves_total = gloves_needed * price_for_a_pair_of_gloves
brushes_total = brushes_needed * price_for_brush
total = paint_total + wallpaper_total + gloves_total + brushes_total
overall_price = total / 15

# print
print(f"This delivery will cost {overall_price:.2f} lv.")
