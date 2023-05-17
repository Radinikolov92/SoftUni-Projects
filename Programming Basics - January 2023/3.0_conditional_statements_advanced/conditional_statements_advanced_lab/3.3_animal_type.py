# read
animal = str(input())

# logic
animal_type = "N/A"
if animal == "dog":
    animal_type = "mammal"
elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
    animal_type = "reptile"
else:
    animal_type = "unknown"

# print
print(animal_type)
