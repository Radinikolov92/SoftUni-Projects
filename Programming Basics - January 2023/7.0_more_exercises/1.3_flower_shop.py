# read
number_of_chrysanthemums = int(input())
number_of_roses = int(input())
number_of_tulips = int(input())
season = str(input())
holiday_check = str(input())

# read prices

price_for_preparation = 2
bouquet_total_count = number_of_chrysanthemums + number_of_roses + number_of_tulips
bouquet_price = 0
bouquet_price_with_discounts = 0

# logic
if holiday_check == "Y":
    chrysanthemum_spring_price = 2 + (15 * 2 / 100)
    chrysanthemum_summer_price = 2 + (15 * 2 / 100)
    chrysanthemum_autumn_price = 3.75 + (15 * 3.75 / 100)
    chrysanthemum_winter_price = 3.75 + (15 * 3.75 / 100)

    rose_spring_price = 4.10 + (15 * 4.10 / 100)
    rose_summer_price = 4.10 + (15 * 4.10 / 100)
    rose_autumn_price = 4.50 + (15 * 4.50 / 100)
    rose_winter_price = 4.50 + (15 * 4.50 / 100)

    tulip_spring_price = 2.50 + (15 * 2.50 / 100)
    tulip_summer_price = 2.50 + (15 * 2.50 / 100)
    tulip_autumn_price = 4.15 + (15 * 4.15 / 100)
    tulip_winter_price = 4.15 + (15 * 4.15 / 100)
# seasons logic
    if season == "Spring":
        price_chrysanthemum_flowers = number_of_chrysanthemums * chrysanthemum_spring_price
        price_rose_flowers = number_of_roses * rose_spring_price
        price_tulip_flowers = number_of_tulips * tulip_spring_price
        bouquet_price = price_chrysanthemum_flowers + price_rose_flowers + price_tulip_flowers
        if 7 <= number_of_tulips:
            bouquet_price_with_discounts = bouquet_price - (5 * bouquet_price / 100)
            final_price = bouquet_price_with_discounts + price_for_preparation
        else:
            final_price = bouquet_price_with_discounts + price_for_preparation
        if 20 <= bouquet_total_count:
            discount = bouquet_price_with_discounts - (20 * bouquet_price_with_discounts / 100)
            final_price = discount + price_for_preparation
        else:
            final_price = bouquet_price_with_discounts + price_for_preparation
        print(f"{final_price:.2f}")
    elif season == "Summer":
        price_chrysanthemum_flowers = number_of_chrysanthemums * chrysanthemum_summer_price
        price_rose_flowers = number_of_roses * rose_summer_price
        price_tulip_flowers = number_of_tulips * tulip_summer_price
        bouquet_price = price_chrysanthemum_flowers + price_rose_flowers + price_tulip_flowers
        bouquet_price_with_discounts = bouquet_price
        if 20 <= bouquet_total_count:
            bouquet_price_with_discounts = bouquet_price - (20 * bouquet_price / 100)
            final_price = bouquet_price_with_discounts + price_for_preparation
        else:
            bouquet_price_with_discounts = bouquet_price
            final_price = bouquet_price_with_discounts + price_for_preparation
        print(f"{final_price:.2f}")

    elif season == "Autumn":
        price_chrysanthemum_flowers = number_of_chrysanthemums * chrysanthemum_autumn_price
        price_rose_flowers = number_of_roses * rose_autumn_price
        price_tulip_flowers = number_of_tulips * tulip_autumn_price
        bouquet_price = price_chrysanthemum_flowers + price_rose_flowers + price_tulip_flowers
        bouquet_price_with_discounts = bouquet_price
        if 20 <= bouquet_total_count:
            bouquet_price_with_discounts = bouquet_price - (20 * bouquet_price / 100)
            final_price = bouquet_price_with_discounts + price_for_preparation
        else:
            bouquet_price_with_discounts = bouquet_price
            final_price = bouquet_price_with_discounts + price_for_preparation
        print(f"{final_price:.2f}")
    elif season == "Winter":
        price_chrysanthemum_flowers = number_of_chrysanthemums * chrysanthemum_winter_price
        price_rose_flowers = number_of_roses * rose_winter_price
        price_tulip_flowers = number_of_tulips * tulip_winter_price
        bouquet_price = price_chrysanthemum_flowers + price_rose_flowers + price_tulip_flowers
        bouquet_price_with_discounts = bouquet_price
        if 10 <= number_of_roses:
            bouquet_price_with_discounts = bouquet_price - (10 * bouquet_price / 100)
            final_price = bouquet_price_with_discounts + price_for_preparation
        else:
            final_price = bouquet_price_with_discounts + price_for_preparation
        if 20 <= bouquet_total_count:
            discount = bouquet_price_with_discounts - (20 * bouquet_price_with_discounts / 100)
            final_price = discount + price_for_preparation
        else:
            final_price = bouquet_price_with_discounts + price_for_preparation
        print(f"{final_price:.2f}")
    else:
        print("Invalid Season!")
