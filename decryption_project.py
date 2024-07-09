import string

def decrypt(message, shift):

    alphabet = string.ascii_lowercase

    decrypted_message = ""

    for letter in message:
        if letter.lower() in alphabet:
            original_position = alphabet.index(letter.lower())
            new_position = (original_position - shift) % 26
            decrypted_letter = alphabet[new_position]

            if letter.isupper():
                decrypted_letter = decrypted_letter.upper()

            decrypted_message += decrypted_letter
        else:
            decrypted_message += letter
    print(f"\n\nHere is the original message\n******** {decrypted_message} ********\n")                


user_message = input("Enter a message: ")
shift_number = int(input("Enter a shift number: "))

decrypt(message = user_message, shift = shift_number)