import random

# Print starting title
print("Blackjack Game Started")

# Variables
player_card = []
dealer_card = []
temp_player = 0
temp_dealer = 0
player_turns = 0
dealer_turns = 0

# Options
def Options():
    print("""
Options:
    1. Hit
    2. Pass
    3. Quit
          """)

# Hit
def Hit():
    card = random.randint(1, 10)
    player_card.append(card)
    print(f"You drew: {card}")
    print(f"Your cards: {player_card} Total: {sum(player_card)}")

# Pass
def Pass():
    print("You passed")
    print(f"Your cards: {player_card} Total: {sum(player_card)}")

# Random dealer choice
def Dealer_choice():
    card = random.randint(1, 10)
    dealer_card.append(card)
    print(f"Dealer drew: {card}")

# Sum up
def Sum():
    global temp_player, temp_dealer
    temp_player = sum(player_card)
    temp_dealer = sum(dealer_card)

# Game Process
while temp_player < 21 and temp_dealer < 21 and player_turns < 4 and dealer_turns < 4:
    Options()
    choice = int(input("Choose: "))
    if choice == 1:
        Hit()
        player_turns += 1
    elif choice == 2:
        Pass()
        dealer_turns += 1
        Dealer_choice()
    else:
        break
    Sum()

# Game Over
print("\nGame Over")
print(f"Your final cards: {player_card} Total: {temp_player}")
print(f"Dealer's final cards: {dealer_card} Total: {temp_dealer}")

# Determine the winner
if temp_player > 21:
    print("You busted! Dealer wins.")
elif temp_dealer > 21:
    print("Dealer busted! You win.")
elif temp_player == temp_dealer:
    print("It's a tie!")
elif temp_player > temp_dealer:
    print("You win!")
else:
    print("Dealer wins!")