elif holiday_check == "N":
    chrysanthemum_spring_price = 2
    chrysanthemum_summer_price = 2
    chrysanthemum_autumn_price = 3.75
    chrysanthemum_winter_price = 3.75

    rose_spring_price = 4.10
    rose_summer_price = 4.10
    rose_autumn_price = 4.50
    rose_winter_price = 4.50

    tulip_spring_price = 2.50
    tulip_summer_price = 2.50
    tulip_autumn_price = 4.15
    tulip_winter_price = 4.15
# seasons logic
    if season == "Spring":
        price_chrysanthemum_flowers = number_of_chrysanthemums * chrysanthemum_spring_price
        price_rose_flowers = number_of_roses * rose_spring_price
        price_tulip_flowers = number_of_tulips * tulip_spring_price
        bouquet_price = price_chrysanthemum_flowers + price_rose_flowers + price_tulip_flowers
        if 7 <= number_of_tulips:
            bouquet_price_with_discounts = bouquet_price - (5 * bouquet_price / 100)
            final_price = bouquet_price_with_discounts + price_for_preparation
        else:
            final_price = bouquet_price_with_discounts + price_for_preparation
        if 20 <= bouquet_total_count:
            discount = bouquet_price_with_discounts - (20 * bouquet_price_with_discounts / 100)
            final_price = discount + price_for_preparation
        else:
            final_price = bouquet_price_with_discounts + price_for_preparation
        print(f"{final_price:.2f}")
    elif season == "Summer":
        price_chrysanthemum_flowers = number_of_chrysanthemums * chrysanthemum_summer_price
        price_rose_flowers = number_of_roses * rose_summer_price
        price_tulip_flowers = number_of_tulips * tulip_summer_price
        bouquet_price = price_chrysanthemum_flowers + price_rose_flowers + price_tulip_flowers
        bouquet_price_with_discounts = bouquet_price
        if 20 <= bouquet_total_count:
            bouquet_price_with_discounts = bouquet_price - (20 * bouquet_price / 100)
            final_price = bouquet_price_with_discounts + price_for_preparation
        else:
            bouquet_price_with_discounts = bouquet_price
            final_price = bouquet_price_with_discounts + price_for_preparation
        print(f"{final_price:.2f}")

    elif season == "Autumn":
        price_chrysanthemum_flowers = number_of_chrysanthemums * chrysanthemum_autumn_price
        price_rose_flowers = number_of_roses * rose_autumn_price
        price_tulip_flowers = number_of_tulips * tulip_autumn_price
        bouquet_price = price_chrysanthemum_flowers + price_rose_flowers + price_tulip_flowers
        bouquet_price_with_discounts = bouquet_price
        if 20 <= bouquet_total_count:
            bouquet_price_with_discounts = bouquet_price - (20 * bouquet_price / 100)
            final_price = bouquet_price_with_discounts + price_for_preparation
        else:
            bouquet_price_with_discounts = bouquet_price
            final_price = bouquet_price_with_discounts + price_for_preparation
        print(f"{final_price:.2f}")
    elif season == "Winter":
        price_chrysanthemum_flowers = number_of_chrysanthemums * chrysanthemum_winter_price
        price_rose_flowers = number_of_roses * rose_winter_price
        price_tulip_flowers = number_of_tulips * tulip_winter_price
        bouquet_price = price_chrysanthemum_flowers + price_rose_flowers + price_tulip_flowers
        bouquet_price_with_discounts = bouquet_price
        if 10 <= number_of_roses:
            bouquet_price_with_discounts = bouquet_price - (10 * bouquet_price / 100)
            final_price = bouquet_price_with_discounts + price_for_preparation
        else:
            final_price = bouquet_price_with_discounts + price_for_preparation
        if 20 <= bouquet_total_count:
            discount = bouquet_price_with_discounts - (20 * bouquet_price_with_discounts / 100)
            final_price = discount + price_for_preparation
        else:
            final_price = bouquet_price_with_discounts + price_for_preparation
        print(f"{final_price:.2f}")
    else:
        print("Invalid Season!")
else:
    print("Invalid answer!")
