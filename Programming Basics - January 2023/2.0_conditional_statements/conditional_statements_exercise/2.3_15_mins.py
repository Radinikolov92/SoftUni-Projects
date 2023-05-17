# read
hours = int(input())
minutes = int(input()) + 15

# logic
if minutes >= 60:
    hours += 1
    minutes -= 60

if hours > 23:
    hours -= 24

# print
print(f"{hours}:{minutes:02d}")
