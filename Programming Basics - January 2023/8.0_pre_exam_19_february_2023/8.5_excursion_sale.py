# read
sea_packets = int(input())
mountain_packets = int(input())

# prices
sea_price = 680
mountain_price = 499
# logic
packet_type = ""
sea_income = 0
mountain_income = 0
while packet_type != "Stop":
    if sea_packets == 0 and mountain_packets == 0:
        break
    packet_type = str(input())
    if packet_type == "sea":
        if sea_packets == 0:
            continue
        else:
            sea_income += sea_price
            sea_packets -= 1
    elif packet_type == "mountain":
        if mountain_packets == 0:
            continue
        else:
            mountain_income += mountain_price
            mountain_packets -= 1

total_income = sea_income + mountain_income

# print
if sea_packets == 0 and mountain_packets == 0:
    print(f" Good job! Everything is sold.")
    print(f"Profit: {total_income} leva.")
else:
    print(f"Profit: {total_income} leva.")
