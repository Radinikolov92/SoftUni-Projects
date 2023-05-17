import math
# read
vineyard_area = int(input())
grapes_quantity = float(input())
needed_wine_liters = int(input())
worker = (int(input()))

# logic
production = vineyard_area * grapes_quantity
wine_production_liter = 2.5
wine_resource = (40 * production / 100)
wine_production_capacity = wine_resource / wine_production_liter

if wine_production_capacity < needed_wine_liters:
    deficit = needed_wine_liters - wine_production_capacity
    print(f"It will be a tough winter! More {math.floor(deficit)} liters wine needed.")
else:
    excess = wine_production_capacity - needed_wine_liters
    worker_bonus = excess / worker
    print(f"Good harvest this year! Total wine: {math.floor(wine_production_capacity)} liters.")
    print(f"{math.ceil(excess)} liters left -> {math.ceil(worker_bonus)} liters per person.")
