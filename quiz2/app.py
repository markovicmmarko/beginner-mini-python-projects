import csv

with open("quiz2/zzz.csv", "r") as file:
    csvfile = list(csv.reader(file))

print("Welcome to ***quiz game***")


play = input("Are you ready to play (y/n)? ").lower()

if play != "y":
    print("Have a nice day...")
    quit()
else:
    score = 0
    for line in csvfile:
        answer = input(line[0]).lower()
        if answer == line[1]:
            score += 1
            print("Correct!")
        else:
            print("Incorrect...")
    
    print("You finished this quiz game....")
    score = (score / len(csvfile)) * 100
    print(f"You answered correctly on {score:.1f}% of the questions!")
    


