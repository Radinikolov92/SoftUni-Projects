# read
off_days = int(input())

# logic

full_year = 365
play_time_work = 63
play_time_off = 127
play_time_cap_for_a_year = 30000

work_days = full_year - off_days
play_time_work_total = work_days * play_time_work
play_time_off_total = off_days * play_time_off
total_play_time = play_time_work_total + play_time_off_total
difference_in_play_time = play_time_cap_for_a_year - total_play_time

if total_play_time > play_time_cap_for_a_year:
    overplay = total_play_time - play_time_cap_for_a_year
    # time calculation
    hours = overplay // 60
    minutes = overplay % 60
    print(f"Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")

else:
    # time calculation
    hours = difference_in_play_time // 60
    minutes = difference_in_play_time % 60
    print(f"Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
