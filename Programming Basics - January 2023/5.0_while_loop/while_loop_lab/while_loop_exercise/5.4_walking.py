# read
goal = 10000
steps_done = 0
# logic
command = input()
while True:
    if command == "Going home":
        steps_till_home = int(input())
        steps_done += steps_till_home
        if steps_done < goal:
            deficit = goal - steps_done
            print(f"{deficit} more steps to reach goal.")
            break
        else:
            excess = abs(goal - steps_done)
            print("Goal reached! Good job!")
            print(f"{excess} steps over the goal!")
            break
    else:
        steps_done += int(command)
        if steps_done >= goal:
            excess = abs(goal - steps_done)
            print("Goal reached! Good job!")
            print(f"{excess} steps over the goal!")
            break
        else:
            command = input()
            continue
