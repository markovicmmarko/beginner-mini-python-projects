import turtle, random


display = turtle.Screen()
display.setup(800, 600)
display.bgcolor("gray")



colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_poss = [240, 150, 60, -30, -120, -210]
turtles = []

for i in range(len(colors)):
    kornjaca = turtle.Turtle(shape="turtle")
    kornjaca.color(colors[i])
    kornjaca.penup()
    kornjaca.goto(-380, y_poss[i])
    turtles.append(kornjaca)

bet = display.textinput("Place your bet!", "Choose your color: ")

finish = 350
race = True

if bet in colors:
    while race:
        for t in turtles:
            if t.xcor() >= finish:
                race = False
                if bet == t.pencolor():
                    print(f"You won! Your {t.pencolor()} color turtle arrived first!")
                else:
                    print(f"You lost! {t.pencolor()} won...")
            t.forward(random.randint(1,30))
else:
    display.bye()
    print(f"Choose between existing colors! ({", ".join(colors)})")
 






display.exitonclick()









