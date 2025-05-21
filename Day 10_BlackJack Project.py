import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if cards == 11 and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def deal_card():
    card = random.choice(cards)
    return card

def play_game():
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    from art import logo
    print(logo)
    your_deck = []
    computer_deck = []
    if play == "n":
        print("BYE!")
    if play == "y":
        your_deck.extend([deal_card(), deal_card()])
        computer_deck.extend([deal_card(), deal_card()])

        your_current_score = sum(your_deck)
        computer_current_score = sum(computer_deck)
        print(f"Your cards: ({your_deck}), Current score: {your_current_score}")
        print(f"Computer's cards ({computer_deck}). Current Score: {computer_current_score}")

        if your_current_score == 21:
            calculate_score(your_deck)
            compare(your_current_score, computer_current_score)
            play_game()
        if computer_current_score == 21:
            calculate_score(computer_deck)
            compare(your_current_score, computer_current_score)
            play_game()
        if your_current_score > 21:
            calculate_score(your_current_score)
            print(f"Your cards: ({your_deck}), Current score: {your_current_score}")
        if computer_current_score > 21:
            print(f"Computer's cards ({computer_deck}). Current Score: {computer_current_score}")

        game_over = False
        while not game_over:
            if your_current_score < 21:
                draw = input("Type 'y' to get another card, type 'n' to pass: ").lower()#when n caught in an infinite loop
                if draw == "y":
                    your_deck.append(deal_card())
                    your_current_score = sum(your_deck)
                    print(f"Your cards: {your_deck}, Current score: {your_current_score}")

                if draw == "n":
                    print("okay!")
                    game_over = True

                if computer_current_score < 17:
                    computer_deck.append(deal_card())
                    computer_current_score = sum(computer_deck)
                    print(f"Computer's cards ({computer_deck}). Current Score: {computer_current_score}")
                if computer_current_score > 21:
                    game_over = True
            else:
                game_over = True
        print(f"Your final hand: ({your_deck}), final score: {your_current_score}")
        print(f"Computer's final hand: ({computer_deck}), final score: {computer_current_score}")
        compare(your_current_score, computer_current_score)

    play_game()



def compare(your_current_score, computer_current_score):
    if computer_current_score == your_current_score:
        print("it's a draw")
    elif computer_current_score == 0:
        print("You lose")
    elif your_current_score == 0:
        print("blackJack")
    elif computer_current_score > 21:
        print("Computer loses, you win!")
    elif your_current_score > 21:
        print("You went over. You lose")
    elif computer_current_score > your_current_score:
        print("computer wins!")
    else:
        print("you win!")

play_game()
