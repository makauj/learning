#simple quiz game to learn codeing in python

print("welcome to my computer quiz")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    exit()

print("Let's begin :")
score = 0
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphical processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ").upper()
if answer == "POWER SUPPLY UNIT":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {score} questions correct")