name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. "
    "Which way would you like to go? ").lower()

if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim across? Type (walk) to walk around and (swim) to swim "
        "across: ").lower()

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("It was not a valid option so you lost the game!")

elif answer == "right":
    answer = input("You came to a bridge, it looked wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "cross":
        answer = input("You crossed the bridge and met a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("You talked to the stranger and they give you gold. You won!")
        elif answer == "no":
            print("You ignored the stranger and they are offended and you lost!")
        else:
            print("It was not a valid option so you lost the game!")

    elif answer == "back":
        print("You went back to the main road so you lost! ")
    else:
        print("It was not a valid option so you lost the game!")

else:
    print("It was not a valid option so you lost the game!")

print(f"Thanks {name} for playing with us :)")
