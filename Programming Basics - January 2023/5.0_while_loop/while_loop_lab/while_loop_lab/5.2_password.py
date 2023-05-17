# read
username = str(input())
true_password = (input())
# logic
while True:
    password_prompt = input()
    if password_prompt != true_password:
        continue
    else:
        print(f"Welcome {username}!")
        break
