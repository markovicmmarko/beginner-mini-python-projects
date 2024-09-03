import random

with open("words.txt","r") as file:
    words = file.read().split("\n")

chosen_word = random.choice(words)
display = ""
for i in range(len(chosen_word)):
    display += "_ "
print(display)


lives = 6
correct_letters = []

while lives > 0:
    correct = False
    guess = input("Guess a letter: ").lower()
    output = ""
    
    for letter in chosen_word:
        if letter == guess:
            output += letter
            correct_letters.append(letter)
            correct = True
        elif letter in correct_letters:
            output += letter
        else:
            output += "_ "
    
    if not correct:
        lives -= 1
    print(output)
    print(f"================ Lives left: {lives} ===================")
    
    if lives == 0:
        print(f"the word was {chosen_word.upper()}")
        print("****************** YOU LOSE ******************")
    
    if "_ " not in output:
        print("*************** YOU WIN ********************")
        break
