import random

max_num = input("Choose a top range number: ")

if max_num.isdigit():
    max_num = int(max_num)
    if max_num <= 0:
        print("Please enter a number larger than 0...")
        quit()
else:
    print("You must enter a number!")
    quit()

ran_num = random.randint(0, max_num)
tries = 0

while True:
    tries += 1
    user_num = input("Choose your number: ")
    if user_num.isdigit():
        user_num = int(user_num)
        if user_num <= 0:
            print("Please enter a number larger than 0...")
            quit()
    else:
        print("You must enter a number!")
        continue

    if user_num == ran_num:
        print("You guessed right!")
        break
    elif user_num > ran_num:
        print("You aimed high...")
    else:
        print("You aimed low....")

print(f"You've got it in {tries} tries.")