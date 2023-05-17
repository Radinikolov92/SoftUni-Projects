# read
fat_percent = int(input())
protein_percent = int(input())
carbohydrates_percent = int(input())
total_calories = int(input())
water_percent = int(input())

# calories
gram_of_fats = 9
gram_of_proteins = 4
gram_of_carbohydrates = 4

# logic
fat_conv = fat_percent / 100 * total_calories
total_fat = fat_conv / gram_of_fats
protein_conv = protein_percent / 100 * total_calories
total_protein = protein_conv / gram_of_proteins
carbohydrates_conv = carbohydrates_percent / 100 * total_calories
total_carbohydrate = carbohydrates_conv / gram_of_carbohydrates
food_weight = total_fat + total_protein + total_carbohydrate
gram_of_calories = total_calories / food_weight
water = water_percent / 100 * gram_of_calories
calories = gram_of_calories - water

# print
print(f"{calories:.4f}")
