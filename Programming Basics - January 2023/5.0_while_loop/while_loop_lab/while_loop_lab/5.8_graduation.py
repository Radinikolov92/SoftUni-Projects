# read
name = input()
grade_average = 0
vault = 0
year = 0
exclusion = 0
# logic
while True:
    yearly_grade = float(input())
    if yearly_grade >= 4:
        vault += yearly_grade
        year += 1
    else:
        exclusion += 1

    if exclusion >= 2:
        print(f"{name} has been excluded at {year +1} grade")
        break

    if year >= 12:
        grade_average = vault / year
        print(f"{name} graduated. Average grade: {grade_average:.2f}")
        break
