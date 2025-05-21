from hangman_art import stages, logo
import random
from hangman_words import word_list
print(logo)

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)


placeholder = ""
for letters in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []


while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"you've already guessed {guess}!")

    display = ""

    for letters in chosen_word:
        if letters == guess:
            display += letters
            correct_letters.append(guess)
        elif letters in correct_letters:  # have to check if its in the list
            display += letters  # have to add onto the string "display"
        else:
            display += "_"
    print(display)


    if "_" not in display:
        print(f"IT WAS {chosen_word}! YOU GOT IT!")
        game_over = True

    if guess not in chosen_word:
        lives -= 1
        print(f"You've guessed {guess}, that's not in the word. You've lost a life.")
        print(f"****************************{lives}/6 LIVES LEFT****************************")
    elif lives == 0:
        print(f"IT WAS {chosen_word}! YOU LOST !")
        game_over = True
    print(stages[lives])