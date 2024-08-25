import random

print("Game Started") 

player_card = [0,0,0,0]
dealer_card = [0,0,0,0]

def card(self) :
    self = random.randint(1,10)

user_hit = input("Want Another Card ? ")
if (user_hit.lower() == "h") :
    card(player_card[0])
else : 
    print("Pass")

print(player_card[0])
