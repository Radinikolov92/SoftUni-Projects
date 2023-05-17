# read
number_of_pages = int(input())
pages_for_one_hour = int(input())
deadline = int(input())

# logic
hours_needed_total = number_of_pages / pages_for_one_hour
hours_needed_per_day = hours_needed_total / deadline


# print
print(int(hours_needed_per_day))
