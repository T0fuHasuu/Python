# Random module
import random

# Declare variables
correct = 0
bottle = [0,0,0]
answer = [0,0,0]

# Get The Random number store in array
for i in range(len(bottle)):
    bottle[i] = random.randint(1,6)
    i = i + 1

# Input 3 numbers and store it into array while if not 1-6 will make user enter again
for i in range(len(bottle)):
    while True:
        guess = int(input(f"Input guess {i+1}: "))
        if 1 <= guess <= 6:
            answer[i] = guess
            break
        else:
            print("Number 1-6 : ")

# Checking if the number correct each array index
for i in range(len(bottle)) :
    for y in range(len(bottle)) :
        if (answer[i] == bottle[y]) :
            correct += 1
        y += 1
    i += 1

# Conditioning the award
if (correct==3) :
    print("You Won!!")
elif (correct == 2 ) :
    print("Nice Job, You Won 2 slots.")
elif (correct == 1) :
    print("Good I guess, you got 1 correct")
else :
    print("You lose . . .")