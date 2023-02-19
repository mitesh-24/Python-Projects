import random


def deal_card():
    cards = [2,3,4,5,6,7,8,9,10,11,10,10,10]
    card = random.choices(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:   
        return 0

    if 11 in cards and sum(cards) > 21:     #adjust the value of ace card according to the sum
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(user_score,computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    elif computer_score == user_score:
        return "Draw"
    elif computer_score > user_score:
        return "Dealer won !!"
    elif computer_score < user_score:
        return "You won !!" 
    elif computer_score == 0:
        return "dealer has a blackjack !!"
    elif user_score == 0:
        return "You have a blackJack !!"
    else:
        return "You loose !!"

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards {user_cards}, Your score : {user_score}")
        print(f"Dealer's first card {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(print("Do you want to draw another card? 'y' -> yes  'n' -> no"))
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

        #compare the scores now
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        print(f"   Your final hand: {user_cards}, final score: {user_score}")
        print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare_score(user_score, computer_score))



while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()
