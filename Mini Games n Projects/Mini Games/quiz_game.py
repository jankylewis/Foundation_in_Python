print("Welcome to my computer quiz!")

# ask user to typing sth in the console
playing = input("Do you want to play?\nYes to play, No to quit the game\n")

if playing.upper() != "YES":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for?\n").lower()

if answer == "central processing unit":
    print("You were correct!")
    score += 1
else:
    print("You were incorrect!")

answer = input("What does GPU stand for?\n").lower()

if answer == "graphics processing unit":
    print("You were correct!")
    score += 1
else:
    print("You were incorrect!")

answer = input("What does RAM stand for?\n").lower()

if answer == "random access memory":
    print("You were correct!")
    score += 1
else:
    print("You were incorrect!")

answer = input("What does PSU stand for?\n").lower()

if answer == "power supply":
    print("You were correct!")
    score += 1
else:
    print("You were incorrect!")

print(f"You got {str(score)} questions out of 4 correct!")
print(f"You got {str((score / 4) * 100)}% percentage of correct questions!")
