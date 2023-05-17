# read
number_of_unsatisfactory_grades = int(input())
# logic
number_of_tasks = 0
fail_grades = 0
total_grades = 0
last_task = ""
while True:
    if fail_grades == number_of_unsatisfactory_grades:
        print(f"You need a break, {fail_grades} poor grades.")
        break
    else:
        name_of_task = str(input())

    if name_of_task == "Enough":
        average_grade = total_grades / number_of_tasks
        print(f"Average score: {average_grade:.2f}")
        print(f"Number of problems: {number_of_tasks}")
        print(f"Last problem: {last_task}")
        break
    else:
        grade = int(input())

    if grade <= 4:
        fail_grades += 1
        total_grades += grade
        number_of_tasks += 1
        last_task = name_of_task
    else:
        number_of_tasks += 1
        total_grades += grade
        last_task = name_of_task
