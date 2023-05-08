from art import logo
# Importing the ASCII Art from the art.py module
print(logo)

# The list which will be used to Encrypt/Decrypt or text
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def ceasar(start_text, shift_amount, cipher_direction):
    # First we set the "end_text" which will hold our Encrypted || Decrypted Text.
    end_text = ""
    # Secondly we check whether we are Decrypting or Encrypting.
    if cipher_direction == "decode":
        shift_amount *= -1
    # Thirdly we loop through each character within our text.
    for char in start_text:
        # Bug Fix: Here we have an exception for any character that is not within the alphabet list.
        if char in alphabet:
            original_position = alphabet.index(char)
            new_position = original_position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    # Finally we return the transformed text back to the user.
    print(f'The {cipher_direction} text is: {end_text}')


# We don't just want the program to end as soon as the process is complete so we instead ask the the user if they wish
# to continue using the program or if they want to end the program.
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Would you like to Decrypt this message? Type 'y' if so, if not then type 'n':\n")
    if result == "n":
        should_continue = False
        print("Goodbye")
