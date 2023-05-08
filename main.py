from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def ceasar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            original_position = alphabet.index(char)
            new_position = original_position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f'The {cipher_direction} text is: {end_text}')


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number (not more than 13):\n"))

    shift = shift % 26

    ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Would you like to Decryt this message? Type 'y' if so, if not then type 'n'.")
    if result == "n":
        should_continue = False
        print("Goodbye")
