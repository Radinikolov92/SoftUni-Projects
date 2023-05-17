import math
# read
magnolia_quantity = int(input())
hyacinth_quantity = int(input())
rose_quantity = int(input())
cactus_quantity = int(input())
price_of_gift = float(input())

# prices
magnolia = 3.25
hyacinth = 4
rose = 3.50
cactus = 8

# logic
magnolia_total = magnolia_quantity * magnolia
hyacinth_total = hyacinth_quantity * hyacinth
rose_total = rose_quantity * rose
cactus_total = cactus_quantity * cactus
net_sum = magnolia_total + hyacinth_total + rose_total + cactus_total
taxes = 5 * net_sum / 100
gross_sum = net_sum - taxes

if gross_sum >= price_of_gift:
    excess = gross_sum - price_of_gift
    print(f"She is left with {math.floor(excess)} leva.")
else:
    deficit = price_of_gift - gross_sum
    print(f"She will have to borrow {math.ceil(deficit)} leva.")
