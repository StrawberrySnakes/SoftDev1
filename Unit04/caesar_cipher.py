def encrypt_letter(letter, shift):
    # first turn the letter into a code
    #then shift the code by adding to shift value
    #then turn that code back into a letter 
    #return that letter 
    if is_alphabetic(letter) == True:
        letter_code = ord(letter)
        shift_code = letter_code + shift
        shifted_letter = chr(shift_code)
        return shifted_letter
    else:
        return ""

def is_alphabetic(character):
    char_code = ord(character)
    result = char_code >= 65 and char_code <=90
    return result

def decrypt_letter(letter, shift):
    #tranlate letter into code 
    letter_code = ord(letter)
    #subtrat the shift ammount from the letter code
    shifted_letter_code = letter_code - shift
    #translate into a letter
    new_letter = chr(shifted_letter_code)
    return new_letter

def encrypt_message(plaintext, shift=3):
    ciphertext = ""
    for index in range(len(plaintext)):
        character = plaintext[index]
        ciphertext += encrypt_letter(character, shift)
    return ciphertext
    """
    ciphertext = ''
    index = 0
    while index < len(plaintext):
        character = plaintext[index]
        ciphertext += encrypt_letter(character, shift)
        index += 1
    return ciphertext
    """

def decrypt_message(ciphertext, shift):
    plaintext = ''

    for character in ciphertext:
        plaintext += decrypt_letter(character, shift)
    return plaintext
    
    """
    index = 0
    while index < len(plaintext):
        character = ciphertext[index]
        plaintext += decrypt_letter(ciphertext[index], shift)
        index += 1
    return plaintext
    """


def main():
    decrypt_message("yhalxbpgglz", 2)
    decrypt_message("yhalxbpgglz", 5)
    """
    phrase = input("Enter a message: ")
    for token in phrase.split():
        encrypted = encrypt_message(token)
        print(encrypted)
    
    letter = input("Enter a letter: ")
    print(encrypt_letter(letter, 3))
    print(decrypt_letter(letter, 3))
    print(encrypt_message("HELLO", 4))
    """
if __name__ == "__main__":
    main()


