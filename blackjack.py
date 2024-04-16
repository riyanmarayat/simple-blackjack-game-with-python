############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
import random

import art

def play_game_blackjack():
    """Player input apakah dia ingin bermain blackjack atau tidak"""
    player_input = input("Do you want to play a game of Blackjack? type 'y' or 'n': ")
    if player_input.lower() == "n":
        return False
    elif player_input.lower() == "y":
        return True
    else:
        print("Your input is invalid, please reinput!")
        play_game_blackjack()

def cek_same_card(player1_card, player2_card):
    """Mengecek apakah kartu P1 sama dengan P2"""
    num_p1_card = len(player1_card)
    num_p2_card = len(player2_card)
    for i in range(num_p1_card):
        if i > 0:
            for j in range(i+1, num_p1_card):
                if player1_card[i] == player1_card[j]:
                    return True
        for k in range(num_p2_card):
            if player1_card[i] == player2_card[k]:
                return True
    return False

def cek_score(player_cards):
    """Mengecek score dari kartu-kartu player"""
    num_of_card = len(player_cards)
    player_score = 0
    for i in range(num_of_card):
        player_score += int(player_cards[i].split(",")[1])
    while player_score > 21:
        if "A\u2663,11" in player_cards:
            index_ace = player_cards.index("A\u2663,11")
            player_cards[index_ace] = "A\u2663,1"
            player_score -= 10
        elif "A\u2665,11" in player_cards:
            index_ace = player_cards.index("A\u2665,11")
            player_cards[index_ace] = "A\u2665,1"
            player_score -= 10
        elif "A\u2666,11" in player_cards:
            index_ace = player_cards.index("A\u2666,11")
            player_cards[index_ace] = "A\u2666,1"
            player_score -= 10
        elif "A\u2660,11" in player_cards:
            index_ace = player_cards.index("A\u2660,11")
            player_cards[index_ace] = "A\u2660,1"
            player_score -= 10
        else:
            return player_score
    return player_score

def print_player_cards(player_card):
    num_of_card = len(player_card)
    output_player_cards = player_card[0].split(",")[0]
    for i in range(1, num_of_card):
        output_player_cards += f",{player_card[i].split(',')[0]}"
    return output_player_cards
pool_of_card = [
    "A\u2663,11", "2\u2663,2", "3\u2663,3", "4\u2663,4", "5\u2663,5", "6\u2663,6", "7\u2663,7", "8\u2663,8", "9\u2663,9", "10\u2663,10", "J\u2663,10", "Q\u2663,10", "K\u2663,10",
    "A\u2665,11", "2\u2665,2", "3\u2665,3", "4\u2665,4", "5\u2665,5", "6\u2665,6", "7\u2665,7", "8\u2665,8", "9\u2665,9", "10\u2665,10", "J\u2665,10", "Q\u2665,10", "K\u2665,10",
    "A\u2666,11", "2\u2666,2", "3\u2666,3", "4\u2666,4", "5\u2666,5", "6\u2666,6", "7\u2666,7", "8\u2666,8", "9\u2666,9", "10\u2666,10", "J\u2663,10", "Q\u2666,10", "K\u2666,10",
    "A\u2660,11", "2\u2660,2", "3\u2660,3", "4\u2660,4", "5\u2660,5", "6\u2660,6", "7\u2660,7", "8\u2660,8", "9\u2660,9", "10\u2660,10", "J\u2660,10", "Q\u2660,10", "K\u2660,10"]

def draw_card(player1_card, player2_card, player_input):
    same_card = True
    if player_input.lower() == "y":
        while same_card:
            player1_card.append(random.choice(pool_of_card))
            same_card = cek_same_card(player1_card, player2_card)
            if same_card == False:
                return player1_card
            player1_card.pop()
    elif player_input.lower() == "n":
        return player1_card
    else:
        your_input = input("Your input invalid. Please correct the input! 'y' or 'n': ")
        draw_card(player1_card, player2_card, your_input)

def game_of_blackjack(player_cards, player_score, computer_cards, computer_score, is_player_pass = "y"):
    while True:
        print(art.logo)
        if player_score == 21:
            print(f"\tYour cards: [{print_player_cards(player_cards)}]BlackJack!, current score: {player_score}")
        else:
            print(f"\tYour cards: [{print_player_cards(player_cards)}], current score: {player_score}")
    
        if is_player_pass == "y":
            print(f"\tComputer's first card: {computer_cards[0].split(',')[0]}, current score: {computer_score}")
        elif is_player_pass == "n":
            while computer_score < 17:
                computer_cards = draw_card(computer_cards, player_cards, "y")
                computer_score = cek_score(computer_cards)
            if computer_score == 21:
                print(f"\tComputer final hand: [{print_player_cards(computer_cards)}]BlackJack!, current score: {computer_score}")
            else:
                print(f"\tComputer final hand: [{print_player_cards(computer_cards)}], current score: {computer_score}")

            if player_score > 21 and computer_score > 21:
                if player_score > computer_score:
                    print("You win! \U0001F606")
                elif player_score == computer_score:
                    print("You draw! \U0001F642")
                else:
                    print("You lose! \U0001F979")
            elif player_score > 21:
                print("You lose! \U0001F979")
            elif computer_score > 21:
                if player_score == 21:
                    print("You win with BlackJack! \U0001F923")
                else:
                    print("You win! \U0001F606")
            elif player_score == 21 and player_score > computer_score:
                print("You win with BlackJack! \U0001F923")
            elif player_score > computer_score:
                print("You win! \U0001F606")
            elif player_score == computer_score:
                print("You draw! \U0001F642")
            else:
                print("You lose! \U0001F979")
            break
        while True:
            if player_score >= 21:
                is_player_pass = "n"
                break
            else:
                is_player_pass = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if is_player_pass == "y" or is_player_pass == "n":
                    break
                print("Your input is invalid. Please input the correct word!")
        player_cards = draw_card(player_cards, computer_cards, is_player_pass)
        player_score = cek_score(player_cards)

play_blackjack = play_game_blackjack()
while play_blackjack:
    player_cards = []
    computer_cards = []
    same_card = True
    while same_card == True:
        player_cards.append(random.choice(pool_of_card))
        computer_cards.append(random.choice(pool_of_card))
        same_card = cek_same_card(player_cards, computer_cards)
        if same_card == True:
            player_cards.pop()
            computer_cards.pop()

        if len(player_cards) == 2 and len(computer_cards) == 2:
            same_card = False
            break
        else:
            same_card = True
    player_score = cek_score(player_cards)
    computer_score = int(computer_cards[0].split(",")[1])
    game_of_blackjack(player_cards, player_score, computer_cards, computer_score)
    play_blackjack = play_game_blackjack()
    print("\033[2J\033[H", end="", flush=True) #clear console