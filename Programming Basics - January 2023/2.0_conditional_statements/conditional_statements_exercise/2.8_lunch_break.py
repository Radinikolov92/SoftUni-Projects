import math
# read
name_of_serial = str(input())
episode_time = int(input())
break_time = int(input())

# additional info
lunch_time = break_time / 8
relax_time = break_time / 4
occupied_time = lunch_time + relax_time

# logic
real_time = break_time - occupied_time

if episode_time <= real_time:
    excess = math.ceil(real_time - episode_time)
    print(f"You have enough time to watch {name_of_serial} and left with {excess:} minutes free time.")
else:
    deficit = math.ceil(episode_time - real_time)
    print(f"You don't have enough time to watch {name_of_serial}, you need {deficit:} more minutes.")
