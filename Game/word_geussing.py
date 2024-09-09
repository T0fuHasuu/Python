import random

# Array List
fruits = ["apple", "banana", "pineapple", "orange", "dragonfruit", "kiwi"]

# Menu as Function to Call it later on
def Menu() :
    print("""
        Fruit List :
        
        1. Apple
        2. Banana
        3. Pineapple
        4. Orange
        5. Dragonfruit
        6. Kiwi
    """)
    
# To loop the game
while (True) :

    # Randomize the index
    fruit_picking = fruits[random.randint(0,int(len(fruits) - 1))]

    # Callout The Menu
    Menu() 

    # Make sure the input number is between 1-6
    while (True) :
        answer = input("Choose A Number : ")
        if (int(answer) >= 1 and int(answer) <= 6) :
            break
        else :
            print("Choose Again!!")

    # Checking the answer
    if (fruit_picking == str(fruits[int(answer)-1])) :
        print(f"\n{fruit_picking} Is The Answer !!!")

        break
    else :
        print("Wrong, Try Again")