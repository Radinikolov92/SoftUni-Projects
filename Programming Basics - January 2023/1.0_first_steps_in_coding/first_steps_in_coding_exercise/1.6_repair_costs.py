# read requirements
cover_nylon_needed = float(input())
base_paint_needed = float(input())
paint_reducer_needed = float(input())
work_hours_needed = int(input())
garbage_bags_needed = int(1)
extra_nylon = int(2)

# read prices
price_for_cover_nylon_for_1_cubic_meter = float(1.50)
price_for_base_paint_for_1_liter = float(14.50)
price_for_paint_reducer_for_1_liter = float(5.00)
paint_extra = (base_paint_needed * 10 / 100)
price_for_garbage_bags = float(0.40)
price_for_work_in_percent = float(30 / 100)

# logic
total_sum_for_nylon = float((cover_nylon_needed + extra_nylon) * price_for_cover_nylon_for_1_cubic_meter)
total_sum_for_paint = float((base_paint_needed + paint_extra) * price_for_base_paint_for_1_liter)
total_sum_for_reducer = float(paint_reducer_needed * price_for_paint_reducer_for_1_liter)
total_sum_for_garbage_bags = float(garbage_bags_needed * price_for_garbage_bags)

# overall calculations
total_sum_for_materials = float(total_sum_for_nylon + total_sum_for_paint +
                                total_sum_for_reducer + total_sum_for_garbage_bags)

overall_price_for_work = float((total_sum_for_materials * price_for_work_in_percent) * work_hours_needed)

overall_costs = float(total_sum_for_materials + overall_price_for_work)

# print
print(float(overall_costs))
