# read
name_of_actor = str(input())
academy_points = float(input())
jury = int(input())

# logic
target = 1250.5
bonus_points = 0
grade = academy_points
for character in range(1, jury + 1):
    name_of_judge = str(input())
    judge_points = float(input())
    bonus_points = len(name_of_judge)
    grade += (bonus_points * judge_points) / 2
    if grade >= target:
        break
    else:
        continue
if grade < target:
    diff = target - grade
    print(f"Sorry, {name_of_actor} you need {abs(diff):.1f} more!")
else:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {grade:.1f}!")
