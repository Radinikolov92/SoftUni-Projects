# read prices
gasoline_for_liter = 2.22
diesel_for_liter = 2.33
gas_for_liter = 0.93
# discounts
gasoline_discount_for_liter = 0.18
diesel_discount_for_liter = 0.12
gas_discount_for_liter = 0.08
conditional_percent_discount_1 = 8
conditional_percent_discount_2 = 10

# read
fuel_type = str(input())
fuel_quantity = float(input())
ownership_of_club_card = str(input())

# logic

gasoline_sum = fuel_quantity * gasoline_for_liter
diesel_sum = fuel_quantity * diesel_for_liter
gas_sum = fuel_quantity * gas_for_liter


# Gasoline Calculation

if fuel_type == "Gasoline":
    total_gasoline = gasoline_sum

    if ownership_of_club_card == "Yes":
        total_gasoline_with_discount = total_gasoline - (fuel_quantity * gasoline_discount_for_liter)
        if 20 <= fuel_quantity <= 25:
            final_gasoline_price = total_gasoline_with_discount - (8 * total_gasoline_with_discount / 100)
            print(f"{final_gasoline_price:.2f} lv.")
        elif 25 < fuel_quantity:
            final_gasoline_price = total_gasoline_with_discount - (10 * total_gasoline_with_discount / 100)
            print(f"{final_gasoline_price:.2f} lv.")
        else:
            print(f"{total_gasoline_with_discount:.2f} lv.")

    elif ownership_of_club_card == "No":
        if 20 <= fuel_quantity <= 25:
            final_gasoline_price = gasoline_sum - (8 * gasoline_sum / 100)
            print(f"{final_gasoline_price:.2f} lv.")
        elif 25 < fuel_quantity:
            final_gasoline_price = gasoline_sum - (10 * gasoline_sum / 100)
            print(f"{final_gasoline_price:.2f} lv.")
        else:
            print(f"{gasoline_sum:.2f} lv.")
    else:
        print("Invalid parameter!")

# Diesel calculation

elif fuel_type == "Diesel":
    total_diesel = diesel_sum

    if ownership_of_club_card == "Yes":
        total_diesel_with_discount = total_diesel - (fuel_quantity * diesel_discount_for_liter)
        if 20 <= fuel_quantity <= 25:
            final_diesel_price = total_diesel_with_discount - (8 * total_diesel_with_discount / 100)
            print(f"{final_diesel_price:.2f} lv.")
        elif 25 < fuel_quantity:
            final_diesel_price = total_diesel_with_discount - (10 * total_diesel_with_discount / 100)
            print(f"{final_diesel_price:.2f} lv.")
        else:
            print(f"{total_diesel_with_discount:.2f} lv.")

    elif ownership_of_club_card == "No":
        if 20 <= fuel_quantity <= 25:
            final_diesel_price = diesel_sum - (8 * diesel_sum / 100)
            print(f"{final_diesel_price:.2f} lv.")
        elif 25 < fuel_quantity:
            final_diesel_price = diesel_sum - (10 * diesel_sum / 100)
            print(f"{final_diesel_price:.2f} lv.")
        else:
            print(f"{diesel_sum:.2f} lv.")
    else:
        print("Invalid parameter!")

# Gas Calculation

elif fuel_type == "Gas":
    total_gas = gas_sum

    if ownership_of_club_card == "Yes":
        total_gas_with_discount = total_gas - (fuel_quantity * gas_discount_for_liter)
        if 20 <= fuel_quantity <= 25:
            final_gas_price = total_gas_with_discount - (8 * total_gas_with_discount / 100)
            print(f"{final_gas_price:.2f} lv.")
        elif 25 < fuel_quantity:
            final_gas_price = total_gas_with_discount - (10 * total_gas_with_discount / 100)
            print(f"{final_gas_price:.2f} lv.")
        else:
            print(f"{total_gas_with_discount:.2f} lv.")

    elif ownership_of_club_card == "No":
        if 20 <= fuel_quantity <= 25:
            final_gas_price = gas_sum - (8 * gas_sum / 100)
            print(f"{final_gas_price:.2f} lv.")
        elif 25 < fuel_quantity:
            final_gas_price = gas_sum - (10 * gas_sum / 100)
            print(f"{final_gas_price:.2f} lv.")
        else:
            print(f"{gas_sum:.2f} lv.")
    else:
        print("Invalid parameter!")
else:
    print("Invalid Fuel!")
