# read
kilometers = int(input())
time_of_day = input()

# prices
taxi_start_price = 0.70
taxi_day_price_km = 0.79
taxi_night_price_km = 0.90
bus_price = 0.09
train_price = 0.06

# logic
if kilometers < 20:
    taxi_price_per_km = 0
    if time_of_day == "day":
        taxi_price_per_km = taxi_day_price_km
        trip_price = (taxi_start_price + (kilometers * taxi_price_per_km))
        print(f"{trip_price:.2f}")
    elif time_of_day == "night":
        taxi_price_per_km = taxi_night_price_km
        trip_price = (taxi_start_price + (kilometers * taxi_price_per_km))
        print(f"{trip_price:.2f}")
    else:
        print("incorrect parameters.")
elif 20 <= kilometers < 100:
    trip_price = (kilometers * bus_price)
    print(f"{trip_price:.2f}")
elif 100 <= kilometers:
    trip_price = (kilometers * train_price)
    print(f"{trip_price:.2f}")
