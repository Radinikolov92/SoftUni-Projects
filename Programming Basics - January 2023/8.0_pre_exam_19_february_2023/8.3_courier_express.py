# read
weight = float(input())
mode = str(input())
distance = int(input())

# prices
s_under_1 = 0.03
s_1_9 = 0.05
s_10_39 = 0.10
s_40_89 = 0.15
s_90_149 = 0.20

e_under_1 = weight * (80 / 100 * s_under_1)
e_1_9 = weight * (40 / 100 * s_1_9)
e_10_39 = weight * (5 / 100 * s_10_39)
e_40_89 = weight * (2 / 100 * s_40_89)
e_90_149 = weight * (1 / 100 * s_90_149)

# logic
if mode == "standard":
    price = 0
    if 0 < weight < 1:
        price = distance * s_under_1
        print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {price:.2f} lv.")
    elif 1 <= weight < 10:
        price = distance * s_1_9
        print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {price:.2f} lv.")
    elif 10 <= weight < 40:
        price = distance * s_10_39
        print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {price:.2f} lv.")
    elif 40 <= weight < 90:
        price = distance * s_40_89
        print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {price:.2f} lv.")
    elif 90 <= weight < 150:
        price = distance * s_90_149
        print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {price:.2f} lv.")
    else:
        print("Invalid package!")
elif mode == "express":
    price = 0
    if 0 < weight < 1:
        over_tax = distance * e_under_1
        price = (distance * s_under_1) + over_tax
        print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {price:.2f} lv.")
    elif 1 <= weight < 10:
        over_tax = distance * e_1_9
        price = (distance * s_1_9) + over_tax
        print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {price:.2f} lv.")
    elif 10 <= weight < 40:
        over_tax = distance * e_10_39
        price = (distance * s_10_39) + over_tax
        print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {price:.2f} lv.")
    elif 40 <= weight < 90:
        over_tax = distance * e_40_89
        price = (distance * s_40_89) + over_tax
        print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {price:.2f} lv.")
    elif 90 <= weight < 150:
        over_tax = distance * e_90_149
        price = (distance * s_90_149) + over_tax
        print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {price:.2f} lv.")
    else:
        print("Invalid package!")
else:
    print("Invalid type of service! Please pick between: {standard} and {express}.")
