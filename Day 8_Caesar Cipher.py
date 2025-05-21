alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
message = input("What is your message?: ").lower()
shift = int(input("Type the shift number: "))


def caesar(original_text, shift_amount, direction):
    cipher = ""
    if direction == "decode":
        shift_amount *= -1
    for letters in original_text:
        if letters not in alphabet:
            cipher += letters
        else:
            shifted_message = alphabet.index(letters) + shift_amount
            shifted_message %= len(alphabet)#remainder will be the shift_amount
            cipher += (alphabet[shifted_message])
    print(f"Your message is {cipher}.", end="")
    game_over = False

    while not game_over:
        again = input("\nWould you like to go again? Type 'yes' or 'no': ").lower()
        if again == "yes":
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
            message = input("What is your message?: ").lower()
            shift = int(input("Type the shift number: "))
            return caesar(message, shift, direction)
        else:
            print("see ya later!")
            game_over = True





caesar(message,shift, direction)